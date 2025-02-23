# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output_list = []

        queue = deque()

        if root:
            queue.append(root)

        while queue:
            level_list = []
            for i in range(len(queue)):
                curr_node = queue.popleft()
                level_list.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)
            output_list.append(level_list)

        return output_list
        