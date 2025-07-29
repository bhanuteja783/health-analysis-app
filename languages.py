from googletrans import Translator

translator = Translator()

LANGUAGES = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Urdu": "ur",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Bengali": "bn",
    "Spanish": "es",
    "French": "fr",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-cn",
    "Russian": "ru"
}

def translate_text(text, target_lang_code):
    try:
        translated = translator.translate(text, dest=target_lang_code)
        return translated.text
    except:
        return text