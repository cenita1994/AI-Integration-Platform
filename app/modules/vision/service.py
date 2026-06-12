import numpy as np

from PIL import Image

from tensorflow.keras.applications.mobilenet_v2 import (
    preprocess_input
)


from .model_loader import (

    cnn_model,

    THRESHOLD

)


from .validator import (

    check_similarity

)


from app.ai.gemini import (

    ask_gemini

)


from app.ai.interpreter import (

    vision_interpreter

)


def classify_image(uploaded_file):

    # ===============================
    # IMAGE PREPROCESSING
    # ===============================

    img = Image.open(
        uploaded_file
    )

    img = img.convert(
        "RGB"
    )

    img = img.resize(
        (224, 224)
    )


    img_array = np.array(
        img
    )


    img_array = preprocess_input(
        img_array
    )


    img_array = np.expand_dims(
        img_array,
        axis=0
    )


    # ===============================
    # FEATURE SIMILARITY VALIDATION
    # ===============================

    similarity_score = check_similarity(
        img_array
    )


    similarity = (

        f"{similarity_score * 100:.2f}%"

    )


    # ===============================
    # UNKNOWN IMAGE DETECTION
    # ===============================

    if similarity_score < THRESHOLD:


        prediction = "Unknown Image"


        confidence = similarity


        explanation = vision_interpreter(

            prediction,

            confidence,

            similarity

        )


        return {

            "prediction": prediction,

            "confidence": confidence,

            "similarity": similarity,

            "explanation": explanation

        }


    # ===============================
    # CNN CLASSIFICATION
    # ===============================


    prediction_value = cnn_model.predict(

        img_array,

        verbose=0

    )[0][0]


    if prediction_value >= 0.5:


        prediction = "Dog"


        confidence_value = (

            prediction_value * 100

        )


    else:


        prediction = "Cat"


        confidence_value = (

            (1 - prediction_value)

            * 100

        )


    confidence = (

        f"{confidence_value:.2f}%"

    )


    prompt = f"""

You are a Computer Vision AI researcher.

Explain this CNN classification.

Prediction:
{prediction}

Confidence:
{confidence}

Similarity Score:
{similarity}

"""


    fallback = vision_interpreter(

        prediction,

        confidence,

        similarity

    )


    explanation = ask_gemini(

        prompt,

        fallback

    )


    return {

        "prediction": prediction,

        "confidence": confidence,

        "similarity": similarity,

        "explanation": explanation

    }