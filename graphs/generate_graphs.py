# ==========================================
# PHASE 11
# PERFORMANCE VISUALIZATION
# ==========================================

import matplotlib.pyplot as plt

from simulator.runner import run_all
from simulator.workloads import mixed_workload


def generate_graphs():

    print("\nGenerating Graphs...\n")

    # Generate workload
    requests = mixed_workload(100)

    # Run all cache policies
    results = run_all(requests, cache_size=5)

    policies = list(results.keys())

    hit_rates = [
        results[p]["hit_rate"] * 100
        for p in policies
    ]

    miss_rates = [
        results[p]["miss_rate"] * 100
        for p in policies
    ]

    energy = [
        results[p]["energy"]
        for p in policies
    ]

    latency = [
        results[p]["latency"]
        for p in policies
    ]

    # ---------------------------------
    # Hit Rate
    # ---------------------------------

    plt.figure(figsize=(6,4))
    plt.bar(policies, hit_rates)
    plt.title("Hit Rate Comparison")
    plt.ylabel("Hit Rate (%)")
    plt.savefig("graphs/hit_rate.png")
    plt.close()

    # ---------------------------------
    # Miss Rate
    # ---------------------------------

    plt.figure(figsize=(6,4))
    plt.bar(policies, miss_rates)
    plt.title("Miss Rate Comparison")
    plt.ylabel("Miss Rate (%)")
    plt.savefig("graphs/miss_rate.png")
    plt.close()

    # ---------------------------------
    # Energy
    # ---------------------------------

    plt.figure(figsize=(6,4))
    plt.bar(policies, energy)
    plt.title("Energy Comparison")
    plt.ylabel("Energy")
    plt.savefig("graphs/energy.png")
    plt.close()

    # ---------------------------------
    # Latency
    # ---------------------------------

    plt.figure(figsize=(6,4))
    plt.bar(policies, latency)
    plt.title("Latency Comparison")
    plt.ylabel("Latency")
    plt.savefig("graphs/latency.png")
    plt.close()

    print("Graphs Generated Successfully!")