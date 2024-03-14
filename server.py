from sdg.audio import Audio
from sdg.streaming_daemon_generator import execute
import asyncio
from fastapi import FastAPI


app = FastAPI()

@app.get("/healthz")
def read_root():
    return {"OK"}

@app.post("/audio/generate")
async def put_audio_generate(audio: Audio):
    asyncio.create_task(execute(audio))
    return {"Audio eneration started, check back soon!"}
