import json
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = []
classes = []
documents = []

with open("data/intents.json") as file:
    intents = json.load(file)

for intent in intents["intents"]:
    for pattern in intent["patterns"]:

        # SAFE TOKENIZATION
        word_list = pattern.lower().split()

        words.extend(word_list)
        documents.append((word_list, intent["tag"]))

        if intent["tag"] not in classes:
            classes.append(intent["tag"])

words = [lemmatizer.lemmatize(w) for w in words if w.isalnum()]
words = sorted(set(words))
classes = sorted(set(classes))

print("\nWORDS:", words)
print("\nCLASSES:", classes)
print("\nDOCUMENTS:", documents[:3])