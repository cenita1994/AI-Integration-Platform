import numpy as np


from .model_loader import (

    feature_extractor,

    neighbor_model

)


def check_similarity(img_array):

    features = feature_extractor.predict(

        img_array,

        verbose=0

    )

    distances, indexes = (

        neighbor_model.kneighbors(

            features

        )

    )

    average_distance = np.mean(

        distances

    )

    similarity = (

        1 - average_distance

    )

    return similarity
