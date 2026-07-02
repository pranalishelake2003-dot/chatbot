import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read API Key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


def get_response(user_message):
    try:
        response = model.generate_content(user_message)
        return response.text
    except Exception as e:
        return f"Error: {e}"