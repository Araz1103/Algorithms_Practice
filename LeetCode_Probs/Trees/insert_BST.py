# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Inserting @Leaf Nodes
# If BST is balanced, then again approx half nodes skipped every turn to find where to insert
# Therefore insertion is O(LogN)
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        # We first do a BST for the node to insert
        # When we reach the node post which it is null
        # We attach that to the parent we came from
        
        # Handle if 0 nodes case
        if root is None:
            return TreeNode(val)
        
        # Now we know at least 1 node is there
        parent = root
        current_node = root
        direction = None
        while current_node!=None:
            parent = current_node
            if val > current_node.val:
                # We need to go to Right
                direction = "r"
                current_node = current_node.right
            else:
                # We need to go to Left
                direction = "l"
                current_node = current_node.left
        
        # Attach a new node to the parent @direction
        if direction=="l":
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root
        