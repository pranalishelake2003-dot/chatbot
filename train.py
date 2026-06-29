import json
import joblib

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open("data/intents.json", "r") as file:
    intents = json.load(file)

texts = []
labels = []

# Prepare training data
for intent in intents["intents"]:

    for pattern in intent["patterns"]:

        texts.append(pattern.lower())
        labels.append(intent["tag"])

print("Texts:", texts)
print("Labels:", labels)

# Convert text into vectors
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)

print("Vocabulary:", vectorizer.get_feature_names_out())
print("Vector Shape:", X.shape)

# Train Model
model = LogisticRegression(max_iter=1000)

model.fit(X, labels)

print("Training Prediction:", model.predict(X))

# Save Model
joblib.dump(model, "model/chatbot_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("✅ Model Trained Successfully")