# ==========================================
# PHASE 7.2
# RANDOM FOREST MODEL
# ==========================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def train_random_forest():

    print("\n========== RANDOM FOREST ==========")

    # Load dataset
    data = pd.read_csv("datasets/dataset.csv")

    print("Dataset Loaded Successfully!")
    print("Total Samples :", len(data))

    # Input features
    X = data[
        [
            "unique_count",
            "repetition_ratio",
            "sequentiality",
            "frequency_variance"
        ]
    ]

    # Output label
    y = data["best_policy"]

    # Split dataset:
    # 80% training
    # 20% testing
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    # Create Random Forest
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    print("\nTraining Random Forest...")

    # Train model
    model.fit(X_train, y_train)

    # Calculate accuracy
    accuracy = model.score(X_test, y_test)

    print("Training Completed!")
    print(f"Random Forest Accuracy : {accuracy * 100:.2f}%")

    # Save Random Forest
    joblib.dump(
        model,
        "models/random_forest.pkl"
    )

    print("Random Forest Saved Successfully!")

    return model, accuracy