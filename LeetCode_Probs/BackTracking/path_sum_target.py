"""
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        def check_valid_path(root, path_sum):
            if not root:
                return False

            path_sum += root.val
            # If at leaf Node
            if (not root.left and not root.right):
                if path_sum == targetSum:
                    return True # Found a valid path
                else:
                    return False #Reached Leaf but not equal to Target

            if check_valid_path(root.left, path_sum):
                return True #Found a valid path in RST
            
            if check_valid_path(root.right, path_sum):
                return True #Found a valid path in LST

            # If till now didn't return, this means no path from this node onwards
            path_sum -= root.val #reset to backtrack to previous node
            return False

        if check_valid_path(root, 0):
            return True
        else:
            return False

            
        
        
        