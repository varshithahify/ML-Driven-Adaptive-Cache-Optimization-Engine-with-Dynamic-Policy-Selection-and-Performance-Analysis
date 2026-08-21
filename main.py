from core.policies import lru

requests = [1, 2, 3, 1, 4, 2, 5, 1]
cache_size = 3

hits, misses = lru(requests, cache_size)

print("Cache Requests:", requests)
print("Cache Size:", cache_size)
print("Hits:", hits)
print("Misses:", misses)