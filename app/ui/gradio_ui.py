import gradio as gr


def add_user_message(message: str, history: list[dict]):
    return "", history + [{"role": "user", "content": message}]


def build_ui(chat_fn) -> gr.Blocks:
    with gr.Blocks() as ui:
        with gr.Row():
            chatbot = gr.Chatbot(height=500)
            image_output = gr.Image(height=500, interactive=False)

        with gr.Row():
            audio_output = gr.Audio(autoplay=True)

        with gr.Row():
            message_box = gr.Textbox(label="Chat with our AI Assistant:")

        message_box.submit(
            add_user_message,
            inputs=[message_box, chatbot],
            outputs=[message_box, chatbot]
        ).then(
            chat_fn,
            inputs=chatbot,
            outputs=[chatbot, audio_output, image_output]
        )

    return ui
