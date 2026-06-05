# ====================================
# IMPORT LIBRARIES
# ====================================

from flask import Flask, render_template, request, jsonify

import pickle

import pandas as pd

import os

from dotenv import load_dotenv

import google.generativeai as genai

from deep_translator import GoogleTranslator

# ====================================
# COMPUTER VISION LIBRARIES
# ====================================

from tensorflow.keras.models import load_model

from tensorflow.keras.preprocessing import image

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

from PIL import Image

import numpy as np

# ====================================
# CREATE FLASK APPLICATION
# ====================================

app = Flask(__name__)


# ====================================
# LOAD PREDICTIVE ANALYTICS MODEL
# ====================================

with open(
    "models/predictive/buy_computer_model.pkl",
    "rb"
) as file:

    model = pickle.load(file)


# ====================================
# LOAD NLP SENTIMENT ANALYSIS MODEL
# ====================================

with open(
    "models/nlp/sentiment_model.pkl",
    "rb"
) as file:

    sentiment_model = pickle.load(file)



with open(
    "models/nlp/tfidf_vectorizer.pkl",
    "rb"
) as file:

    tfidf_vectorizer = pickle.load(file)


# ====================================
# LOAD COMPUTER VISION MODEL
# ====================================

cnn_model = load_model(
    "models/vision/cat_dog_mobilenet_model.h5"
)

# ====================================
# CONFIGURE GEMINI AI
# ====================================

load_dotenv()



genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


gemini_model = genai.GenerativeModel(

    "gemini-2.0-flash"

)


# ====================================
# DASHBOARD ROUTE
# ====================================

@app.route("/")
def dashboard():

    return render_template("dashboard.html")


# ====================================
# INTELLIGENT SYSTEMS ROUTES
# ====================================

@app.route("/artificial-intelligence")
def artificial_intelligence():

    return render_template(
        "intelligent_systems/ai.html"
    )


@app.route("/machine-learning")
def machine_learning():

    return render_template(
        "intelligent_systems/ml.html"
    )


@app.route("/deep-learning")
def deep_learning():

    return render_template(
        "intelligent_systems/dl.html"
    )


# ====================================
# LEARNING PARADIGMS ROUTES
# ====================================

@app.route("/supervised-learning")
def supervised_learning():

    return render_template(
        "paradigms/supervised_learning.html"
    )


@app.route("/unsupervised-learning")
def unsupervised_learning():

    return render_template(
        "paradigms/unsupervised_learning.html"
    )


@app.route("/reinforcement-learning")
def reinforcement_learning():

    return render_template(
        "paradigms/reinforcement_learning.html"
    )


# ====================================
# KDD ROUTE
# ====================================

@app.route("/kdd")
def kdd():

    return render_template(
        "kdd/kdd.html"
    )


# ====================================
# PREDICTIVE ANALYTICS ROUTES
# ====================================

@app.route("/predictive-documentation")
def predictive_documentation():

    return render_template(
        "applications/predictive/documentation.html"
    )

@app.route("/buy-computer-prediction")
def buy_computer_prediction():

    return render_template(
        "applications/predictive/buy_computer.html"
    )
    

# ====================================
# NLP APPLICATION ROUTES
# ====================================

@app.route("/nlp-documentation")
def nlp_documentation():


    return render_template(
        "applications/nlp/documentation.html"
    )
