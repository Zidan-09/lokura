import queue
import sys
import numpy as np
import sounddevice as sd
import torch
import config

class AudioListener:
    def __init__(self):
        self.vad_model, _ = torch.hub.load(
            repo_or_dir='snakers4/silero-vad',
            model='silero_vad',
            force_reload=False,
            onnx=False
        )
        self.audio_queue = queue.Queue()

    def _audio_callback(self, indata, frames, time_info, status):
        if status:
            print(f"Status do áudio: {status}", file=sys.stderr)
        self.audio_queue.put(indata.copy())

    def listen_loop(self, on_speech_detected):
        audio_buffer = []
        silence_counter = 0
        is_speaking = False

        with sd.InputStream(
            samplerate=config.SAMPLE_RATE,
            channels=1,
            dtype='float32',
            blocksize=config.CHUNK_SIZE,
            callback=self._audio_callback
        ):
            while True:
                chunk = self.audio_queue.get()
                chunk_tensor = torch.from_numpy(chunk.squeeze())
                speech_prob = self.vad_model(chunk_tensor, config.SAMPLE_RATE).item()

                if speech_prob > 0.5:
                    if not is_speaking:
                        is_speaking = True
                        print("\n[Escutando...]", end="", flush=True)

                    audio_buffer.append(chunk)
                    silence_counter = 0

                elif is_speaking:
                    audio_buffer.append(chunk)
                    silence_counter += config.CHUNK_SIZE / config.SAMPLE_RATE

                    if silence_counter >= config.SILENCE_THRESHOLD:
                        is_speaking = False
                        silence_counter = 0

                        full_audio = np.concatenate(audio_buffer, axis=0).ravel()
                        audio_buffer = []

                        on_speech_detected(full_audio)