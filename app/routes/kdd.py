from flask import (
    Blueprint,
    render_template
)


kdd_bp = Blueprint(
    "kdd",
    __name__
)


@kdd_bp.route("/kdd")
def kdd():

    return render_template(
        "kdd/kdd.html"
    )
