from sdg.audio import Audio
import os
import requests
import time
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

WORK_DIRECTORY = 'audio'

async def execute(audio: Audio):
    print("Starting execute")
    if audio.description != None and audio.description != '':
        print('Generating Music Description:', audio.description)
        model = MusicGen.get_pretrained('facebook/musicgen-small')
        model.set_generation_params(duration=int(15))
        wav = model.generate([audio.description])
        for idx, one_wav in enumerate(wav):
            file_name = f'{WORK_DIRECTORY}/{idx}_{audio.name}_{audio.artist}_{audio.album}'
            audio_write(file_name, one_wav.cpu(), model.sample_rate,
                        strategy='loudness', loudness_compressor=True)
        print("Successfully completed execute")


def background_send():
    while True:
        print("Start send...")
        send()
        print("Finished send")
        time.sleep(15)


def send():
    _dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', WORK_DIRECTORY)
    sent_files = []
    for file_name in os.listdir(_dir):
        file_path = os.path.join(_dir, file_name)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'rb') as file:
                    url = 'http://localhost:8082/audio/insert'
                    files = {'audioFile': (file_name, file)}
                    data = {
                        'name': audio.name,
                        'artist': audio.artist,
                        'album': audio.album,
                        'description': audio.description,
                    }
                    response = requests.post(url, files=files, data=data)
                    if response.status_code != 200:
                        print('Failure:', response.text,
                              audio.name, audio.artist, audio.album)
                    else:
                        print('Success:', response.text,
                              audio.name, audio.artist, audio.album)
                        sent_files.append(file_path)
            except IOError as e:
                print('Error opening file:', e)
    if len(sent_files) > 0:
         for f in sent_files:
            time.sleep(5)
            print("deleting file", f)
            os.remove(f)
