# ==========================================
# PHASE 7.1
# DECISION TREE MODEL
# ==========================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def train_decision_tree():

    print("\n========== DECISION TREE ==========")

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

    # Create Decision Tree
    model = DecisionTreeClassifier(
        random_state=42
    )

    print("\nTraining Decision Tree...")

    # Train model
    model.fit(X_train, y_train)

    # Calculate accuracy
    accuracy = model.score(X_test, y_test)

    print("Training Completed!")
    print(f"Decision Tree Accuracy : {accuracy * 100:.2f}%")

    # Save Decision Tree
    joblib.dump(
        model,
        "models/decision_tree.pkl"
    )

    print("Decision Tree Saved Successfully!")

    return model, accuracy