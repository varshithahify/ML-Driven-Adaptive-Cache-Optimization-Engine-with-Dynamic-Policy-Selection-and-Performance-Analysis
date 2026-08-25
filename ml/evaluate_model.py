# ==========================================
# PHASE 8
# MODEL EVALUATION
# ==========================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


def evaluate_model():

    print("\n========================================")
    print(" MODEL EVALUATION")
    print("========================================")

    # ==========================================
    # LOAD DATASET
    # ==========================================

    data = pd.read_csv("datasets/dataset.csv")

    print("\nDataset Loaded Successfully!")
    print("Total Samples :", len(data))

    # ==========================================
    # INPUT FEATURES
    # ==========================================

    X = data[
        [
            "unique_count",
            "repetition_ratio",
            "sequentiality",
            "frequency_variance"
        ]
    ]

    # ==========================================
    # OUTPUT LABEL
    # ==========================================

    y = data["best_policy"]

    # ==========================================
    # SAME TRAIN / TEST SPLIT AS PHASE 7
    # ==========================================

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("Testing Samples :", len(X_test))

    # ==========================================
    # LOAD BEST MODEL
    # ==========================================

    model = joblib.load(
        "models/cache_model.pkl"
    )

    print("\nBest Model Loaded Successfully!")

    # ==========================================
    # MAKE PREDICTIONS
    # ==========================================

    predictions = model.predict(X_test)

    # ==========================================
    # ACCURACY
    # ==========================================

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("\n========================================")
    print(" ACCURACY")
    print("========================================")

    print(
        f"Model Accuracy : {accuracy * 100:.2f}%"
    )

    # ==========================================
    # CLASSIFICATION REPORT
    # ==========================================

    print("\n========================================")
    print(" CLASSIFICATION REPORT")
    print("========================================")

    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )

    # ==========================================
    # CONFUSION MATRIX
    # ==========================================

    labels = sorted(y.unique())

    matrix = confusion_matrix(
        y_test,
        predictions,
        labels=labels
    )

    print("========================================")
    print(" CONFUSION MATRIX")
    print("========================================")

    print("\nLabels Order:")
    print(labels)

    print("\nConfusion Matrix:")
    print(matrix)

    print("\n========================================")
    print(" MODEL EVALUATION COMPLETED")
    print("========================================")

    return accuracy