# ==========================================
# PHASE 6
# DATASET GENERATION IMPROVEMENT
# main.py
# ==========================================
# PHASE 7.1
# DECISION TREE TRAINING
# ==========================================
#Phase 7.2
#MODEL COMPARISON
# ==========================================
# PHASE 7
# MACHINE LEARNING MODEL TRAINING
# DECISION TREE + RANDOM FOREST
# ==========================================
# ==========================================
# PHASE 8
# MODEL EVALUATION
# ==========================================
# PHASE 9
# AI CACHE POLICY PREDICTION
# ==========================================

from simulator.workloads import (
    random_workload,
    sequential_workload,
    repetitive_workload,
    mixed_workload
)

from ml.predictor import predict_policy


print("========================================")
print(" AI CACHE PROJECT")
print(" PHASE 9 - AI POLICY PREDICTION")
print("========================================")


# ==========================================
# GENERATE NEW WORKLOAD
# ==========================================

requests = mixed_workload(100)


print("\nNew Workload Generated!")

print("\nFirst 20 Memory Requests:")
print(requests[:20])


# ==========================================
# AI PREDICTION
# ==========================================

predicted_policy, features = predict_policy(
    requests
)


# ==========================================
# DISPLAY FEATURES
# ==========================================

print("\n========================================")
print(" WORKLOAD FEATURES")
print("========================================")

print(
    "Unique Count :",
    features["unique_count"]
)

print(
    "Repetition Ratio :",
    features["repetition_ratio"]
)

print(
    "Sequentiality :",
    features["sequentiality"]
)

print(
    "Frequency Variance :",
    features["frequency_variance"]
)


# ==========================================
# DISPLAY AI PREDICTION
# ==========================================

print("\n========================================")
print(" AI PREDICTION")
print("========================================")

print(
    "Predicted Best Cache Policy :",
    predicted_policy
)


print("\n========================================")
print(" PHASE 9 COMPLETED")
print("========================================")