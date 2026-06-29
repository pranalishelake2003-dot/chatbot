from flask import Flask, render_template, request, jsonify

from predict import predict_intent
from chatbot import get_response
from save_chat import save_chat

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")



@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data["message"]

    intent = predict_intent(user_message)

    response = get_response(intent)

    save_chat(user_message, response, intent)

    return jsonify({
        "response": response
    })



if __name__ == "__main__":

   import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)