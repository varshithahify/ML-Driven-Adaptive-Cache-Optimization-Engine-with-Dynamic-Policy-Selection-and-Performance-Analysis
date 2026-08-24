# ==========================================
# PHASE 7.1
# DECISION TREE MODEL TRAINING
# ==========================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def train_decision_tree():

    print("\n========================================")
    print(" PHASE 7.1 - DECISION TREE")
    print("========================================")

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

    # Target
    y = data["best_policy"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("Training Samples :", len(X_train))
    print("Testing Samples  :", len(X_test))

    # Create model
    model = DecisionTreeClassifier(
        random_state=42
    )

    print("\nTraining Decision Tree...")

    # Train
    model.fit(X_train, y_train)

    # Accuracy
    accuracy = model.score(
        X_test,
        y_test
    )

    print("Training Completed!")
    print(
        f"Decision Tree Accuracy : "
        f"{accuracy * 100:.2f}%"
    )

    # Save model
    joblib.dump(
        model,
        "ml/decision_tree.pkl"
    )

    print("Decision Tree Saved Successfully!")

    return model, accuracy


if __name__ == "__main__":
    train_decision_tree()