import re
import easyocr
from PIL import Image
import numpy as np

reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(image_path):
    """
    Extract and clean text from uploaded medical report image.
    """
    try:
        img = Image.open(image_path)
        result = reader.readtext(np.array(img), detail=0)
        raw_text = ' '.join(result)
        return clean_text(raw_text)
    except Exception as e:
        return f"Error extracting text: {e}"

def clean_text(text):
    cleaned = text.replace('\n', ' ')
    cleaned = re.sub(r'\s+', ' ', cleaned)
    cleaned = re.sub(r'[^a-zA-Z0-9:.,()%+-/ ]', '', cleaned)
    return cleaned.strip()