# ====================================
# RANDOM FOREST PREDICTION API
# ====================================


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    # Receive data from frontend

    age = data["age"]

    income = data["income"]

    student = data["student"]

    credit = data["credit_rating"]

    # Convert categorical values

    age_map = {

        "<=30": 0,

        "31...40": 1,

        ">40": 2

    }

    income_map = {

        "High": 0,

        "Low": 1,

        "Medium": 2

    }

    student_map = {

        "No": 0,

        "Yes": 1

    }

    credit_map = {

        "Excellent": 0,

        "Fair": 1

    }

    input_data = pd.DataFrame(

        [[

            15,

            age_map[age],

            income_map[income],

            student_map[student],

            credit_map[credit]

        ]],


        columns=[

            "Record",

            "Age",

            "Income",

            "Student",

            "Credit_Rating"

        ]

    )

    # Random Forest Prediction

    result = model.predict(input_data)

    if result[0] == 1:

        prediction = "Will Buy Computer"

    else:

        prediction = "Will Not Buy Computer"

    # ====================================
    # GEMINI AI INTERPRETATION
    # ====================================


    prompt = f"""

    You are an expert Machine Learning researcher and Data Analyst.

    A Random Forest classification model was used to predict customer purchasing behavior.

    Analyze the prediction result using a professional data analytics interpretation.


    Customer Profile:

    Age Group:
    {data['age']}

    Income Level:
    {data['income']}

    Student Status:
    {data['student']}

    Credit Rating:
    {data['credit_rating']}


    Machine Learning Prediction:

    {prediction}



    Provide a comprehensive explanation containing:


    1. Prediction Summary

    Explain what the prediction means.


    2. Customer Profile Analysis

    Analyze how each customer attribute may influence the result:

    - Age
    - Income
    - Student Status
    - Credit Rating


    3. Machine Learning Interpretation

    Explain how a Random Forest model uses learned patterns from historical customer data to produce this prediction.


    4. Decision Support Insight

    Explain how this result can help businesses understand customer behavior.


    5. Important Note

    Mention that machine learning predictions are decision-support tools and should be combined with real-world business judgment.


    Use a professional research and data analytics tone.

    """
    try:

        response = gemini_model.generate_content(prompt)

        explanation = response.text

    except Exception:


        explanation = f"""

    Prediction Summary:

    The Random Forest Machine Learning model classified this customer as:

    {prediction}


    Customer Profile Analysis:

    The prediction was generated by analyzing multiple customer characteristics including age group, income level, student status, and credit rating.


    Age Group:
    {data['age']}

    The customer's age category was evaluated because purchasing behavior may differ across different age groups.


    Income Level:
    {data['income']}

    Income information helps the model understand possible purchasing capability and customer behavior patterns.


    Student Status:
    {data['student']}

    Student classification is considered because technology needs and computer purchasing decisions may vary depending on educational involvement.


    Credit Rating:
    {data['credit_rating']}

    Credit rating provides additional information related to customer reliability and purchasing characteristics.



    Machine Learning Interpretation:

    Random Forest is an ensemble learning algorithm that combines multiple decision trees.

    Each decision tree analyzes the customer's information and contributes to the final prediction.

    The model identifies patterns learned from previous customer records and applies those patterns to new customer information.



    Decision Support Insight:

    The prediction result can help organizations identify potential customers and support data-driven decision-making.



    Important Note:

    This prediction does not guarantee actual customer behavior. It serves as an intelligent recommendation that should be combined with business knowledge and additional customer information.

    """
    return jsonify({

        "prediction": prediction,

        "explanation": explanation

    })

# ====================================
# NLP ROUTES
# ====================================

@app.route("/sentiment-analysis")
def sentiment_analysis():


    return render_template(
        "applications/nlp/sentiment_analysis.html"
    )

# ====================================
# COMPUTER VISION ROUTES
# ====================================

@app.route("/image-classification")
def image_classification():


    return render_template(
        "applications/vision/image_classification.html"
    )
@app.route("/image-classification-documentation")
def image_classification_documentation():

    return render_template(
        "applications/vision/documentation.html"
    )

# ====================================
# COMPUTER VISION IMAGE PREDICTION API
# ====================================

