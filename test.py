from predict import predict_intent

while True:
    message = input("You: ")

    if message.lower() == "quit":
        break
    intent = predict_intent(message)

    print("intent:", intent)
    