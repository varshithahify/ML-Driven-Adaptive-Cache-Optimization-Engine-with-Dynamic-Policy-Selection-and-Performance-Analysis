# ==========================================
# PHASE 2
# BASIC CACHE REPLACEMENT POLICIES
# ==========================================


# ==========================================
# LRU - Least Recently Used
# ==========================================

def lru(requests, cache_size):

    cache = []
    hits = 0
    misses = 0

    for req in requests:

        if req in cache:

            hits += 1

            # Move recently used item to the end
            cache.remove(req)
            cache.append(req)

        else:

            misses += 1

            if len(cache) == cache_size:
                cache.pop(0)

            cache.append(req)

    return hits, misses


# ==========================================
# FIFO - First In First Out
# ==========================================

def fifo(requests, cache_size):

    cache = []
    hits = 0
    misses = 0

    for req in requests:

        if req in cache:

            hits += 1

        else:

            misses += 1

            if len(cache) == cache_size:
                cache.pop(0)

            cache.append(req)

    return hits, misses


# ==========================================
# LFU - Least Frequently Used
# ==========================================

def lfu(requests, cache_size):

    cache = []
    freq = {}

    hits = 0
    misses = 0

    for req in requests:

        if req in cache:

            hits += 1
            freq[req] += 1

        else:

            misses += 1

            if len(cache) == cache_size:

                lfu_item = min(
                    cache,
                    key=lambda x: freq[x]
                )

                cache.remove(lfu_item)
                del freq[lfu_item]

            cache.append(req)
            freq[req] = 1

    return hits, misses


# ==========================================
# PHASE 3
# OPTIMIZED LRU
# HashMap + Doubly Linked List
# ==========================================


class Node:

    def __init__(self, key):

        self.key = key
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):

        self.capacity = capacity

        # HashMap
        self.cache = {}

        # Dummy nodes
        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head


    # --------------------------------------
    # Remove node
    # --------------------------------------

    def remove(self, node):

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    # --------------------------------------
    # Insert node at front
    # --------------------------------------

    def insert(self, node):

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node


    # --------------------------------------
    # Access cache
    # --------------------------------------

    def access(self, key):

        # CACHE HIT
        if key in self.cache:

            node = self.cache[key]

            # Move to front
            self.remove(node)
            self.insert(node)

            return True


        # CACHE MISS
        else:

            if len(self.cache) == self.capacity:

                # Least Recently Used
                lru_node = self.tail.prev

                self.remove(lru_node)

                del self.cache[lru_node.key]


            # Create new node
            new_node = Node(key)

            self.insert(new_node)

            self.cache[key] = new_node

            return False


# ==========================================
# OPTIMIZED LRU SIMULATION
# ==========================================

def lru_optimized(requests, cache_size):

    cache = LRUCache(cache_size)

    hits = 0
    misses = 0

    for req in requests:

        if cache.access(req):

            hits += 1

        else:

            misses += 1

    return hits, misses