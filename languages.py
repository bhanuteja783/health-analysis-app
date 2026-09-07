from deep_translator import GoogleTranslator

LANGUAGES = [
    "en", "hi", "te", "ta", "kn", "mr", "bn", "gu", "ml",  # Indian
    "es", "fr", "de", "zh", "ja", "ru", "ar", "pt",         # Global
]


def translate_text(text, target_lang):
    """Translate text and fall back to the original text if translation fails."""
    if not isinstance(text, str) or not text.strip():
        return ""

    if target_lang == "en" or target_lang not in LANGUAGES:
        return text

    try:
        return GoogleTranslator(source="auto", target=target_lang).translate(text)
    except Exception:
        return text
