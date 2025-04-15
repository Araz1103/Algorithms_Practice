"""
Note on Using In-Order Traversal for Serialization/Deserialization:

In-order traversal visits nodes in the order: Left, Root, Right.
One might consider using in-order traversal with explicit null markers 
(e.g., "N" for None) to serialize a binary tree. However, in-order alone is 
not sufficient to uniquely reconstruct a tree because the position of the root 
is ambiguous without additional information.

Consider the following two different trees:

Tree A:
      1
     /
    2

Tree B:
      2
       \
        1

If we perform in-order traversal on both trees and include null markers, we get:

For Tree A:
1. Traverse left of node 1:  
   - Visit node 2:  
     * Left of 2 → None, record "N"
     * Then node 2 → "2"
     * Right of 2 → None, record "N"
2. Then visit node 1 → "1"
3. Traverse right of node 1 → None, record "N"

Overall, Tree A in-order serialization: "N,2,N,1,N"

For Tree B:
1. Traverse left of node 2 → None, record "N"
2. Visit node 2 → "2"
3. Traverse right of node 2:
   - Visit node 1:
     * Left of 1 → None, record "N"
     * Then node 1 → "1"
     * Right of 1 → None, record "N"

Overall, Tree B in-order serialization: "N,2,N,1,N"

Both trees produce the **exact same in-order traversal** ("N,2,N,1,N"), 
even though they are structurally different. This ambiguity occurs because 
in-order does not provide a clear, fixed position (like first or last) for the 
root node, making it impossible to uniquely partition the serialized string 
into left and right subtrees during deserialization.

In contrast, pre-order (Root, Left, Right) and post-order (Left, Right, Root) 
traversals include the root at a known position (first for pre-order, last for 
post-order), which, when combined with null markers, allows for unambiguous 
serialization and deserialization.

References:
- Baeldung, "Binary Tree Serialization & Deserialization", https://www.baeldung.com/cs/binary-tree-serialize-deserialize

Thus, while in-order traversal with null markers might seem to encode the complete 
structure, its inherent ambiguity in identifying the root makes it unsuitable on its own 
for the serialization and deserialization of binary trees.

Serialization of Binary Trees with Null Markers (Pre/Post Order)

When serializing a binary tree using DFS traversal (pre-order or post-order),
we often include explicit null markers (e.g., "N") to denote absent children.
This ensures that we preserve the structure of the tree exactly and can
deserialize it unambiguously.

One key observation is:
    ✅ A binary tree with `N` nodes will always have `N + 1` null children.

Why?

Each node in a binary tree has two child pointers: left and right.
So for `N` nodes, there are `2N` total child pointers.

Out of these:
- `N - 1` pointers are non-null (since there are `N - 1` edges in any connected tree)
- The remaining `2N - (N - 1) = N + 1` pointers must be null

Thus, the number of "null" markers you'll need to serialize a binary tree with `N` nodes is exactly `N + 1`.

➡️ This means the serialized representation will have:
    - `N` actual values (node values)
    - `N + 1` "N" null markers
    = Total of `2N + 1` items

Example:

        1
       / \
      2   3
         /
        4

Pre-order Serialization with null markers:  
    ["1", "2", "N", "N", "3", "4", "N", "N", "N"]

Breakdown:
- Nodes = 4
- Nulls = 5 → 4 (nodes) + 1 = N + 1

This property guarantees that a binary tree can be fully reconstructed using
pre-order or post-order DFS traversal with nulls.
"""

# TC: O(N) -> Visiting every node once and all null nodes: 2*N + 1 -> O(N)
# SC: O(h)
from typing import Optional

# With Post-Order

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Using PostOrder (L->Right->Root)
        ser_array = []
        def dfs(curr_node):
            if not curr_node:
                ser_array.append("N")
                return
            dfs(curr_node.left)
            dfs(curr_node.right)
            ser_array.append(str(curr_node.val))
            return
        dfs(root)
        return ",".join(ser_array)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Now deserialize with PostOrder itself
        ser_array = data.split(",")
        # Starting from end, as post order in reverse is root -> right -> left
        self.index_pointer = len(ser_array)-1 #Telling where we are in our postorder
        def dfs():
            if ser_array[self.index_pointer]=="N":
                self.index_pointer-=1
                return None
            node = TreeNode(int(ser_array[self.index_pointer]))
            self.index_pointer-=1
            # Post-Order in Reverse is: Root -> Right -> Left
            # Right
            node.right = dfs()
            # Left
            node.left = dfs()
            return node
        return dfs()

# With Pre-Order
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
