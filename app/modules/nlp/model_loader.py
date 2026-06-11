import pickle


with open(
    "models/nlp/sentiment_model.pkl",
    "rb"
) as file:

    sentiment_model = pickle.load(
        file
    )


with open(
    "models/nlp/tfidf_vectorizer.pkl",
    "rb"
) as file:

    tfidf_vectorizer = pickle.load(
        file
    )
