# ==========================================
# PHASE 6
# DATASET GENERATOR
# ==========================================

import csv

from simulator.workloads import random_workload
from simulator.runner import run_all
from ml.features import extract_features


def generate_dataset(samples=300, cache_size=5):

    print("\nGenerating Dataset...\n")

    with open("datasets/dataset.csv", "w", newline="") as file:

        writer = csv.writer(file)

        # CSV Header
        writer.writerow([
            "unique_count",
            "repetition_ratio",
            "sequentiality",
            "frequency_variance",
            "best_policy"
        ])

        # Generate samples
        for i in range(samples):

            # Generate random workload
            requests = random_workload(100)

            # Extract workload features
            features = extract_features(requests)

            # Run all cache policies
            results = run_all(requests, cache_size)

            # Find the policy with highest hit rate
            best_policy = max(
                results,
                key=lambda policy: results[policy]["hit_rate"]
            )

            # Save one row into dataset.csv
            writer.writerow([
                features["unique_count"],
                features["repetition_ratio"],
                features["sequentiality"],
                features["frequency_variance"],
                best_policy
            ])

            print(f"Sample {i + 1}/{samples} Generated")

    print("\n===================================")
    print(" Dataset Generated Successfully!")
    print(" Total Samples :", samples)
    print(" Saved File : datasets/dataset.csv")
    print("===================================")