# app/services/audio_service.py
from openai import AsyncOpenAI
from app.core.config import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
async def transcribe_audio(audio_path: str) -> str:
    """
    Transcribes audio file to text using Whisper API.
    """
    with open(audio_path, "rb") as f:
        transcript =await client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    return transcript.text