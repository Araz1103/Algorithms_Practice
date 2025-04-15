"""
Binary Tree Maximum Path Sum

Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. 
A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-15,10,20,null,null,15,5,-5]
Output: 40
Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.

Constraints:
1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Basically @each node
    # The max can be using a split: including this node and the ones on left and right
    # or it can be going on either paths
    # But we can overall only split once
    # So we handle that
    # Also for negatives, 
    # we hande that if sum returned from left and right is negative, 
    # then can we just take the node itself

    # TC: Checking all nodes once: O(N)
    # SC: Height of Tree for recursion: O(h), balanced: log(N), skewed N
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # return max path sum without split
        # as we compute split to update max, but cannot use it
        res = [root.val] #to store max path sum and update

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # If we got negative values from both, making them 0, so we only take node value
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum with split, to udpate our global max
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # But we return without split, so can only include one of the values from left or right and node sum
            # So we take max
            # That's why if leftMax and rightMax were -ve, we made 0, so only taking curr root value
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0] #should contain max path sum overall