from deep_translator import GoogleTranslator

LANGUAGES = [
    "en", "hi", "te", "ta", "kn", "mr", "bn", "gu", "ml",  # Indian
    "es", "fr", "de", "zh", "ja", "ru", "ar", "pt"         # Global
]

def translate_text(text, target_lang):
    try:
        if target_lang == "en":
            return text
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"(Translation error: {e})"