@app.route("/analyze-image", methods=["POST"])
def analyze_image():


    uploaded_file = request.files["image"]




    # Load uploaded image

    img = Image.open(uploaded_file)



    # Convert image to RGB

    img = img.convert(

        "RGB"

    )



    # Resize based on MobileNetV2 input size

    img = img.resize(

        (224,224)

    )




    # Convert image to array

    img_array = np.array(

        img

    )




    # Apply MobileNetV2 preprocessing

    img_array = preprocess_input(

        img_array

    )




    # Add batch dimension

    img_array = np.expand_dims(

        img_array,

        axis=0

    )


    # CNN Prediction

    prediction_value = cnn_model.predict(img_array)[0][0]




    if prediction_value >= 0.5:


        prediction = "Dog"

        confidence = prediction_value * 100



    else:


        prediction = "Cat"

        confidence = (1 - prediction_value) * 100






    # Gemini Explanation


    prompt = f"""

    A Convolutional Neural Network (CNN) image classification model analyzed an uploaded image.

    Prediction Result:
    {prediction}

    Confidence Score:
    {confidence:.2f}%

    Explain this result in a simple but professional way.

    Describe that the CNN model analyzed visual patterns such as shapes,
    textures, and image features learned from training examples.

    Do not mention uncertainty unless necessary.

    """



    try:


        response = gemini_model.generate_content(prompt)


        explanation = response.text



    except Exception:


        explanation = f"""

        The uploaded image was classified as {prediction}.

        The CNN model analyzed visual characteristics of the image,
        including shapes, patterns, and extracted features.

        Based on the learned patterns from previous cat and dog images,
        the system determined that the image belongs to the {prediction}
        category.

        """





    return jsonify({


        "prediction": prediction,


        "confidence": f"{confidence:.2f}%",


        "explanation": explanation


    })

# ====================================
# SENTIMENT ANALYSIS API
# ====================================

@app.route("/analyze-sentiment", methods=["POST"])
def analyze_sentiment():


    data = request.json


    tweet = data["tweet"]


    # ====================================
    # TRANSLATE INPUT TEXT TO ENGLISH
    # ====================================

    try:


        english_text = GoogleTranslator(
            source="auto",
            target="en"
        ).translate(tweet)



    except Exception as e:


        print(
            "TRANSLATION ERROR:",
            e
        )


        english_text = tweet


    # Convert text using TF-IDF



    tweet_vector = tfidf_vectorizer.transform(
        [english_text]
    )


    # Predict sentiment

    result = sentiment_model.predict(
        tweet_vector
    )



    sentiment = result[0]





    # ====================================
    # GEMINI SENTIMENT EXPLANATION
    # ====================================

    prompt = f"""

    You are an expert Natural Language Processing researcher and Data Analyst.


    A machine learning sentiment classification model analyzed the following text.


    Original User Input:

    "{tweet}"


    Translated English Text Used for Prediction:

    "{english_text}"


    Machine Learning Prediction Result:

    {sentiment}



    Provide a comprehensive sentiment analysis explanation containing:


    1. Sentiment Summary

    Explain what the {sentiment} classification means.


    2. Text Interpretation

    Analyze the words, phrases, and expressions that influenced the sentiment.


    3. Emotional Context

    Explain the possible emotion or intention expressed by the user.


    4. NLP Process Explanation

    Explain that the text was translated into English, converted into numerical features using TF-IDF, and classified using a trained machine learning model.


    5. Decision Support Insight

    Explain how this sentiment information can help understand user opinions or feedback.


    Use a professional research and data analytics tone.

    """


    try:


        response = gemini_model.generate_content(prompt)


        explanation = response.text



    except Exception as e:
        

        print(
            "EXPLANATION ERROR:",
            e
        )

        explanation = f"""

        The statement was classified as {sentiment} because of the emotion and meaning expressed in the message.

        The phrase:

        "{english_text}"

        shows language patterns that indicate a {sentiment} feeling or opinion.

        The message reflects the possible attitude, reaction, or emotion of the person who wrote the statement.

        """


    return jsonify({

        "original_text": tweet,

        "translated_text": english_text,

        "sentiment": sentiment,

        "explanation": explanation

    })
    
# ====================================
# RUN APPLICATION
# ====================================
if __name__ == "__main__":

    app.run(debug=True)
