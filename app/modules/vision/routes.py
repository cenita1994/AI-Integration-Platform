from flask import (
    Blueprint,
    render_template,
    request,
    jsonify
)

import traceback

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

    try:
        print("IMAGE ANALYZE ROUTE REACHED", flush=True)

        if "image" not in request.files:
            print("ERROR: No image key found", flush=True)

            return jsonify({
                "error": "No image uploaded."
            }), 400

        uploaded_file = request.files[
            "image"
        ]

        if uploaded_file.filename == "":
            print("ERROR: Empty filename", flush=True)

            return jsonify({
                "error": "No selected image."
            }), 400

        result = classify_image(
            uploaded_file
        )

        print("IMAGE ANALYSIS SUCCESS", flush=True)

        return jsonify(
            result
        )

    except Exception as error:
        print("IMAGE ANALYSIS ERROR:", flush=True)
        print(error, flush=True)
        traceback.print_exc()

        return jsonify({
            "error": str(error),
            "prediction": "Error",
            "confidence": "0%",
            "similarity": "Disabled in online deployment",
            "explanation": "Unable to process image classification because an internal server error occurred."
        }), 500