class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    def __str__(self):
        return str(self.val)

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    # @return an integer
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._update_cache(node)
            return node.val
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if len(self.cache) == self.capacity and key not in self.cache:
            tail = self.tail
            if tail.prev:
                prev = tail.prev
                prev.next = None
            del self.cache[tail.key]
            self.tail = tail.prev
            if len(self.cache) == 0:
                self.head = None
        if key in self.cache:
            node = self.cache[key]
            node.val = value
        else:
            node = Node(key=key, val=value)
        self._update_cache(node)

    def _update_cache(self, node):
        key = node.key
        if len(self.cache) == 0:
            self.head = node
            self.tail = node
            self.cache[key] = node
            return

        if key in self.cache:
            if self.head == node:
                return
            if node.prev:
                prev = node.prev
                prev.next = node.next
            if node.next:
                next = node.next
                next.prev = node.prev
            else:
                self.tail = node.prev

        else:
            self.cache[key] = node
        head = self.head
        head.prev = node
        node.prev = None
        node.next = self.head
        self.head = node

solution = LRUCache(2)
solution.set(2,1)
solution.set(2,2)
print(solution.get(2))
solution.set(1,1)
solution.set(4,1)
# print(solution.get(1))
print(solution.get(2))
