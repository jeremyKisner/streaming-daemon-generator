from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Audio(BaseModel):
    name: Optional[str] = None
    artist: Optional[str] = None
    album: Optional[str] = None
    description: str

@app.get("/healthz")
def read_root():
    return {"OK"}


@app.post("/audio/generate")
async def put_audio_generate(audio: Audio):
    return audio
