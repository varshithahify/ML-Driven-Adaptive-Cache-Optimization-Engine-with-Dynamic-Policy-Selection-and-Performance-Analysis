# ==========================================
# PHASE 3
# CACHE SIMULATOR RUNNER
# ==========================================

from core.policies import (
    lru,
    fifo,
    lfu,
    lru_optimized
)


# ==========================================
# CACHE POLICIES
# Strategy Pattern
# ==========================================

POLICIES = {
    "LRU": lru,
    "FIFO": fifo,
    "LFU": lfu,
    "LRU_OPT": lru_optimized
}


# ==========================================
# ENERGY MODEL
# ==========================================

def calculate_energy(misses):
    return misses * 5


# ==========================================
# LATENCY MODEL
# ==========================================

def calculate_latency(hits, misses):
    return (hits * 1) + (misses * 10)


# ==========================================
# RUN SINGLE CACHE POLICY
# ==========================================

def run_policy(policy_name, requests, cache_size):

    if policy_name not in POLICIES:
        raise ValueError("Invalid cache policy")

    policy = POLICIES[policy_name]

    hits, misses = policy(
        requests,
        cache_size
    )

    total = len(requests)

    return {
        "hits": hits,
        "misses": misses,
        "hit_rate": hits / total,
        "miss_rate": misses / total,
        "energy": calculate_energy(misses),
        "latency": calculate_latency(
            hits,
            misses
        )
    }


# ==========================================
# RUN ALL CACHE POLICIES
# ==========================================

def run_all(requests, cache_size):

    results = {}

    for policy_name in POLICIES:

        results[policy_name] = run_policy(
            policy_name,
            requests,
            cache_size
        )

    return results