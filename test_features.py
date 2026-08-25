from ml.features import extract_features
from simulator.workloads import repetitive_workload

# Generate workload
requests = repetitive_workload(20)

# Extract features
features = extract_features(requests)

print("\nRequests:")
print(requests)

print("\nFeatures:")
print(features)