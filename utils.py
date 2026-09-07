import re
from functools import lru_cache

import numpy as np


@lru_cache(maxsize=1)
def get_reader():
    """Create the EasyOCR reader only when OCR is actually needed."""
    import easyocr

    return easyocr.Reader(["en"], gpu=False)


def extract_text_from_image(image):
    """Extract and clean text from a PIL Image using EasyOCR."""
    try:
        if image is None:
            return ""

        reader = get_reader()
        result = reader.readtext(np.array(image), detail=0)
        raw_text = " ".join(result)
        return clean_text(raw_text)
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
