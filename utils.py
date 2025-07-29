import re
import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(image):
    """
    Extract and clean text from a PIL Image using EasyOCR.
    """
    try:
        result = reader.readtext(np.array(image), detail=0)
        raw_text = ' '.join(result)
        return clean_text(raw_text)
    except Exception as e:
        return f"Error extracting text: {e}"

def clean_text(text):
    cleaned = text.replace('\n', ' ')
    cleaned = re.sub(r'\s+', ' ', cleaned)
    cleaned = re.sub(r'[^a-zA-Z0-9:.,()%+-/ ]', '', cleaned)
    return cleaned.strip()
