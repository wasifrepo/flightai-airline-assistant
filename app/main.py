import asyncio
import sys
from dotenv import load_dotenv

from app.config import MODEL
from app.prompts import SYSTEM_MESSAGE
from app.tools.schemas import TOOLS
from app.tools.handlers import handle_tool_calls_and_return_cities
from app.services.openai_client import get_client
from app.services.audio_service import text_to_speech
from app.services.image_service import generate_city_image
from app.ui.gradio_ui import build_ui



load_dotenv()

# Optional Windows fix to reduce noisy asyncio disconnect logs
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def chat_with_tools_and_media(history: list[dict]):
    client = get_client()

    sanitized_history = [{"role": h["role"], "content": h["content"]} for h in history]
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}] + sanitized_history

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS
    )

    cities = []
    image = None

    while response.choices[0].finish_reason == "tool_calls":
        model_message = response.choices[0].message

        tool_responses, tool_cities = handle_tool_calls_and_return_cities(model_message)
        cities.extend(tool_cities)

        messages.append(model_message)
        messages.extend(tool_responses)

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS
        )

    reply_text = response.choices[0].message.content or ""
    sanitized_history.append({"role": "assistant", "content": reply_text})

    voice_audio = text_to_speech(reply_text)

    if cities:
        image = generate_city_image(cities[0])

    return sanitized_history, voice_audio, image


def main():
    ui = build_ui(chat_with_tools_and_media)
    ui.launch(
    inbrowser=True,
    debug=False,
    show_error=True
)



if __name__ == "__main__":
    main()
