"""
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [1,2,3]
Output: false

Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.

Constraints:

1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""
"""
# Remember, the edge case
# root has to be greater than all nodes in the BST
# So below is not a valid BST
# As 3 < 5!

        5
       / \
      4   6
           / \
          3   7

"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
# TC: O(N), checking each node once
# SC: O(h), h is height of tree for recursion call stack
Space Complexity:
        - O(H): H is the height of the tree due to the recursion stack.
          This is because recursive DFS uses the call stack to remember each node's state until the subtree is processed.

        Why is space = height?
        -----------------------
        For recursive DFS, each level of depth adds one call to the stack.
        Example (skewed tree):

                5
               /
              4
             /
            3

        - Call stack grows like: dfs(5) → dfs(4) → dfs(3)
        - So the max depth of recursion = tree height.
        - Balanced tree ⇒ O(log N)
        - Skewed tree ⇒ O(N)
"""
class Solution:
    # Root can be between -inf and +inf
    # Left child has to be -inf and root val
    # Right child has to be root and + inf
    # Then for each child, get the interval from the parent
    # Right child of above: root.right and +inf
    # Left child of above: root and root.right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr_node, left_interval, right_interval):
            if not curr_node:
                return True #Ok to be empty, valid tree

            if curr_node.val > left_interval and curr_node.val < right_interval:
                # Now check for each child, and update interval accordingly
                # for left child, it needs to be less than the curr node
                # for right child, it needs to be greater than the curr node
                if dfs(curr_node.left, left_interval, curr_node.val) and dfs(curr_node.right, curr_node.val, right_interval):
                    return True
                else:
                    return False
            else:
                return False 
            
        # root can be between -inf and +inf
        return dfs(root, float("-inf"), float("inf"))
