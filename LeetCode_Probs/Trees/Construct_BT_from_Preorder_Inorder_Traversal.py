"""
Construct Binary Tree from Preorder and Inorder Traversal
You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:

Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

Output: [1,2,3,null,null,null,4]

Example 2:

Input: preorder = [1], inorder = [1]

Output: [1]

Constraints:

1 <= inorder.length <= 1000.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # LST: Left Sub Tree
        # RST: Right Sub Tree
        # Basically from the pre-order and in-order get Root, LST and RST
        # Keep doing until we have one of LST and RST empty, and a single node in the Sub Tree(s)
        # Or both LST and RST both empty
        # Intuition: Pre-Order tells us first element in it is the root
        # Inorder divides from the Root into LST and RST
        # So we can recursively, for each Sub Tree find the root and LST and RST
        # And Assign accordingly!
        
        print("INORDER", inorder)
        print("PREORDER", preorder)
        root = TreeNode(preorder[0])
        print("ROOT", root.val)

        # Get In-Orders for LST and RST
        left_inorder = []
        right_inorder = []
        found_root = False
        for element in inorder:
            #print(element)
            if not found_root and element != root.val: # Until then we will have LST
                #print("Found for LI")
                left_inorder.append(element)
                #print("LI", left_inorder)
            elif element == root.val:
                print("Found Root!")
                found_root = True
            elif found_root and element != root.val: # Now we have RST
                #print("Found for RI")
                right_inorder.append(element)
                #print("RI", right_inorder)

        # Get Pre-Orders for LST and RST
        left_preorder = []
        right_preorder = []
        for element in preorder[1:]: # All elements post root
            if element in left_inorder:
                left_preorder.append(element)
            else:
                right_preorder.append(element)

        print("LEFT", left_inorder, left_preorder)
        print("RIGHT", right_inorder, right_preorder)
        # If len of pre-order and inorder is 1 or 0, assign
        # Else need to build the Tree
        if len(left_inorder)==1:
            root.left = TreeNode(left_inorder[0])
        elif len(left_inorder)==0:
            root.left = None
        else:
            root.left = self.buildTree(left_preorder, left_inorder) # Pass in the List of LST and It's Pre-Order & In-Order
        
        if len(right_inorder)==1:
            root.right = TreeNode(right_inorder[0])
        elif len(right_inorder)==0:
            root.right = None
        else:
            root.right = self.buildTree(right_preorder, right_inorder) # Pass in the List of RST and It's Pre-Order & In-Order
        
        return root
        
        