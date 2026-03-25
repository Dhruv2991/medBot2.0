import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("dataset.csv")

X = data["symptoms"]
y = data["risk"]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec, y)

pickle.dump(model, open("common/triage_model.pkl", "wb"))
pickle.dump(vectorizer, open("common/vectorizer.pkl", "wb"))

print("ML Triage Model Trained Successfully")
