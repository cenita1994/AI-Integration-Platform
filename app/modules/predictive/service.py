import pandas as pd


from .model_loader import (

    buy_computer_model

)


from app.ai.gemini import (

    ask_gemini

)


from app.ai.interpreter import (

    predictive_interpreter

)


def predict_buy_computer(data):

    # ===============================
    # ENCODING
    # ===============================

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

    # ===============================
    # PREPARE DATA
    # ===============================

    input_data = pd.DataFrame(


        [[

            15,


            age_map[

                data["age"]

            ],


            income_map[

                data["income"]

            ],


            student_map[

                data["student"]

            ],


            credit_map[

                data["credit_rating"]

            ]

        ]],



        columns=[

            "Record",

            "Age",

            "Income",

            "Student",

            "Credit_Rating"

        ]

    )

    # ===============================
    # RANDOM FOREST
    # ===============================

    result = buy_computer_model.predict(

        input_data

    )

    if result[0] == 1:

        prediction = (

            "Will Buy Computer"

        )

    else:

        prediction = (

            "Will Not Buy Computer"

        )

    # ===============================
    # GEMINI PROMPT
    # ===============================

    prompt = f"""

You are a professional statistician, machine learning researcher, and data analyst.


Interpret the Random Forest classification result.


Customer Information:

Age Group:
{data["age"]}


Income Level:
{data["income"]}


Student Status:
{data["student"]}


Credit Rating:
{data["credit_rating"]}



Prediction Result:

{prediction}



Explain the result like a human researcher:

- why the model may have produced this result
- possible relationship between variables
- statistical interpretation
- decision-support recommendation


Avoid sounding like a robot.

"""

    # ===============================
    # LOCAL HUMAN-LIKE FALLBACK
    # ===============================

    fallback = predictive_interpreter(

        prediction,

        data

    )

    # ===============================
    # FINAL EXPLANATION
    # ===============================

    explanation = ask_gemini(


        prompt,


        fallback


    )

    return {


        "prediction":

        prediction,



        "explanation":

        explanation

    }
