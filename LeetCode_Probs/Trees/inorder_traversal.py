"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# InOrder is Left to Right
# First Left Sub Tree
# Then Root
# Then Right Sub Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Solution
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        op = []
        if not root:
            return []
        op.extend(self.inorderTraversal(root.left))
        op.append(root.val)
        op.extend(self.inorderTraversal(root.right))
        return op
    
# Recursive Solution
# List passed as param
class Solution(object):
    def inorderTraversal(self, root, result=[]):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Since list is mutable, once passed to the function
        # Keeps adding whenever finds a root
        # Rest helps it go in the right Traversal
        if not root:
            self.inorderTraversal(root.left, result)
            result.append(root.val)
            self.inorderTraversal(root.right, result)
    
# Iterative Solution
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Using a Stack
        # Last in First Out
        stack = []
        op = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            # If current is None, this means no left child
            # Pop Top Element (Last one, who's left child is None)
            # This is new current
            # pop default is last element
            current = stack.pop()
            op.append(current.val)
            current = current.right

        return op
                

