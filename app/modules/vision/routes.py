from flask import (

    Blueprint,

    render_template,

    request,

    jsonify

)


from .service import (

    classify_image

)


vision_bp = Blueprint(

    "vision",

    __name__

)


@vision_bp.route(
    "/image-classification"
)
def image_classification():

    return render_template(

        "applications/vision/image_classification.html"

    )


@vision_bp.route(

    "/analyze-image",

    methods=["POST"]

)
def analyze_image():

    uploaded_file = request.files[

        "image"

    ]

    result = classify_image(

        uploaded_file

    )

    return jsonify(

        result

    )
