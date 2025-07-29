from deep_translator import DeeplTranslator

LANGUAGES = [
    "English", "Hindi", "Telugu", "Tamil", "Kannada", "Malayalam", "Urdu", 
    "Spanish", "French", "German", "Chinese", "Arabic", "Bengali", "Japanese"
]

LANG_CODE_MAP = {
    "English": "EN",
    "Hindi": "HI",
    "Telugu": "TE",
    "Tamil": "TA",
    "Kannada": "KN",
    "Malayalam": "ML",
    "Urdu": "UR",
    "Spanish": "ES",
    "French": "FR",
    "German": "DE",
    "Chinese": "ZH",
    "Arabic": "AR",
    "Bengali": "BN",
    "Japanese": "JA"
}

def translate_text(text, language):
    try:
        target_lang = LANG_CODE_MAP.get(language, "EN")
        return DeeplTranslator(source="EN", target=target_lang).translate(text)
    except Exception as e:
        return f"Translation error: {e}"

