from deep_translator import GoogleTranslator

LANGUAGES = {
    "en": "english",
    "te": "telugu",
    "hi": "hindi",
    "ta": "tamil",
    "ml": "malayalam",
    "kn": "kannada",
    "ur": "urdu",
    "es": "spanish",
    "fr": "french",
    "zh-CN": "chinese (simplified)",
    "de": "german",
    "ru": "russian",
    "ja": "japanese"
}

def translate_text(text, target_lang):
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        return f"Translation error: {e}"
