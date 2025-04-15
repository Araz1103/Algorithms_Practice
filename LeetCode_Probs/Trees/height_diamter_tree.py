from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(node):
    if node is None:
        return -1  # An empty tree has height -1
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1 #+1 for the current node
    
# Above runs in O(N) as visits all nodes exactly once
# Height of just one node is 0 (example: Tree with just root)
# The height of a BST is defined as the number of edges on the longest path from the root node to a leaf node.

# Diameter of BST: 
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0] #So we can modify inside height function
        def get_height(curr_node):
            if not curr_node:
                return -1 #Height of an Empty Node is -1

            left_sub_tree_height = get_height(curr_node.left)
            right_sub_tree_height = get_height(curr_node.right)

            # Diamter is LST Height + RST Height + 2 (for 2 edges connecting to each L & R Node)
            curr_diameter = left_sub_tree_height + right_sub_tree_height + 2
            
            # Update for Max Diameter
            diameter[0] = max(diameter[0], curr_diameter)

            # Return Height at this node
            # Max of Left Height & Right Height + 1 for the current node
            return max(left_sub_tree_height, right_sub_tree_height) + 1

        get_height(root)
        return diameter[0]


        