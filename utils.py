import pytesseract
from PIL import Image
import re
import numpy as np  # Reserved if needed later

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        raw_text = pytesseract.image_to_string(img)
        cleaned = clean_text(raw_text)
        return cleaned
    except Exception as e:
        return f"Error extracting text: {e}"

def clean_text(text):
    cleaned = text.replace('\n', ' ')
    cleaned = re.sub(r'\s+', ' ', cleaned)
    cleaned = re.sub(r'[^a-zA-Z0-9:.,()%+-/ ]', '', cleaned)
    cleaned = cleaned.strip()
    return cleaned

def detect_diseases(cleaned_text):
    findings = {}
    if "TSH" in cleaned_text or "thyroid" in cleaned_text.lower():
        findings["Thyroid"] = "Detected abnormal levels. Consult endocrinologist."
    if any(x in cleaned_text for x in ["cholesterol", "HDL", "LDL", "triglycerides"]):
        findings["Cholesterol"] = "Cholesterol indicators found. Check levels."
    if any(x in cleaned_text for x in ["glucose", "sugar", "diabetes"]):
        findings["Diabetes"] = "Blood sugar related terms found."
    if any(x in cleaned_text for x in ["BP", "blood pressure", "mmHg"]):
        findings["Blood Pressure"] = "Blood pressure terms found."
    if "bilirubin" in cleaned_text or "SGPT" in cleaned_text or "SGOT" in cleaned_text:
        findings["Liver Function / Jaundice"] = "Possible liver function indicators found."
    if not findings:
        findings["Status"] = "No common diseases found based on the keywords."
    return findings
