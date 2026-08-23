# ==========================================
# PHASE 5
# WORKLOAD FEATURE EXTRACTION
# ==========================================

from collections import Counter
import statistics


def extract_features(requests):

    total = len(requests)

    if total == 0:
        return {
            "unique_count": 0,
            "repetition_ratio": 0,
            "sequentiality": 0,
            "frequency_variance": 0
        }

    # ==========================================
    # UNIQUE COUNT
    # ==========================================

    unique_count = len(set(requests))


    # ==========================================
    # REPETITION RATIO
    # ==========================================

    repetition_ratio = 1 - (
        unique_count / total
    )


    # ==========================================
    # SEQUENTIALITY
    # ==========================================

    sequential_count = 0

    for i in range(1, total):

        if requests[i] == requests[i - 1] + 1:
            sequential_count += 1

    sequentiality = sequential_count / total


    # ==========================================
    # FREQUENCY VARIANCE
    # ==========================================

    frequency = Counter(requests)

    frequency_values = list(
        frequency.values()
    )

    if len(frequency_values) > 1:

        frequency_variance = statistics.variance(
            frequency_values
        )

    else:

        frequency_variance = 0


    # ==========================================
    # RETURN FEATURES
    # ==========================================

    return {
        "unique_count": unique_count,
        "repetition_ratio": repetition_ratio,
        "sequentiality": sequentiality,
        "frequency_variance": frequency_variance
    }