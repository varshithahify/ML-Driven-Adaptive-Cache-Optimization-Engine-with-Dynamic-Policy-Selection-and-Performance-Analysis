def lru(requests, cache_size):
    cache = []
    hits, misses = 0, 0

    for req in requests:
        if req in cache:
            hits += 1
            cache.remove(req)
            cache.append(req)
        else:
            misses += 1
            if len(cache) == cache_size:
                cache.pop(0)
            cache.append(req)

    return hits, misses


def fifo(requests, cache_size):
    cache = []
    hits, misses = 0, 0

    for req in requests:
        if req in cache:
            hits += 1
        else:
            misses += 1
            if len(cache) == cache_size:
                cache.pop(0)
            cache.append(req)

    return hits, misses


def lfu(requests, cache_size):
    cache = []
    freq = {}
    hits, misses = 0, 0

    for req in requests:
        if req in cache:
            hits += 1
            freq[req] += 1
        else:
            misses += 1
            if len(cache) == cache_size:
                lfu_item = min(cache, key=lambda x: freq[x])
                cache.remove(lfu_item)
                del freq[lfu_item]

            cache.append(req)
            freq[req] = 1

    return hits, misses
# phase 2
class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def access(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return True
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]

            new_node = Node(key)
            self.insert(new_node)
            self.cache[key] = new_node
            return False


def lru_optimized(requests, cache_size):
    cache = LRUCache(cache_size)
    hits, misses = 0, 0

    for req in requests:
        if cache.access(req):
            hits += 1
        else:
            misses += 1

    return hits, misses
