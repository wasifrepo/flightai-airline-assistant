from app.config import TTS_MODEL, TTS_VOICE
from app.services.openai_client import get_client


def text_to_speech(text: str) -> bytes:
    client = get_client()
    response = client.audio.speech.create(
        model=TTS_MODEL,
        voice=TTS_VOICE,
        input=text
    )
    return response.content
