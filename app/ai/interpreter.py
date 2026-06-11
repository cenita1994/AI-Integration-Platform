# ==================================================
# LOCAL HUMAN-LIKE AI INTERPRETER
# Researcher / Statistician Style
# ==================================================


def predictive_interpreter(
    prediction,
    data
):

    return f"""



Customer Profile Review:

The analyzed customer belongs to the {data["age"]} age category with a {data["income"]} income classification.

The system also considered student status ({data["student"]}) and credit rating ({data["credit_rating"]}) as part of the decision process.


</br></br>
Interpretation:

The Random Forest model evaluated the relationship among these variables by comparing them with patterns discovered from historical records.

Multiple decision trees contributed different analytical perspectives before producing the final classification.


</br></br>
Research Insight:

This result indicates that the customer's characteristics are statistically similar to previous observations associated with this outcome.

The prediction should be considered a decision-support analysis rather than an absolute conclusion.

"""


def nlp_interpreter(
    sentiment,
    original_text,
    translated_text
):

    return f"""




Original Statement:

"{original_text}"


Processed Statement:

"{translated_text}"


</br></br>
Interpretation:

The text was converted into numerical features using TF-IDF representation.

The machine learning model analyzed these patterns to determine the most likely emotional category.

</br></br>

Research Insight:

The result provides an analytical interpretation of the user's expressed opinion or emotional tendency.

Language context and human judgment should still be considered when interpreting sentiment.

"""


def vision_interpreter(
    prediction,
    confidence,
    similarity
):

    return f"""




Visual Analysis:

The model examined important image characteristics including shapes, textures, edges, and visual patterns learned during training.


</br></br>
Deep Learning Interpretation:

CNN models identify images by extracting hierarchical features from visual data and comparing these learned patterns with the uploaded image.


"""
