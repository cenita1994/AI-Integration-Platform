from flask import (
    Blueprint,
    render_template
)


documentation_bp = Blueprint(
    "documentation",
    __name__
)


@documentation_bp.route(
    "/predictive-documentation"
)
def predictive_documentation():

    return render_template(
        "applications/predictive/documentation.html"
    )


@documentation_bp.route(
    "/nlp-documentation"
)
def nlp_documentation():

    return render_template(
        "applications/nlp/documentation.html"
    )


@documentation_bp.route(
    "/image-classification-documentation"
)
def image_classification_documentation():

    return render_template(
        "applications/vision/documentation.html"
    )
