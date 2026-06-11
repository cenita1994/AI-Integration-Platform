import pickle


with open(
    "models/predictive/buy_computer_model.pkl",
    "rb"
) as file:

    buy_computer_model = pickle.load(
        file
    )
