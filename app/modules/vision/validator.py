# ===============================
# IMAGE SIMILARITY VALIDATOR
# MobileNetV2 Feature Validation
# ===============================


from .model_loader import (

    similarity_extractor,

    neighbor_model

)


# ===============================
# CHECK IMAGE SIMILARITY
# ===============================


def check_similarity(

    img_array

):

    # ===============================
    # EXTRACT IMAGE FEATURES
    # MobileNetV2 OUTPUT = 1280
    # ===============================


    image_features = similarity_extractor.predict(

        img_array,

        verbose=0

    )


    print(

        "Extracted Feature Shape:",

        image_features.shape

    )


    # ===============================
    # NEAREST NEIGHBOR COMPARISON
    # ===============================


    distances, indexes = neighbor_model.kneighbors(

        image_features

    )


    # ===============================
    # CONVERT DISTANCE TO SIMILARITY
    # ===============================


    similarity_score = (

        1 - distances.mean()

    )


    return similarity_score