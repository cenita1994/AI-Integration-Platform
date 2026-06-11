import os
import pickle

from tensorflow.keras.models import load_model

from tensorflow.keras.applications import MobileNetV2

from sklearn.neighbors import NearestNeighbors


# ===============================
# PATH CONFIGURATION
# ===============================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "../../../models/vision/cat_dog_mobilenet_model_v3.keras"
)


PROFILE_PATH = os.path.join(
    BASE_DIR,
    "../../../models/vision/cat_dog_similarity_profile_v4.pkl"
)


# ===============================
# LOAD CNN MODEL
# ===============================

cnn_model = load_model(
    MODEL_PATH,
    compile=False
)


# ===============================
# FEATURE EXTRACTOR
# ===============================

feature_extractor = MobileNetV2(

    weights="imagenet",

    include_top=False,

    pooling="avg",

    input_shape=(224, 224, 3)

)


# ===============================
# LOAD SIMILARITY PROFILE
# ===============================


with open(
    PROFILE_PATH,
    "rb"
) as file:

    similarity_profile = pickle.load(file)


THRESHOLD = similarity_profile[
    "threshold"
]


neighbor_model = NearestNeighbors(

    n_neighbors=similarity_profile["n_neighbors"],

    metric=similarity_profile["metric"]

)


neighbor_model.fit(

    similarity_profile["features"]

)


print("====================")

print("Vision Loaded")

print("Model:", MODEL_PATH)

print("Threshold:", THRESHOLD)

print("====================")
