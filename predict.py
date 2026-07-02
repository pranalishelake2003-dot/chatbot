import joblib


model = joblib.load("model/chatbot_model.pkl")

vectorizer = joblib.load("model/vectorizer.pkl")


def predict_intent(user_input):

    
    user_input = user_input.lower()

    
    X = vectorizer.transform([user_input])

    
    prediction = model.predict(X)

    
    return prediction[0]