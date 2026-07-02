import google.generativeai as genai
import os

# Gemini API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")


def get_response(user_message):

    try:
        response = model.generate_content(user_message)
        return response.text

    except Exception as e:
        return f"Error: {e}"