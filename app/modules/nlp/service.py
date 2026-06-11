from deep_translator import (

    GoogleTranslator

)


from .model_loader import (

    sentiment_model,

    tfidf_vectorizer

)


from app.ai.gemini import (

    ask_gemini

)


from app.ai.interpreter import (

    nlp_interpreter

)


def analyze_text_sentiment(tweet):

    # ===============================
    # TRANSLATION
    # ===============================

    try:

        english_text = GoogleTranslator(

            source="auto",

            target="en"

        ).translate(

            tweet

        )

    except Exception:

        english_text = tweet

    # ===============================
    # TF-IDF
    # ===============================

    text_vector = (

        tfidf_vectorizer.transform(

            [

                english_text

            ]

        )

    )

    # ===============================
    # ML SENTIMENT MODEL
    # ===============================

    result = sentiment_model.predict(

        text_vector

    )

    sentiment = result[0]

    # ===============================
    # GEMINI PROMPT
    # ===============================

    prompt = f"""

You are a Natural Language Processing researcher, linguist, and data analyst.


Interpret this sentiment analysis result professionally.


Original User Text:

"{tweet}"


Processed English Text:

"{english_text}"



Machine Learning Sentiment Result:

{sentiment}




Explain like a human expert:

- What the detected sentiment means
- Possible emotional intention of the message
- Important language patterns
- How NLP and machine learning analyzed the text
- Practical interpretation of the result


Use a professional researcher tone.

"""

    # ===============================
    # LOCAL HUMAN-LIKE FALLBACK
    # ===============================

    fallback = nlp_interpreter(


        sentiment,


        tweet,


        english_text

    )

    # ===============================
    # FINAL EXPLANATION
    # ===============================

    explanation = ask_gemini(


        prompt,


        fallback

    )

    return {


        "original_text":

        tweet,



        "translated_text":

        english_text,



        "sentiment":

        sentiment,



        "explanation":

        explanation

    }
