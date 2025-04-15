"""
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [4,7], q = [4,null,7]
Output: false

Example 3:
Input: p = [1,2,3], q = [1,3,2]
Output: false

Constraints:

0 <= The number of nodes in both trees <= 100.
-100 <= Node.val <= 100
"""
# Time Complexity is O(N) as we have to traverse nodes of both trees
# Space is Height of the Longer Tree for Recursion Call Stack
# For balanced tree: O(log(N))

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def is_same_tree(p: Optional[TreeNode], q:Optional[TreeNode]) -> bool:

    def dfs(curr_node1, curr_node2):

        if not curr_node1 and not curr_node2:
            return True #This is ok, as both empty
        
        if curr_node1 and curr_node2 and curr_node1.val==curr_node2.val: #Both must exist and have same value
            # Check with their left and right sub trees
            # Must get true for both, otherwise we know they are not equal
            if dfs(curr_node1.left, curr_node2.left) and dfs(curr_node1.right, curr_node2.right):
                return True
            else:
                return False
        else:
            return False 
        
    return dfs(p, q)