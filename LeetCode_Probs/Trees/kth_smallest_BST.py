"""
Kth Smallest Integer in BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
Example 1:

Input: root = [2,1,3], k = 1

Output: 1

Ex2:
Input: root = [4,3,5,2,null], k = 4

Output: 5

Constraints:

1 <= k <= The number of nodes in the tree <= 1000.
0 <= Node.val <= 1000

"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My intuition
# Naive approach: Do Full Inorder, and store in a list
# Return kth element from list

# Optimise it further
# We do an inorder travseral -> Leads to sorted array
# We stop inorder once we reach K
# As that element will be Kth smallest
# So do not do a full inorder traversal
# Will need to use Stack, so can stop then

# Try with Recursion too!

# I: Stack
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count_element = 0
        stack = []
        curr_node = root

        while curr_node or stack:
            while curr_node: #Keep traversing until no more @left, and add those in stack
                stack.append(curr_node)
                curr_node = curr_node.left

            # If breaks, this means that the top of stack has no left children
            # Pop the stack to return top (as LST -> Root -> RST)
            top_element = stack.pop()
            count_element += 1
            # If count is K, this is our Kth smallest
            if count_element == k:
                return top_element.val
            
            # Now Root done, we want to go down RST
            curr_node = top_element.right

        # Stack should be empty now

# II: Recursion
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val

        def dfs(node):
            nonlocal cnt,res #Take from outer namespace
            if not node:
                return
            
            dfs(node.left)
            if cnt==0:
                return # Can stop unnecessary recursion calls!
            cnt-=1 #We keep decrementing everytime we reach a min node
            if cnt == 0:
                res = node.val # The current node here is Kth smallest
                return #Skips the right traversal #So now backtracks back
            dfs(node.right)

        return res 