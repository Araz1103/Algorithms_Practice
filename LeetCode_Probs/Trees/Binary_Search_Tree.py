# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        # Keep Checking until we reach root as null
        # This means that target not in Tree
        found = None
        while root!=None:
            if val == root.val:
                found = root
                break
            elif val > root.val:
                # Go to the Right Tree
                root = root.right
            else:
                # Go the Left Tree
                root = root.left

        return found
    
def BST_Recursive(root, target):
    if root is None:
        return False # No more possibilities to search
    
    if target > root.val:
       return BST_Recursive(root.right, target)
    
    elif target < root.val:
        return BST_Recursive(root.left, target)
    
    else:
        return True # If Equal

# Time Complexity is O(Log(N)) to Search*
# *: If the BST is Balanced, otherwise we are not eliminating half @each turn
# Balanced Property: Height of Left BST and Right BST only differ by 1 @max
# Also if balaned, height of overall tree is roughly Log(N) (As @each level, approx 2x nodes)
# We prefer BST to Sorted Arrays, as in Arrays Insertion and Deletion is O(N)
# In a balanced BST, Insertion and Deletion is O(Log(N))
        