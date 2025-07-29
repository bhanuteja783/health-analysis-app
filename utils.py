import pytesseract
from PIL import Image
import re
import numpy as np  # Reserved if needed later

def extract_text_from_image(image_path):
    """
    Extracts and cleans text from the uploaded medical report image.
    """
    try:
        # Load image using PIL
        img = Image.open(image_path)

        # Use pytesseract to extract raw text
        raw_text = pytesseract.image_to_string(img)

        # Clean the text
        cleaned = clean_text(raw_text)

        return cleaned

    except Exception as e:
        return f"Error extracting text: {e}"

def clean_text(text):
    """
    Cleans the extracted OCR text by removing unwanted characters,
    fixing spacing, and standardizing formatting.
    """
    # Remove newlines
    cleaned = text.replace('\n', ' ')

    # Remove multiple spaces
    cleaned = re.sub(r'\s+', ' ', cleaned)

    # Allow only useful characters
    cleaned = re.sub(r'[^a-zA-Z0-9:.,()%+-/ ]', '', cleaned)

    # Strip leading/trailing spaces
    cleaned = cleaned.strip()

    return cleaned