from typing import Tuple
from torch import Tensor
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
from sdg.config import WORK_DIRECTORY


async def execute(args):
    print("Starting execute")
    if args.description != None and args.description != '':
        model = MusicGen.get_pretrained('facebook/musicgen-small')
        model.set_generation_params(duration=int(args.time))
        wav = model.generate([args.description])
        generate_audio(model, wav)
        print("Successfully completed execute.")


def generate_audio(model: MusicGen, wav: Tuple[Tensor, Tensor]):
    for idx, one_wav in enumerate(wav):
        file_name = f'{WORK_DIRECTORY}/{idx}'
        audio_write(file_name, one_wav.cpu(), model.sample_rate,
                    strategy='loudness', loudness_compressor=True)
