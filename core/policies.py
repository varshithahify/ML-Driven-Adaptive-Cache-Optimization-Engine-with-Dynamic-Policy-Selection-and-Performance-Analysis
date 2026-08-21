def lru(requests, cache_size):
    cache = []
    hits = 0
    misses = 0

    for req in requests:

        # Cache hit
        if req in cache:
            hits += 1

            # Move recently used item to the end
            cache.remove(req)
            cache.append(req)

        # Cache miss
        else:
            misses += 1

            # Remove least recently used item
            if len(cache) == cache_size:
                cache.pop(0)

            # Add new request
            cache.append(req)

    return hits, misses