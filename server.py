from sdg.audio import Audio
from sdg.streaming_daemon_generator import execute
from fastapi import FastAPI


app = FastAPI()

@app.get("/healthz")
def read_root():
    return {"OK"}

@app.post("/audio/generate")
async def put_audio_generate(audio: Audio):
    execute(audio)
    return audio
