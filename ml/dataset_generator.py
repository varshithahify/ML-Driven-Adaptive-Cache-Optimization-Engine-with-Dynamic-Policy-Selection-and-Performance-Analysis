# ==========================================
# PHASE 6
# ML DATASET GENERATION
# ==========================================

import csv
import os
import random

from ml.features import extract_features


# ==========================================
# CACHE POLICIES
# ==========================================

def lru(requests, cache_size):
    cache = []
    hits = 0

    for item in requests:
        if item in cache:
            hits += 1
            cache.remove(item)
            cache.append(item)
        else:
            if len(cache) >= cache_size:
                cache.pop(0)

            cache.append(item)

    return hits


def fifo(requests, cache_size):
    cache = []
    hits = 0

    for item in requests:
        if item in cache:
            hits += 1
        else:
            if len(cache) >= cache_size:
                cache.pop(0)

            cache.append(item)

    return hits


def lfu(requests, cache_size):
    cache = []
    frequency = {}
    hits = 0

    for item in requests:

        frequency[item] = frequency.get(item, 0) + 1

        if item in cache:
            hits += 1
        else:
            if len(cache) >= cache_size:

                least_used = min(
                    cache,
                    key=lambda x: frequency.get(x, 0)
                )

                cache.remove(least_used)

            cache.append(item)

    return hits


def lru_optimized(requests, cache_size):
    # For Phase 6, use LRU as the baseline optimized policy.
    return lru(requests, cache_size)


# ==========================================
# RANDOM WORKLOAD
# ==========================================

def generate_workload(length=100):

    return [
        random.randint(0, 20)
        for _ in range(length)
    ]


# ==========================================
# FIND BEST POLICY
# ==========================================

def find_best_policy(requests, cache_size):

    policies = {
        "LRU": lru,
        "FIFO": fifo,
        "LFU": lfu,
        "LRU_OPT": lru_optimized
    }

    best_policy = None
    best_hit_rate = -1

    for name, policy in policies.items():

        hits = policy(
            requests,
            cache_size
        )

        hit_rate = hits / len(requests)

        if hit_rate > best_hit_rate:

            best_hit_rate = hit_rate
            best_policy = name

    return best_policy


# ==========================================
# DATASET GENERATION
# ==========================================

def generate_dataset(
    samples=300,
    cache_size=5
):

    print("========================================")
    print(" PHASE 6 - DATASET GENERATION")
    print("========================================")

    # Create datasets folder if it doesn't exist
    os.makedirs("datasets", exist_ok=True)

    file_path = "datasets/dataset.csv"

    with open(
        file_path,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        # ==========================================
        # CSV HEADER
        # ==========================================

        writer.writerow([
            "unique_count",
            "repetition_ratio",
            "sequentiality",
            "frequency_variance",
            "best_policy"
        ])

        # ==========================================
        # GENERATE DATA
        # ==========================================

        for i in range(samples):

            # Generate workload
            requests = generate_workload(100)

            # Extract features
            features = extract_features(
                requests
            )

            # Find best cache policy
            best_policy = find_best_policy(
                requests,
                cache_size
            )

            # Write dataset row
            writer.writerow([
                features["unique_count"],
                features["repetition_ratio"],
                features["sequentiality"],
                features["frequency_variance"],
                best_policy
            ])

            print(
                f"Sample {i + 1}/{samples} Generated"
            )

    print()
    print("========================================")
    print(" DATASET GENERATED SUCCESSFULLY")
    print(" Total Samples :", samples)
    print(" Saved File    :", file_path)
    print("========================================")


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":
    generate_dataset()