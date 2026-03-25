import pickle
import numpy as np

model = pickle.load(open("common/triage_model.pkl", "rb"))
vectorizer = pickle.load(open("common/vectorizer.pkl", "rb"))

def ml_triage_predict_with_confidence(text):
    text_vec = vectorizer.transform([text])
    probabilities = model.predict_proba(text_vec)[0]
    classes = model.classes_

    max_index = np.argmax(probabilities)
    risk = classes[max_index]
    confidence = round(probabilities[max_index] * 100, 2)

    return risk, confidence
