import os

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

SAMPLE_RATE = 16000
CHUNK_SIZE = 512
SILENCE_THRESHOLD = 1.5

WAKE_WORD = "Lokura"
WHISPER_MODEL_SIZE = "small"
WHISPER_DEVICE = "cpu"
WHISPER_COMPUTE_TYPE = "int8"
INITIAL_PROMPT = (
    f"O nome do assistente é {WAKE_WORD}. Transcreva nomes próprios como Manel com precisão. "
    "Conversa informal em português do Brasil com contrações e gírias do dia a dia. "
    "Exemplos de fala: 'Você tá aí?', 'A gente vai pra lá agora', 'Tá ali no canto', 'Entendeu o bagulho?', 'Aí mano, suave?', 'Pô, aí é foda', 'Tô ligado', 'Tá bom'."
)

OLLAMA_MODEL = "llama3.2"

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")