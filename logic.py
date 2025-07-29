import re

def analyze_health_data(text):
    ranges = {
        "Glucose": (70, 140),
        "TSH": (0.4, 4.0),
        "LDL": (0, 130),
        "HDL": (40, 60),
        "Bilirubin": (0.1, 1.2),
        "Systolic BP": (90, 120),
        "Diastolic BP": (60, 80)
    }

    suggestions = {
        "Glucose": {
            "high": "Reduce sugar intake, walk 30 mins daily, eat more fiber.",
            "low": "Eat small frequent meals, add carbs, avoid fasting."
        },
        "TSH": {
            "high": "Check for hypothyroidism. Take iodine-rich foods, see doctor.",
            "low": "Check for hyperthyroidism. Reduce iodine, consult doctor."
        },
        "LDL": {
            "high": "Avoid fried foods, eat oats, exercise regularly.",
            "low": "Low LDL is good but consult doctor if very low."
        },
        "HDL": {
            "low": "Increase exercise, eat healthy fats like nuts, olive oil."
        },
        "Bilirubin": {
            "high": "Could indicate jaundice. Drink fluids, consult doctor."
        },
        "Systolic BP": {
            "high": "Reduce salt, manage stress, walk daily.",
            "low": "Increase fluid intake, eat more salt if needed."
        },
        "Diastolic BP": {
            "high": "Exercise regularly, reduce caffeine and alcohol.",
            "low": "Stay hydrated, avoid alcohol, eat more salt."
        }
    }

    results = {}
    for param, (low, high) in ranges.items():
        pattern = rf"{param}[:\s]*([0-9]+\.?[0-9]*)"
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = float(match.group(1))
            status = "Normal"
            suggestion = "Maintain current habits."
            if value > high:
                status = "High"
                suggestion = suggestions.get(param, {}).get("high", "Consult doctor.")
            elif value < low:
                status = "Low"
                suggestion = suggestions.get(param, {}).get("low", "Consult doctor.")

            results[param] = {
                "value": value,
                "status": status,
                "suggestion": suggestion
            }
    return results