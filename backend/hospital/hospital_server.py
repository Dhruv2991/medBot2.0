from flask import Flask, request, jsonify
from flask_cors import CORS
from common.ml_triage import ml_triage_predict_with_confidence
from hospital.department_mapper import map_department

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/hospital/checkin", methods=["POST"])
def hospital_checkin():
    data = request.json

    name = data.get("name")
    age = data.get("age")
    symptoms = data.get("symptoms")

    risk, confidence = ml_triage_predict_with_confidence(symptoms)
    department = map_department(symptoms)

    if risk == "HIGH":
        priority = "P1 – Immediate"
    elif risk == "MEDIUM":
        priority = "P2 – Urgent"
    else:
        priority = "P3 – Routine"

    return jsonify({
        "patient_name": name,
        "age": age,
        "risk": risk,
        "confidence": confidence,
        "priority": priority,
        "department": department,
        "instruction": "Please proceed to the assigned department counter."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)
