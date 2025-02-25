"""
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.

Example 1:

Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

Output:
[null, null, 10, null, null, 20, -1]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20 
lRUCache.get(1);      // return -1 (not found)
Constraints:

1 <= capacity <= 100
0 <= key <= 1000
0 <= value <= 1000


Recommended Time & Space Complexity
You should aim for a solution with O(1) time for each put() and get() function call and an overall space of O(n), 
where n is the capacity of the LRU cache.

"""

# We need to use a Doubly Linked List to ensure we can remove and add elements in O(1) if we have their address
# To get adress in O(1), we need another Hash Table
class DLL_Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.previous = None

class LRUCache:

    def __init__(self, capacity: int):
        self.current_count = 0
        self.cap = capacity
        self.hash_map_nodes = {}
        self.lru_node = DLL_Node() #Head Always @beginning
        self.mru_node = DLL_Node() #Tail Always @end

    def get(self, key: int) -> int:
        print(f"Getting Key: {key}")
        if key not in self.hash_map_nodes:
            print("Key not found!")
            return -1
        else:
            # If cap is 1, just return the value
            node = self.hash_map_nodes[key]
            node_val = node.val
            print(f"Key found with val:{node_val}")
            if self.cap==1:
                print("Capacity is 1, No Need to update!")
                # If only 1 node @cache, don't need to update
                return node_val
            else:
                # We need to remove this node and add it to tail
                
                # Remove Node
                prev_node = node.previous
                print(f"Prev Node is: {prev_node.key, prev_node.val}")
                next_node = node.next
                print(f"Next Node is: {next_node.key, next_node.val}")
                prev_node.next = next_node
                next_node.previous = prev_node

                # Add @Tail
                last_node = self.mru_node.previous
                last_node.next = node
                node.next = self.mru_node
                node.previous = last_node
                self.mru_node.previous = node
                print(f"New MRU Node: {self.mru_node.previous.key, self.mru_node.previous.val}")
                print(f"New LRU Node: {self.lru_node.next.key, self.lru_node.next.val}")
                return node_val
        
    def put(self, key: int, value: int) -> None:
        print(f"Put for Key: {key} and Value: {value}")
        # First check if key in Hash Map or not
        # If it is we update the value of node
        # Else create a new node and add accordingly
        if key in self.hash_map_nodes:
            # Update val
            print("Key in HashMap, updating value!")
            self.hash_map_nodes[key].val = value
        else:
            print("Key not in HashMap")
            # Depending on current count we add a node
            if self.current_count == self.cap: #Will always be max equal to cap never gt
                # Since there is no capacity to add a new node
                # We remove the LRU Node and then add a node @tail (MRU)
                print(f"Cache is at capacity with {self.current_count}")
                # Removing Node from LRU
                lru_node = self.lru_node.next
                key_to_remove = lru_node.key
                print(f"LRU Found: {key_to_remove}")
                if lru_node.next != self.mru_node:
                    # There is some node we need LRU to point to now & vice versa
                    lru_node.next.previous = self.lru_node
                    self.lru_node.next = lru_node.next
                    lru_node.next = None
                    lru_node.previous = None

                    # Now add a new node @tail
                    new_node = DLL_Node(key, value)
                    self.hash_map_nodes[key] = new_node

                    last_node = self.mru_node.previous
                    last_node.next = new_node
                    new_node.previous = last_node
                    new_node.next = self.mru_node
                    self.mru_node.previous = new_node
                
                else:
                    # This means that there is no node after lru node
                    # Only pointing to MRU
                    # Remove from MRU as well
                    self.lru_node.next = None #Will point to New Node
                    self.mru_node.previous = None #Will point to New Node
                    lru_node.next = None
                    lru_node.previous = None

                    # Now add a new node @tail
                    new_node = DLL_Node(key, value)
                    self.hash_map_nodes[key] = new_node

                    self.lru_node.next = new_node
                    self.mru_node.previous = new_node
                    new_node.next = self.mru_node
                    new_node.previous = self.lru_node

                #@end remove the lru key from hashmap
                self.hash_map_nodes.pop(key_to_remove)
   
            else:
                print(f"There is capacity left to add a new node!: {self.current_count}")
                # There is capacity left to add a new entry
                # Add a new node @tail, so MRU is now that
                new_node = DLL_Node(key, value)
                if self.mru_node.previous is not None: #This means there is a node before MRU
                    print("Cache NOT Empty")
                    last_node = self.mru_node.previous
                    self.mru_node.previous = new_node
                    new_node.previous = last_node
                else: #No Node, therefore Cache Empty
                    print("Cache was Empty")
                    self.mru_node.previous = new_node
                    # Since empty, LRU is also this
                    self.lru_node.next = new_node
                    new_node.previous = self.lru_node

                new_node.next = self.mru_node
                
                self.hash_map_nodes[key] = new_node #Pointer to Node
                self.current_count +=1

        print(f"@END, LRU is: {self.lru_node.next.key, self.lru_node.next.val}")
        print(f"@END, MRU is: {self.mru_node.previous.key, self.mru_node.previous.val}")

        
