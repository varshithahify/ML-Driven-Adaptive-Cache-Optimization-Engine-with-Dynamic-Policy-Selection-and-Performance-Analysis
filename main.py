# ==========================================
# PHASE 4
# CACHE WORKLOAD SIMULATION
# ==========================================

from simulator.workloads import (
    sequential_workload,
    repetitive_workload,
    random_workload,
    mixed_workload
)

from simulator.runner import simulate_workload


print("========================================")
print(" AI CACHE OPTIMIZATION ENGINE")
print(" PHASE 4 - WORKLOAD SIMULATION")
print("========================================")


cache_size = 5


# ==========================================
# SEQUENTIAL WORKLOAD
# ==========================================

print("\n\n========== SEQUENTIAL WORKLOAD ==========")

requests = sequential_workload(100)

simulate_workload(
    requests,
    cache_size
)


# ==========================================
# REPETITIVE WORKLOAD
# ==========================================

print("\n\n========== REPETITIVE WORKLOAD ==========")

requests = repetitive_workload(100)

simulate_workload(
    requests,
    cache_size
)


# ==========================================
# RANDOM WORKLOAD
# ==========================================

print("\n\n========== RANDOM WORKLOAD ==========")

requests = random_workload(100)

simulate_workload(
    requests,
    cache_size
)


# ==========================================
# MIXED WORKLOAD
# ==========================================

print("\n\n========== MIXED WORKLOAD ==========")

requests = mixed_workload(100)

simulate_workload(
    requests,
    cache_size
)


print("\n========================================")
print(" PHASE 4 COMPLETED")
print("========================================")