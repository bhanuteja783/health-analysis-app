
def detect_diseases(cleaned_text):
    diseases = {
        "thyroid": "Your thyroid levels may be imbalanced. Avoid soy, eat iodine-rich foods, and consult an endocrinologist.",
        "cholesterol": "High cholesterol detected. Avoid fried food, eat more fiber and exercise regularly.",
        "sugar": "Elevated sugar levels. Monitor glucose, eat low-GI foods, and reduce sweets.",
        "blood pressure": "Abnormal BP. Limit salt, manage stress, and exercise daily.",
        "jaundice": "Signs of jaundice. Rest well, hydrate, avoid fatty foods and see a doctor.",
        "fever": "Fever detected. Stay hydrated and monitor symptoms. If persistent, seek medical help."
    }

    found = {}
    text_lower = cleaned_text.lower()

    for keyword, advice in diseases.items():
        if keyword in text_lower:
            found[keyword] = advice

    return found
