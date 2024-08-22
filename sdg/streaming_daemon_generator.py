from typing import Tuple
from torch import Tensor
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
from sdg.audio import Audio
from sdg.sender import Sender
from sdg.config import WORK_DIRECTORY,SHOULD_SEND


async def execute(audio: Audio, shouldSend: bool):
    print("Starting execute")
    shouldSend = shouldSend
    if audio.description != None and audio.description != '':
        print('Generating Music Description:', audio.description)
        model = MusicGen.get_pretrained('facebook/musicgen-small')
        model.set_generation_params(duration=int(15))
        wav = model.generate([audio.description])
        generate_audio(audio, model, wav)
        print("Successfully completed execute.")


def generate_audio(audio: Audio, model: MusicGen, wav: Tuple[Tensor, Tensor]):
    for idx, one_wav in enumerate(wav):
        file_name = f'{WORK_DIRECTORY}/unsent/{idx}_{audio.name}_{audio.artist}_{audio.album}'
        audio_write(file_name, one_wav.cpu(), model.sample_rate,
                        strategy='loudness', loudness_compressor=True)
        if SHOULD_SEND:
            Sender().send_audio_files(audio, file_name)
