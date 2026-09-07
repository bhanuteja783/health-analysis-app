import re


HEALTH_TERMS = {
    "thyroid": (
        r"\bthyroid\b|\bTSH\b|\bT3\b|\bT4\b",
        "A thyroid-related term or lab marker was found. Review the reported TSH/T3/T4 values with a qualified clinician.",
    ),
    "cholesterol": (
        r"\bcholesterol\b|\bLDL\b|\bHDL\b|\btriglycerides?\b",
        "A cholesterol-related term or lipid marker was found. Review LDL, HDL and triglyceride values with a qualified clinician.",
    ),
    "blood sugar": (
        r"\bsugar\b|\bglucose\b|\bHbA1c\b|\bA1c\b",
        "A blood-sugar-related term or marker was found. Review glucose/HbA1c values with a qualified clinician.",
    ),
    "blood pressure": (
        r"\bblood pressure\b|\bBP\b",
        "A blood-pressure-related term was found. Review the reported BP values with a qualified clinician.",
    ),
    "jaundice": (
        r"\bjaundice\b|\bbilirubin\b",
        "A jaundice-related term or bilirubin marker was found. Discuss the result with a qualified clinician.",
    ),
    "fever": (
        r"\bfever\b|\btemperature\b",
        "A fever-related term was found. Interpret it together with the reported temperature, symptoms and clinical context.",
    ),
}


def detect_diseases(cleaned_text):
    """Find supported health-related terms in extracted report text.

    This is pattern matching only; it does not diagnose a medical condition.
    """
    if not isinstance(cleaned_text, str) or not cleaned_text.strip():
        return {}

    return {
        label: advice
        for label, (pattern, advice) in HEALTH_TERMS.items()
        if re.search(pattern, cleaned_text, flags=re.IGNORECASE)
    }
