def detect_diseases(cleaned_text):
    """Find supported health-related keywords in extracted report text.

    This is keyword detection only; it does not diagnose a medical condition.
    """
    if not isinstance(cleaned_text, str) or not cleaned_text.strip():
        return {}

    diseases = {
        "thyroid": "Possible thyroid-related finding detected. Review the reported TSH/T3/T4 values with a qualified clinician.",
        "cholesterol": "Cholesterol-related finding detected. Review the LDL, HDL and triglyceride values with a qualified clinician.",
        "sugar": "Blood-sugar-related finding detected. Review the glucose/HbA1c values with a qualified clinician.",
        "blood pressure": "Blood-pressure-related finding detected. Review the reported BP values with a qualified clinician.",
        "jaundice": "A jaundice-related term was found in the report. Discuss the finding and relevant liver/bilirubin results with a qualified clinician.",
        "fever": "A fever-related term was found in the report. Interpret it together with the reported temperature, symptoms and clinical context."
    }

    text_lower = " ".join(cleaned_text.lower().split())
    return {
        keyword: advice
        for keyword, advice in diseases.items()
        if keyword in text_lower
    }
