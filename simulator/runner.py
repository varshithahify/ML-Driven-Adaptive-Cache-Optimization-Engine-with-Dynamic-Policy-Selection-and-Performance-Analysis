# simulator/runner.py
#phase2
#phase 3 updated code
#pahse 4 updated code
from core.policies import lru, fifo, lfu, lru_optimized
# ===== STRATEGY PATTERN =====
POLICIES = {
    "LRU": lru,
    "FIFO": fifo,
    "LFU": lfu,
    "LRU_OPT": lru_optimized
}
# ===== ENERGY MODEL =====
def calculate_energy(misses):
    return misses * 5
# ===== LATENCY MODEL =====
def calculate_latency(hits, misses):
    return (hits * 1) + (misses * 10)
# ===== RUN SINGLE POLICY =====
def run_policy(policy_name, requests, cache_size):

    if policy_name not in POLICIES:
        raise ValueError("Invalid Policy")

    func = POLICIES[policy_name]

    hits, misses = func(requests, cache_size)

    total = len(requests)

    return {
        "hits": hits,
        "misses": misses,
        "hit_rate": hits / total,
        "miss_rate": misses / total,
        "energy": calculate_energy(misses),
        "latency": calculate_latency(hits, misses)
    }
# ===== RUN ALL POLICIES =====
def run_all(requests, cache_size):

    results = {}

    for name, func in POLICIES.items():

        hits, misses = func(requests, cache_size)

        total = len(requests)

        results[name] = {
            "hit_rate": hits / total,
            "miss_rate": misses / total,
            "energy": calculate_energy(misses),
            "latency": calculate_latency(hits, misses)
        }

    return results


    return results