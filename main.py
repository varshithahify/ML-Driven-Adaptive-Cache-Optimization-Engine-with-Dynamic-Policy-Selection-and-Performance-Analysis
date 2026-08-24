# ==========================================
# PHASE 10
# AI CACHE POLICY INTEGRATION
# ==========================================

from simulator.workloads import mixed_workload
from simulator.runner import run_all
from ml.predictor import predict_policy


print("========================================")
print(" AI CACHE OPTIMIZATION ENGINE")
print(" PHASE 10 - AI POLICY INTEGRATION")
print("========================================")


# ==========================================
# GENERATE WORKLOAD
# ==========================================

requests = mixed_workload(100)

cache_size = 5

print("\nWorkload Generated!")
print("Total Requests :", len(requests))
print("Cache Size     :", cache_size)


# ==========================================
# AI PREDICTION
# ==========================================

predicted_policy, features = predict_policy(
    requests
)


print("\n========================================")
print(" AI PREDICTION")
print("========================================")

print(
    "Predicted Best Cache Policy :",
    predicted_policy
)


# ==========================================
# DISPLAY FEATURES
# ==========================================

print("\n========================================")
print(" WORKLOAD FEATURES")
print("========================================")

print(
    "Unique Count       :",
    features["unique_count"]
)

print(
    "Repetition Ratio   :",
    features["repetition_ratio"]
)

print(
    "Sequentiality      :",
    features["sequentiality"]
)

print(
    "Frequency Variance :",
    features["frequency_variance"]
)


# ==========================================
# RUN ALL POLICIES
# ==========================================

results = run_all(
    requests,
    cache_size
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n========================================")
print(" CACHE POLICY PERFORMANCE")
print("========================================")

for policy, result in results.items():

    print("\nPolicy :", policy)

    print(
        "Hit Rate  :",
        f"{result['hit_rate'] * 100:.2f}%"
    )

    print(
        "Miss Rate :",
        f"{result['miss_rate'] * 100:.2f}%"
    )

    print(
        "Energy    :",
        result["energy"]
    )

    print(
        "Latency   :",
        result["latency"]
    )


# ==========================================
# AI SELECTED POLICY RESULT
# ==========================================

selected_result = results[
    predicted_policy
]


print("\n========================================")
print(" AI SELECTED POLICY PERFORMANCE")
print("========================================")

print(
    "Selected Policy :",
    predicted_policy
)

print(
    "Hit Rate :",
    f"{selected_result['hit_rate'] * 100:.2f}%"
)

print(
    "Miss Rate :",
    f"{selected_result['miss_rate'] * 100:.2f}%"
)

print(
    "Energy :",
    selected_result["energy"]
)

print(
    "Latency :",
    selected_result["latency"]
)


print("\n========================================")
print(" PHASE 10 COMPLETED")
print("========================================")