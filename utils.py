import re

import pytesseract
from pytesseract import TesseractNotFoundError


def extract_text_from_image(image):
    """Extract and clean English text from a PIL Image using Tesseract OCR."""
    try:
        if image is None:
            return ""

        raw_text = pytesseract.image_to_string(image, config="--psm 6")
        return clean_text(raw_text)
    except TesseractNotFoundError:
        return (
            "Error extracting text: OCR engine is not installed on the server. "
            "Please try again after the app finishes redeploying."
        )
    except Exception as exc:
        return f"Error extracting text: {exc}"


def clean_text(text):
    """Normalize whitespace and remove unsupported characters."""
    if not isinstance(text, str):
        return ""

    cleaned = text.replace("\n", " ")
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = re.sub(r"[^a-zA-Z0-9:.,()%+\-/ ]", "", cleaned)
    return cleaned.strip()
