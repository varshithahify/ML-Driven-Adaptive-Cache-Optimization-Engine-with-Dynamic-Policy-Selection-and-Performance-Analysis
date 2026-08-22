# ==========================================
# PHASE 3
# OPTIMIZED LRU CACHE
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

        # HashMap for O(1) lookup
        self.cache = {}

        # Dummy head and tail nodes
        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head


    # Remove a node from linked list
    def remove(self, node):

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    # Insert node at the front
    # Front = Most Recently Used
    def insert(self, node):

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node


    # Access cache item
    def access(self, key):

        # CACHE HIT
        if key in self.cache:

            node = self.cache[key]

            # Move accessed item to front
            self.remove(node)
            self.insert(node)

            return True


        # CACHE MISS
        else:

            # Cache is full
            if len(self.cache) == self.capacity:

                # Least Recently Used item
                lru = self.tail.prev

                self.remove(lru)

                del self.cache[lru.key]


            # Create new node
            new_node = Node(key)

            # Insert as Most Recently Used
            self.insert(new_node)

            self.cache[key] = new_node

            return False


# Optimized LRU simulation
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