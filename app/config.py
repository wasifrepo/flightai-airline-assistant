import os

MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
DB_PATH = os.getenv("DB_PATH", "database/prices.db")

IMAGE_MODEL = os.getenv("OPENAI_IMAGE_MODEL", "dall-e-3")
TTS_MODEL = os.getenv("OPENAI_TTS_MODEL", "gpt-4o-mini-tts")
TTS_VOICE = os.getenv("OPENAI_TTS_VOICE", "coral")

