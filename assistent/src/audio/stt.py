from faster_whisper import WhisperModel
import assistent.config as config

class Transcriber:
    def __init__(self):
        self.model = WhisperModel(
            config.WHISPER_MODEL_SIZE,
            device=config.WHISPER_DEVICE,
            compute_type=config.WHISPER_COMPUTE_TYPE
        )

    def transcribe(self, audio_data) -> str:
        segments, _ = self.model.transcribe(
            audio_data,
            language="pt",
            beam_size=1,
            initial_prompt=config.INITIAL_PROMPT
        )
        return " ".join([segment.text for segment in segments]).strip()