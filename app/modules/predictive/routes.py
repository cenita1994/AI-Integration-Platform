from flask import (

    Blueprint,

    render_template,

    request,

    jsonify

)


from .service import (

    predict_buy_computer

)


predictive_bp = Blueprint(

    "predictive",

    __name__

)


# ===============================
# PAGE
# ===============================


@predictive_bp.route(
    "/buy-computer-prediction"
)
def buy_computer_prediction():

    return render_template(

        "applications/predictive/buy_computer.html"

    )


# ===============================
# API
# ===============================


@predictive_bp.route(

    "/predict",

    methods=["POST"]

)
def predict():

    data = request.json

    result = predict_buy_computer(

        data

    )

    return jsonify(

        result

    )
