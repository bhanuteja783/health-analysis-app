import pytesseract
import cv2
import numpy as np
from PIL import Image
import re

def extract_text_from_image(pil_image):
    image = np.array(pil_image.convert('RGB'))
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    gray = cv2.medianBlur(gray, 3)
    text = pytesseract.image_to_string(gray)
    cleaned_text = re.sub(r'[^a-zA-Z0-9:\n.%/-]+', ' ', text)
    return cleaned_text