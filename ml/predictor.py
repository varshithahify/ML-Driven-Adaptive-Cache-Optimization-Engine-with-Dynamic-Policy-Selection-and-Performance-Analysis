# ==========================================
# PHASE 9
# AI CACHE POLICY PREDICTOR
# ==========================================

import joblib
import pandas as pd

from ml.features import extract_features


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

model = joblib.load("models/cache_model.pkl")


def predict_policy(requests):

    # ==========================================
    # EXTRACT FEATURES FROM NEW WORKLOAD
    # ==========================================

    features = extract_features(requests)

    # ==========================================
    # PREPARE FEATURES FOR ML MODEL
    # ==========================================

    input_data = pd.DataFrame(
        [[
            features["unique_count"],
            features["repetition_ratio"],
            features["sequentiality"],
            features["frequency_variance"]
        ]],
        columns=[
            "unique_count",
            "repetition_ratio",
            "sequentiality",
            "frequency_variance"
        ]
    )

    # ==========================================
    # PREDICT BEST CACHE POLICY
    # ==========================================

    prediction = model.predict(input_data)

    # model.predict returns an array.
    # We need the first prediction.
    predicted_policy = prediction[0]

    return predicted_policy, features