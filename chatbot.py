import json
import random
import sqlite3

from predict import predict_intent


# -----------------------------
# Load Intents
# -----------------------------
with open("data/intents.json", "r") as file:
    intents = json.load(file)


# -----------------------------
# Save Chat
# -----------------------------
def save_chat(user_message, bot_response, intent):

    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        bot_response TEXT,
        intent TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO chats(user_message, bot_response, intent)
    VALUES(?,?,?)
    """, (user_message, bot_response, intent))

    conn.commit()
    conn.close()


# -----------------------------
# Get Response
# -----------------------------
def get_response(intent):

    for item in intents["intents"]:

        if item["tag"] == intent:
            return random.choice(item["responses"])

    return "Sorry! I don't understand."


# -----------------------------
# Terminal Chatbot
# -----------------------------
def main():

    print("🤖 AI Chatbot Started")
    print("Type 'quit' to exit.\n")

    while True:

        user_message = input("You: ")

        if user_message.lower() == "quit":
            print("Bot: Goodbye 👋")
            break

        intent = predict_intent(user_message)

        response = get_response(intent)

        print("Bot:", response)

        save_chat(user_message, response, intent)


if __name__ == "__main__":
    main()