# ==========================================
# PHASE 5
# FEATURE EXTRACTION TEST
# ==========================================

from ml.features import extract_features
from simulator.workloads import (
    sequential_workload,
    repetitive_workload,
    random_workload,
    mixed_workload
)


print("========================================")
print(" PHASE 5 - FEATURE EXTRACTION")
print("========================================")


# ==========================================
# TEST SEQUENTIAL WORKLOAD
# ==========================================

requests = sequential_workload(20)

features = extract_features(requests)

print("\n========== SEQUENTIAL ==========")

print("Requests:")
print(requests)

print("\nFeatures:")
print(features)


# ==========================================
# TEST REPETITIVE WORKLOAD
# ==========================================

requests = repetitive_workload(20)

features = extract_features(requests)

print("\n========== REPETITIVE ==========")

print("Requests:")
print(requests)

print("\nFeatures:")
print(features)


# ==========================================
# TEST RANDOM WORKLOAD
# ==========================================

requests = random_workload(20)

features = extract_features(requests)

print("\n========== RANDOM ==========")

print("Requests:")
print(requests)

print("\nFeatures:")
print(features)


# ==========================================
# TEST MIXED WORKLOAD
# ==========================================

requests = mixed_workload(20)

features = extract_features(requests)

print("\n========== MIXED ==========")

print("Requests:")
print(requests)

print("\nFeatures:")
print(features)


print("\n========================================")
print(" PHASE 5 COMPLETED")
print("========================================")