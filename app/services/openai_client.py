import os
from openai import OpenAI

_client: OpenAI | None = None


def get_client() -> OpenAI:
    """
    Lazily create and return a single OpenAI client instance.
    This prevents import-time failures if OPENAI_API_KEY isn't loaded yet.
    """
    global _client
    if _client is None:
        # OpenAI() reads OPENAI_API_KEY from the environment
        _client = OpenAI()
    return _client
