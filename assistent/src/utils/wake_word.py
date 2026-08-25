import re
import config

def check_wake_word(text: str) -> bool:
    pattern = r'\b' + re.escape(config.WAKE_WORD) + r'\b'
    return bool(re.search(pattern, text, re.IGNORECASE))

def extract_prompt(text: str) -> str:
    pattern = r'\b' + re.escape(config.WAKE_WORD) + r'\b'
    clean_text = re.sub(pattern, '', text, flags=re.IGNORECASE).strip()
    return clean_text