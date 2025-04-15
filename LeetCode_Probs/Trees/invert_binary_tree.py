from typing import Optional
"""
You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,3,2,7,6,5,4]

Example 2:
Input: root = [3,2,1]
Output: [3,1,2]

Example 3:
Input: root = []
Output: []

Constraints:

0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursively keep going and swap left and right children

        def dfs(curr_node):
            if not curr_node:
                return
            lst = curr_node.left
            rst = curr_node.right
            curr_node.right = lst
            curr_node.left = rst
            dfs(curr_node.left)
            dfs(curr_node.right)
            return
        dfs(root)
        return root