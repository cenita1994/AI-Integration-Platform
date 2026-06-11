import os


from dotenv import load_dotenv


import google.generativeai as genai


# ===============================
# LOAD ENV VARIABLES
# ===============================


load_dotenv()


# ===============================
# GEMINI CONFIGURATION
# ===============================


genai.configure(


    api_key=os.getenv(

        "GEMINI_API_KEY"

    )

)


# ===============================
# GEMINI MODEL
# ===============================


model = genai.GenerativeModel(

    "gemini-2.0-flash"

)


# ===============================
# AI RESPONSE HANDLER
# ===============================


def ask_gemini(

    prompt,

    fallback

):

    try:

        response = model.generate_content(

            prompt

        )

        return response.text

    except Exception as error:

        print(

            "Gemini unavailable, using local interpreter"

        )

        print(

            error

        )

        return fallback
