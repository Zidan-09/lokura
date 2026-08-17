import queue
import threading
import win32com.client

SVSFlagsAsync = 1
SVSFPurgeBeforeSpeak = 2

class TextToSpeech:
    def __init__(self):
        print("[TTS] Inicializando motor de síntese de voz (SAPI5 com cancelamento)...")
        self.speech_queue = queue.Queue()
        
        # Thread dedicada para processar a fila de áudio
        self.worker_thread = threading.Thread(target=self._speech_worker, daemon=True)
        self.worker_thread.start()

    def _speech_worker(self):
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Rate = 3 

        while True:
            text = self.speech_queue.get()
            if text is None:
                break
            
            try:
                flags = SVSFlagsAsync | SVSFPurgeBeforeSpeak
                speaker.Speak(text, flags)
            except Exception as e:
                print(f"[TTS Erro]: {e}")
            finally:
                self.speech_queue.task_done()

    def speak(self, text: str):
        """Esvazia mensagens antigas e envia apenas o texto mais recente para reprodução."""
        if not text:
            return

        with self.speech_queue.mutex:
            self.speech_queue.queue.clear()

        self.speech_queue.put(text)