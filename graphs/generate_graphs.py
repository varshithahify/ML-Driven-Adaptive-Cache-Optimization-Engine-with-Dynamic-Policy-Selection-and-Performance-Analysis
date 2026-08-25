# ==========================================
# PHASE 11
# PERFORMANCE VISUALIZATION
# ==========================================

import os
import matplotlib.pyplot as plt

from simulator.runner import run_all
from simulator.workloads import mixed_workload


def generate_graphs():

    print("\n========================================")
    print(" PHASE 11 - PERFORMANCE VISUALIZATION")
    print("========================================")

    # ==========================================
    # CREATE GRAPH DIRECTORY
    # ==========================================

    os.makedirs("graphs", exist_ok=True)

    # ==========================================
    # GENERATE WORKLOAD
    # ==========================================

    requests = mixed_workload(100)

    cache_size = 5

    print("\nWorkload Generated!")
    print("Total Requests :", len(requests))
    print("Cache Size     :", cache_size)


    # ==========================================
    # RUN ALL CACHE POLICIES
    # ==========================================

    results = run_all(
        requests,
        cache_size
    )


    policies = list(
        results.keys()
    )


    # ==========================================
    # EXTRACT RESULTS
    # ==========================================

    hit_rates = [
        results[policy]["hit_rate"] * 100
        for policy in policies
    ]

    miss_rates = [
        results[policy]["miss_rate"] * 100
        for policy in policies
    ]

    energy = [
        results[policy]["energy"]
        for policy in policies
    ]

    latency = [
        results[policy]["latency"]
        for policy in policies
    ]


    # ==========================================
    # HIT RATE GRAPH
    # ==========================================

    plt.figure(figsize=(6, 4))

    plt.bar(
        policies,
        hit_rates
    )

    plt.title(
        "Hit Rate Comparison"
    )

    plt.ylabel(
        "Hit Rate (%)"
    )

    plt.xlabel(
        "Cache Policy"
    )

    plt.tight_layout()

    plt.savefig(
        "graphs/hit_rate.png"
    )

    plt.close()


    # ==========================================
    # MISS RATE GRAPH
    # ==========================================

    plt.figure(figsize=(6, 4))

    plt.bar(
        policies,
        miss_rates
    )

    plt.title(
        "Miss Rate Comparison"
    )

    plt.ylabel(
        "Miss Rate (%)"
    )

    plt.xlabel(
        "Cache Policy"
    )

    plt.tight_layout()

    plt.savefig(
        "graphs/miss_rate.png"
    )

    plt.close()


    # ==========================================
    # ENERGY GRAPH
    # ==========================================

    plt.figure(figsize=(6, 4))

    plt.bar(
        policies,
        energy
    )

    plt.title(
        "Energy Comparison"
    )

    plt.ylabel(
        "Energy"
    )

    plt.xlabel(
        "Cache Policy"
    )

    plt.tight_layout()

    plt.savefig(
        "graphs/energy.png"
    )

    plt.close()


    # ==========================================
    # LATENCY GRAPH
    # ==========================================

    plt.figure(figsize=(6, 4))

    plt.bar(
        policies,
        latency
    )

    plt.title(
        "Latency Comparison"
    )

    plt.ylabel(
        "Latency"
    )

    plt.xlabel(
        "Cache Policy"
    )

    plt.tight_layout()

    plt.savefig(
        "graphs/latency.png"
    )

    plt.close()


    # ==========================================
    # DISPLAY RESULTS
    # ==========================================

    print("\n========================================")
    print(" GRAPH GENERATION COMPLETED")
    print("========================================")

    print("\nGenerated Graphs:")

    print("1. graphs/hit_rate.png")
    print("2. graphs/miss_rate.png")
    print("3. graphs/energy.png")
    print("4. graphs/latency.png")

    print("\n========================================")
    print(" PHASE 11 COMPLETED")
    print("========================================")


if __name__ == "__main__":
    generate_graphs()