# ==========================================
# PHASE 7.2
# RANDOM FOREST MODEL TRAINING
# ==========================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def train_random_forest():

    print("\n========================================")
    print(" PHASE 7.2 - RANDOM FOREST")
    print("========================================")

    # Load dataset
    data = pd.read_csv(
        "datasets/dataset.csv"
    )

    print("Dataset Loaded Successfully!")
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
    # TARGET
    # ==========================================

    y = data["best_policy"]


    # ==========================================
    # TRAIN / TEST SPLIT
    # ==========================================

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("Training Samples :", len(X_train))
    print("Testing Samples  :", len(X_test))


    # ==========================================
    # CREATE MODEL
    # ==========================================

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )


    # ==========================================
    # TRAIN
    # ==========================================

    print("\nTraining Random Forest...")

    model.fit(
        X_train,
        y_train
    )


    # ==========================================
    # EVALUATE
    # ==========================================

    accuracy = model.score(
        X_test,
        y_test
    )

    print("Training Completed!")

    print(
        f"Random Forest Accuracy : "
        f"{accuracy * 100:.2f}%"
    )


    # ==========================================
    # SAVE MODEL
    # ==========================================

    joblib.dump(
        model,
        "models/random_forest.pkl"
    )

    print(
        "Random Forest Saved Successfully!"
    )

    return model, accuracy


if __name__ == "__main__":
    train_random_forest()