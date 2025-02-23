"""
You are given the root of a binary tree. 
Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Input: root = [1,2,3]

Output: [1,3]

Input: root = [1,2,3,4,5,6,7]

Output: [1,3,7]

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from collections import deque

# Intution: Do Level Order Traversal from R t L
# Store the first @each level, that's the view

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        queue = deque()

        if root:
            queue.append(root)
        else:
            return []
        
        while queue:
            for i in range(len(queue)):
                curr_node = queue.popleft()
                if i == 0: # Since we only want first from Right @each level
                    right_view.append(curr_node.val)
                # Add Children @queue if they exist
                if curr_node.right:
                    queue.append(curr_node.right)
                if curr_node.left:
                    queue.append(curr_node.left)
        return right_view
                    

        