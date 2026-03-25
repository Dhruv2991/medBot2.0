def map_department(text):
    text = text.lower()

    if any(word in text for word in ["chest pain", "heart", "breathless"]):
        return "Cardiology"
    if any(word in text for word in ["fracture", "bone", "injury"]):
        return "Orthopedics"
    if any(word in text for word in ["fever", "cough", "cold"]):
        return "General Medicine"
    if any(word in text for word in ["stomach", "vomiting", "abdominal"]):
        return "Gastroenterology"

    return "General OPD"
