# 🏥 MedBot 2.0 — AI-Powered Healthcare Assistant

MedBot 2.0 is an intelligent healthcare assistant designed to provide **real-time medical triage, hospital department recommendations, and first-aid guidance** using machine learning and rule-based systems.

---

## 🎯 Problem Statement

In emergency or uncertain medical situations, users often:

* Don’t know which department to visit
* Lack immediate first-aid knowledge
* Delay critical decisions

MedBot aims to **bridge this gap using AI-driven insights**.

---

## 🚀 Key Features

### 🧠 1. ML-Based Triage System

* Predicts severity based on symptoms
* Suggests urgency level (low / medium / critical)
* Uses trained model (`triage_model.pkl`)

### 🏥 2. Hospital Department Recommendation

* Maps symptoms → appropriate department
* Example:

  * Chest pain → Cardiology
  * Fever → General Medicine

### 🚑 3. First Aid Guidance System

* Provides immediate first-aid suggestions
* Helps users before reaching hospital

### 🌐 4. REST API Backend

* Flask-based backend
* Modular structure:

  * `hospital/` → ML + routing
  * `public/` → first-aid APIs

### 💻 5. Simple Frontend UI

* Built using HTML, CSS, JS
* Connects to backend APIs

---

## 🛠 Tech Stack

| Layer    | Technology            |
| -------- | --------------------- |
| Backend  | Python, Flask         |
| ML       | Scikit-learn          |
| Frontend | HTML, CSS, JavaScript |
| Data     | CSV dataset           |
| Model    | Pickle (`.pkl`)       |

---

## 📁 Project Structure

```bash
medbot-2.0/
│
├── backend/
│   ├── common/              # ML model + utilities
│   ├── hospital/            # Hospital triage server
│   ├── public/              # First-aid server
│   ├── train_model.py       # Model training
│   ├── dataset.csv
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
```

---

## ⚙️ Setup & Installation

### 🔹 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/medbot-2.0.git
cd medbot-2.0/backend
```

---

### 🔹 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 🔹 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 🧠 Run Hospital Backend

```bash
python -m hospital.hospital_server
```

Runs at:

```
http://127.0.0.1:6000
```

---

### 🚑 Run First-Aid Backend

```bash
python -m public.server
```

---

### 🌐 Run Frontend

Simply open:

```
frontend/index.html
```

---

## 🔌 API Endpoints (Example)

| Endpoint      | Method | Description                 |
| ------------- | ------ | --------------------------- |
| `/triage`     | POST   | Predict severity            |
| `/department` | POST   | Suggest hospital department |
| `/firstaid`   | POST   | First-aid suggestions       |

---

## 🧪 Example Use Case

1. User enters symptoms
2. System predicts severity
3. Suggests department
4. Provides first-aid guidance

---

## 📈 Future Improvements

* 🔊 Voice-based interaction
* 📱 Mobile app (Android/iOS)
* 🌍 Live hospital integration
* 🤖 LLM-powered medical chatbot
* 🗺️ Navigation to nearest hospital

---

## 👨‍💻 Author

**Dhruv G Nayak**
AI/ML Engineering Student

---

## ⭐ Contribution

Feel free to fork, improve, and contribute!

---

## 📜 License

This project is for educational and research purposes.
