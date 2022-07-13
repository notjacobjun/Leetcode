"""
Observations:
- Need to keep track of which elements were least recently used so need some priority structure
- Need ability to update the storage in O(1) so maybe array, deque, or hash table
- Access values by key so most likely hash table underlying
- Keep track of time to implement priority
- Use a priority queue wrt to time for priority implementation

Approach 1 (Brute force):
- Keep a running counter for the time
- Use a hash table for storage
- min heap for priority queue when we have reached the capacity
- Operations:
    - When element is accessed via get then update the priority with the current time
    - When element is inserted then insert the element into min heap with the current priority 
Time: O(log(n)) for insertion and update, but O(1) for get operation
Space: O(n)

Approach 2:
- Use the same idea as above except replace priority queue with doubly linked list where we use the links as the ordering.
- Then support the doubly linked list with a hashmap to cache each LL node.
    - This way we can help find nodes in O(1) time by sacrificing some extra space.
Time: O(1) for all operations
Space: O(1)
"""


class Node:

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
