import os

from tensorflow.keras.models import load_model


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


# ===============================
# LOAD CNN MODEL ONLY
# ===============================

cnn_model = load_model(
    MODEL_PATH,
    compile=False
)


print("====================")
print("Vision Loaded")
print("Model:", MODEL_PATH)
print("Similarity Validation: Disabled for Render")
print("====================")
