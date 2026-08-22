# ==========================================
# PHASE 4
# CACHE WORKLOAD GENERATION
# ==========================================

import random


# ==========================================
# SEQUENTIAL WORKLOAD
# ==========================================

def sequential_workload(size):

    return list(range(size))


# ==========================================
# REPETITIVE WORKLOAD
# ==========================================

def repetitive_workload(size):

    base = [1, 2, 3]

    return [
        random.choice(base)
        for _ in range(size)
    ]


# ==========================================
# RANDOM WORKLOAD
# ==========================================

def random_workload(size):

    return [
        random.randint(1, 20)
        for _ in range(size)
    ]


# ==========================================
# MIXED WORKLOAD
# ==========================================

def mixed_workload(size):

    data = []

    for _ in range(size):

        pattern = random.choice([
            "sequential",
            "repetitive",
            "random"
        ])

        if pattern == "sequential":

            data.append(
                random.randint(1, 50)
            )

        elif pattern == "repetitive":

            data.append(
                random.choice([1, 2, 3])
            )

        else:

            data.append(
                random.randint(1, 20)
            )

    return data