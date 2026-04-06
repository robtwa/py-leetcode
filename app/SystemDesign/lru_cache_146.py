"""
146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity)
Initialize the LRU cache with positive size capacity.

int get(int key)
Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value)
Update the value of the key if the key exists. Otherwise, add the key-value pair
to the cache. If the number of keys exceeds the capacity from this operation,
evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.


Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

class Node:
    def __init__(self, key: int = 0,  value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Create a hash map to store key-node pairs for O(1) access
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key] # get the node from the cache
        self._move_to_head(node) # move the accessed node to the head (most recently used)
        return node.value


    def put(self, key: int, value: int) -> None:
        # update the value of the key if the key exists
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
            return

        # add the key-value pair to the cache
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_node(new_node)

        # remove LRU key if the cache exceeds capacity
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove_node(lru_node)
            del self.cache[lru_node.key]    

    ############################################################################
    # Helper functions
    ############################################################################

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
