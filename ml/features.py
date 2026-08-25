#phase 5
from collections import Counter
import statistics


def extract_features(requests):

    total = len(requests)

    # Unique Count
    unique = len(set(requests))

    # Repetition Ratio
    repetition = 1 - (unique / total)

    # Sequentiality
    seq_count = 0

    for i in range(1, total):

        if requests[i] == requests[i - 1] + 1:
            seq_count += 1

    sequentiality = seq_count / total

    # Frequency Variance
    freq = Counter(requests)

    variance = statistics.variance(freq.values()) \
        if len(freq.values()) > 1 else 0

    return {
        "unique_count": unique,
        "repetition_ratio": repetition,
        "sequentiality": sequentiality,
        "frequency_variance": variance
    }