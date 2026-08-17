import queue
import threading

import pyttsx3


class TextToSpeech:
    def __init__(self):
        print("[TTS] Inicializando motor de síntese de voz...")

        self.speech_queue = queue.Queue()

        self.worker_thread = threading.Thread(
            target=self._speech_worker,
            daemon=True
        )
        self.worker_thread.start()

    def _speech_worker(self):
        try:
            speaker = pyttsx3.init()

            speaker.setProperty("rate", 180)

            while True:
                text = self.speech_queue.get()

                if text is None:
                    break

                try:
                    speaker.say(text)
                    speaker.runAndWait()

                except Exception as e:
                    print(f"[TTS Erro]: {e}")

                finally:
                    self.speech_queue.task_done()

        except Exception as e:
            print(f"[TTS Erro]: Não foi possível inicializar o motor: {e}")

    def speak(self, text: str):
        if not text:
            return

        with self.speech_queue.mutex:
            self.speech_queue.queue.clear()

        self.speech_queue.put(text)