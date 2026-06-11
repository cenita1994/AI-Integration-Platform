from flask import (
    Blueprint,
    render_template
)


paradigms_bp = Blueprint(
    "paradigms",
    __name__
)


@paradigms_bp.route("/supervised-learning")
def supervised_learning():

    return render_template(
        "paradigms/supervised_learning.html"
    )


@paradigms_bp.route("/unsupervised-learning")
def unsupervised_learning():

    return render_template(
        "paradigms/unsupervised_learning.html"
    )


@paradigms_bp.route("/reinforcement-learning")
def reinforcement_learning():

    return render_template(
        "paradigms/reinforcement_learning.html"
    )
