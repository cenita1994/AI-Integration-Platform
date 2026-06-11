import os

from dotenv import load_dotenv

from google import genai


# ===============================
# LOAD ENV VARIABLES
# ===============================

load_dotenv()


# ===============================
# AI RESPONSE HANDLER
# ===============================

def ask_gemini(
    prompt,
    fallback
):
    api_key = os.getenv(
        "GEMINI_API_KEY"
    )

    if not api_key:
        print(
            "Gemini API key missing, using local interpreter"
        )

        return fallback

    try:
        client = genai.Client(
            api_key=api_key
        )

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        if response.text:
            return response.text

        return fallback

    except Exception as error:
        print(
            "Gemini unavailable, using local interpreter"
        )

        print(
            error
        )

        return fallback
