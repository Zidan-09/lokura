import ollama
import config

class Brain:
    def __init__(self):
        self.model = config.OLLAMA_MODEL

        self.client = ollama.Client(host=config.OLLAMA_HOST)
        
        self.conversation_history = [
            {
                "role": "system",
                "content": (
                    f"Você é {config.WAKE_WORD}, um assistente virtual sarcástico, altamente inteligente, "
                    "direto ao ponto e sem enrolação,"
                    "Responda de forma curta, natural e conversacional (no máximo 2 ou 3 frases), "
                    "pois suas respostas serão sintetizadas em áudio."
                )
            }
        ]

    def generate_response(self, prompt: str) -> str:
        if not prompt:
            return "O que foi? Fala logo."

        self.conversation_history.append({
            "role": "user",
            "content": prompt
        })

        try:
            response = self.client.chat(
                model=self.model,
                messages=self.conversation_history,
                options={
                    "temperature": 0.7,
                }
            )

            assistant_reply = response["message"]["content"]

            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_reply
            })

            return assistant_reply

        except Exception as e:
            print(f"[LLM Erro]: Não foi possível conectar ao Ollama. {e}")
            return "Meu cérebro travou ou o Ollama não tá rodando. Dá uma olhada aí."