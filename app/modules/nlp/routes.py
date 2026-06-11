from flask import (

    Blueprint,

    render_template,

    request,

    jsonify

)


from .service import (

    analyze_text_sentiment

)


nlp_bp = Blueprint(

    "nlp",

    __name__

)


# ===============================
# PAGE ROUTE
# ===============================


@nlp_bp.route(
    "/sentiment-analysis"
)
def sentiment_analysis():

    return render_template(

        "applications/nlp/sentiment_analysis.html"

    )


# ===============================
# API ROUTE
# ===============================


@nlp_bp.route(

    "/analyze-sentiment",

    methods=["POST"]

)
def analyze_sentiment():

    data = request.json

    result = analyze_text_sentiment(

        data["tweet"]

    )

    return jsonify(

        result

    )
