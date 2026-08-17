import assistent.config as config
from assistent.src.audio.listener import AudioListener
from assistent.src.audio.stt import Transcriber
from assistent.src.audio.tts import TextToSpeech
from assistent.src.llm.brain import Brain
from assistent.src.utils.wake_word import check_wake_word, extract_prompt

def main():
    transcriber = Transcriber()
    listener = AudioListener()
    brain = Brain()
    tts = TextToSpeech()

    def process_audio(full_audio):
        transcription = transcriber.transcribe(full_audio)

        if not transcription:
            return

        if check_wake_word(transcription):
            prompt_limpo = extract_prompt(transcription)

            resposta = brain.generate_response(prompt_limpo)

            tts.speak(resposta)
            
        else:
            print("-> (Descartado: Palavra de ativação não encontrada)")

        print(f"\n=== {config.WAKE_WORD} está ouvindo... ===")

    print(f"\n=== {config.WAKE_WORD} está ouvindo... (Fale algo) ===")
    listener.listen_loop(on_speech_detected=process_audio)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\nEncerrando o {config.WAKE_WORD}.")