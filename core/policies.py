# ==========================================
# PHASE 2
# BASIC CACHE REPLACEMENT POLICIES
# ==========================================


def lru(requests, cache_size):
    """
    Least Recently Used (LRU) cache policy.
    """

    cache = []
    hits = 0
    misses = 0

    for req in requests:

        if req in cache:
            # Cache hit
            hits += 1

            # Move recently used item to the end
            cache.remove(req)
            cache.append(req)

        else:
            # Cache miss
            misses += 1

            # Remove least recently used item
            if len(cache) == cache_size:
                cache.pop(0)

            # Add new item
            cache.append(req)

    return hits, misses


def fifo(requests, cache_size):
    """
    First In First Out (FIFO) cache policy.
    """

    cache = []
    hits = 0
    misses = 0

    for req in requests:

        if req in cache:
            # Cache hit
            hits += 1

        else:
            # Cache miss
            misses += 1

            # Remove oldest item
            if len(cache) == cache_size:
                cache.pop(0)

            # Add new item
            cache.append(req)

    return hits, misses


def lfu(requests, cache_size):
    """
    Least Frequently Used (LFU) cache policy.
    """

    cache = []
    frequency = {}

    hits = 0
    misses = 0

    for req in requests:

        if req in cache:
            # Cache hit
            hits += 1
            frequency[req] += 1

        else:
            # Cache miss
            misses += 1

            # Cache is full
            if len(cache) == cache_size:

                # Find least frequently used item
                lfu_item = min(
                    cache,
                    key=lambda x: frequency[x]
                )

                cache.remove(lfu_item)
                del frequency[lfu_item]

            # Add new item
            cache.append(req)
            frequency[req] = 1

    return hits, misses