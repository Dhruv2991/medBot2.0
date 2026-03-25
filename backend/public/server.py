from flask import Flask, request, jsonify
from flask_cors import CORS
from common.ml_triage import ml_triage_predict_with_confidence
from public.aid_matcher import get_first_aid

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.json.get("message")

    if not user_text:
        return jsonify({"response": "Please describe your symptoms."})

    risk, confidence = ml_triage_predict_with_confidence(user_text)
    first_aid = get_first_aid(user_text)

    if risk == "HIGH":
        response = (
            "⚠️ This may be a medical emergency.\n"
            "Please seek immediate medical attention or contact emergency services."
        )
        emergency = True

    elif risk == "MEDIUM":
        response = "Your symptoms may require medical attention. Please consult a doctor."
        emergency = False

    else:
        response = "Your condition appears mild."
        emergency = False

    if first_aid:
        response += "\n\nFirst Aid Advice:\n" + first_aid
    elif risk != "HIGH":
        response += (
            "\n\nI do not have specific first-aid guidance for this issue. "
            "Please consult a healthcare professional."
        )

    return jsonify({
        "risk": risk,
        "confidence": confidence,
        "emergency": emergency,
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
