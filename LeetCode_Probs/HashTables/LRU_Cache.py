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
        self.lru_node = None #Head Always @beginning
        self.mru_node = None #Tail Always @end

    def visualise(self):
        if self.lru_node is not None:
            print("None->")
            curr_node = self.lru_node
            while curr_node is not None:
                print(f"[{curr_node.key}, {curr_node.val}]->")
                curr_node = curr_node.next
            print("None")
        else:
            print("Empty Cache!")

    def get(self, key: int) -> int:
        self.visualise()
        print(f"Getting Key: {key}")
        if key not in self.hash_map_nodes:
            print("Key not found!")
            return -1
        else:
            # If cap is 1, just return the value
            node = self.hash_map_nodes[key]
            node_val = node.val
            print(f"Key found with val:{node_val}")
            if self.current_count==1 or self.cap==1:
                print("Count/Capacity is 1, No Need to update!")
                # If only 1 node @cache, don't need to update
                return node_val
            else:
                # We need to remove this node and add it to tail

                # Check if Node is @Head or not
                if self.lru_node==node:
                    print("Node is Head")
                    next_node = node.next
                    print(f"Next Node is: {next_node.key}")
                    self.lru_node = next_node
                    next_node.previous = None

                    print("Adding Node @Tail now")

                    # Add @Tail
                    last_node = self.mru_node
                    last_node.next = node
                    node.previous = last_node
                    node.next = None
                    self.mru_node = node #Make it the Tail
                else:
                    # Check if node is @tail already or not
                    # If it is, do nothing
                    # Else Simply disconnect, allow previous to connect to next
                    # Then add it @ tail
                    if self.mru_node!=node:
                        print("Node is not at Tail!")
                        prev_node = node.previous
                        print(f"Prev Node is: {prev_node.key, prev_node.val}")
                        next_node = node.next
                        print(f"Next Node is: {next_node.key, next_node.val}")
                        prev_node.next = next_node
                        next_node.previous = prev_node
                
                        # Add @Tail
                        last_node = self.mru_node
                        last_node.next = node
                        node.previous = last_node
                        node.next = None
                        self.mru_node = node #Make it the Tail
                
                print(f"New MRU Node: {self.mru_node.key, self.mru_node.val}")
                print(f"New LRU Node: {self.lru_node.key, self.lru_node.val}")
                return node_val
        
    def put(self, key: int, value: int) -> None:
        self.visualise()
        print(f"Put for Key: {key} and Value: {value}")
        # First check if key in Hash Map or not
        # If it is we update the value of node
        # Else create a new node and add accordingly
        if key in self.hash_map_nodes:
            # Update val
            print("Key in HashMap, updating value!")
            self.hash_map_nodes[key].val = value
            # Also need to bring it to MRU
            # Let's just call get on it!
            self.get(key)
        else:
            print("Key not in HashMap")
            # Depending on current count we add a node
            new_node = DLL_Node(key, value)
            self.hash_map_nodes[key] = new_node
            if self.current_count == self.cap: #Will always be max equal to cap never gt
                # Since there is no capacity to add a new node
                # We remove the LRU Node and then add a node @tail (MRU)
                print(f"Cache is at capacity with {self.current_count}")

                if self.cap==1:
                    print("Max Cap is 1")
                    # Remove old lru node
                    lru_node = self.lru_node
                    key_to_remove = lru_node.key
                    print(f"LRU Found: {key_to_remove}")
                    self.hash_map_nodes.pop(key_to_remove)
                    # If only 1 node can be added
                    self.lru_node = new_node
                    self.mru_node = new_node

                else:
                    # Now we need to remove the LRU & Add the new node @MRU
                    # Removing LRU Node
                    lru_node = self.lru_node
                    key_to_remove = lru_node.key
                    print(f"LRU Found: {key_to_remove}")
                    self.hash_map_nodes.pop(key_to_remove)
                    lru_node.next.previous = None
                    self.lru_node = lru_node.next
                    # Add the new node @MRU
                    mru_node = self.mru_node
                    mru_node.next = new_node
                    new_node.previous = mru_node
                    self.mru_node = new_node

            else:
                print(f"There is capacity left to add a new node!: {self.current_count}")
                # There is capacity left to add a new entry
                # Add a new node @tail, so MRU is now that
                if self.current_count==0:
                    self.lru_node = new_node
                    self.mru_node = new_node
                else:
                    current_mru = self.mru_node
                    current_mru.next = new_node
                    new_node.previous = current_mru
                    self.mru_node = new_node
                
                self.current_count +=1

        print(f"@END, LRU is: {self.lru_node.key, self.lru_node.val}")
        print(f"@END, MRU is: {self.mru_node.key, self.mru_node.val}")

#"LRUCache", [3], 
ip_commands = ["put", [1, 1], "put", [2, 2], "put", [3, 3], "get", [1], "get", [2], "get", [4], "put", [4, 4], "get", [1], "get", [2], "get", [3], "get", [4], "get", [2], "put", [1, 8], "put", [3, 7], "get", [1], "get", [2], "get", [3], "get", [4], "get", [5], "get", [2], "get", [3], "get", [4], "put", [1,9], "put", [6,6], "get", [1], "get", [2], "get", [3], "get", [4], "get", [5], "get", [6]]

lru_cache = LRUCache(3)
for i in range(0, len(ip_commands), 2):
    print(ip_commands[i], ip_commands[i+1])
    if ip_commands[i]=="put":
        lru_cache.put(ip_commands[i+1][0], ip_commands[i+1][1])
    else:
        get_op = lru_cache.get(ip_commands[i+1][0])
        print(f"Get O/P is: {get_op}")
        if get_op==8:
            break
    print("-------------------")

# More cleaner version!
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
