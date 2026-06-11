from flask import (
    Blueprint,
    render_template
)


intelligent_systems_bp = Blueprint(
    "intelligent_systems",
    __name__
)


@intelligent_systems_bp.route("/artificial-intelligence")
def artificial_intelligence():

    return render_template(
        "intelligent_systems/ai.html"
    )


@intelligent_systems_bp.route("/machine-learning")
def machine_learning():

    return render_template(
        "intelligent_systems/ml.html"
    )


@intelligent_systems_bp.route("/deep-learning")
def deep_learning():

    return render_template(
        "intelligent_systems/dl.html"
    )
