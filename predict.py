import joblib

# Load trained model
model = joblib.load("model/chatbot_model.pkl")

# Load vectorizer
vectorizer = joblib.load("model/vectorizer.pkl")


def predict_intent(user_input):

    # Convert user text to lowercase
    user_input = user_input.lower()

    # Convert text into vector
    X = vectorizer.transform([user_input])

    # Predict intent
    prediction = model.predict(X)

    # Return first prediction
    return prediction[0]