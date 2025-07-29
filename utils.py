import pytesseract
from PIL import Image
import re

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        raw_text = pytesseract.image_to_string(img)
        return clean_text(raw_text)
    except Exception as e:
        return f"Error extracting text: {e}"

def clean_text(text):
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9:.,()%+\-/ ]', '', text)
    return text.strip()

def detect_diseases(cleaned_text):
    disease_keywords = {
        "thyroid": "Your thyroid levels are abnormal. Consult an endocrinologist. Foods rich in iodine like fish may help.",
        "cholesterol": "Your cholesterol is outside normal range. Avoid fried foods and increase fiber intake. Daily walking helps.",
        "sugar": "High or low sugar levels detected. Diabetics should monitor diet, avoid sweets, and stay active.",
        "blood pressure": "Abnormal blood pressure detected. Reduce salt intake for high BP. Hydrate well for low BP.",
        "jaundice": "Signs of jaundice found. Avoid fatty foods. Stay hydrated and rest. Get liver function tests.",
        "fever": "Possible fever symptoms. Monitor temperature and take paracetamol if necessary. Seek medical advice.",
        "infection": "Infection markers noted. Drink warm fluids, rest, and consult a doctor for antibiotics if needed."
    }
    found = {}
    for disease, advice in disease_keywords.items():
        if disease.lower() in cleaned_text.lower():
            found[disease] = advice
    return found

