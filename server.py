from sdg.audio import Audio
from sdg.streaming_daemon_generator import execute, background_send

import asyncio
import threading
from fastapi import FastAPI
import uvicorn


app = FastAPI()

# Create a thread for the background task
background_thread = threading.Thread(target=background_send)
background_thread.daemon = True  # Set the thread as daemon so it exits when the main thread exits
background_thread.start()


@app.get("/")
def read_root():
    return {"OK"}

@app.post("/audio/generate")
async def put_audio_generate(audio: Audio):
    asyncio.create_task(execute(audio))
    return {"Audio generation started, check back soon!"}

if __name__ == '__main__':
    uvicorn.run(app, port=8081, host='0.0.0.0')
