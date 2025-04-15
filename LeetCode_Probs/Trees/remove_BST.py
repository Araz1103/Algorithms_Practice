# First Finding the Min of a BST
# Like a Sorted Array
# [a, b, c ........ z]
# Leftmost is min and Rightmost is max
# So if we keep going to the Left, will reach min

def findMinBST(root):
    curr_node = root
    while curr_node and curr_node.left:
        # If node doesn't exist or doesn't have a left val
        # Then that is the minimum
        curr_node = curr_node.left # Go the left, as we know it exists
    
    return curr_node #Will either be min or None if root itself is None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time and Space Complexity: O(log(N)) for Balanced Tree
# O(N) worst case for skewed tree
# Space is number of recursion stack calls, equal to height of the tree
class Solution(object):
    def findMinNode(self, root):
        curr_node = root
        while curr_node and curr_node.left:
            curr_node = curr_node.left
        return curr_node

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """

        # If root doesn't exist
        if not root:
            return None
        
        if key > root.val:
            # Go to the Right
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # Go to the Left
            root.left = self.deleteNode(root.left, key)
        else:
            # If we found Key
            if not root.left:
                # This means 1 child doesn't exist
                # Return other child
                # If other child is None, that is ok too, as in CASE I we return child
                return root.right
            elif not root.right:
                return root.left
            else:
                # CASE II
                # First find min element on Right Sub Tree
                minNode = self.findMinNode(root.right)
                # Put the min's value @node to delete (current root)
                root.val = minNode.val
                # Now we remove the minimum node
                # And assign to root.right as change in Right Sub Tree
                root.right = self.deleteNode(root.right, minNode.val)
        return root