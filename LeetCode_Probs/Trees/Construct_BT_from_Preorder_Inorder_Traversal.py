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
    
# Shorten the code
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

        # If preorder or inorder list empty, return None, as we know that previous must point to None
        if not preorder or not inorder:
            return None
        
        print("INORDER", inorder)
        print("PREORDER", preorder)
        root = TreeNode(preorder[0])
        print("ROOT", root.val)

        # Get Root Index @Inorder
        root_index = inorder.index(root.val)

        # left_inorder
        left_inorder = inorder[:root_index]
        # right_inorder
        right_inorder = inorder[(root_index + 1):]

        # left pre-order
        # Num elements in left inorder post root
        # Num elements is equal to (root index)
        # Start from 1 @preorder, to skip root
        left_preorder = preorder[1:(root_index+1)]
        right_preorder = preorder[(1+root_index):]
        
        root.left = self.buildTree(left_preorder, left_inorder) # Pass in the List of LST and It's Pre-Order & In-Order
        root.right = self.buildTree(right_preorder, right_inorder) # Pass in the List of RST and It's Pre-Order & In-Order
        
        return root
    
# Solving in O(N)
# 
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Constructs a binary tree from preorder and inorder traversal lists.
        
        :param preorder: List[int] - Preorder traversal of the tree (Root -> Left -> Right)
        :param inorder: List[int] - Inorder traversal of the tree (Left -> Root -> Right)
        :return: Optional[TreeNode] - Root of the reconstructed binary tree
        """
        
        # Dictionary to store index positions of inorder values for O(1) lookups
        indices = {val: idx for idx, val in enumerate(inorder)}
        
        # Preorder index to track which element is the current root
        self.pre_idx = 0
        
        def dfs(l: int, r: int) -> Optional[TreeNode]:
            """
            Recursively constructs the binary tree.
            
            :param l: int - Left boundary of the inorder traversal range
            :param r: int - Right boundary of the inorder traversal range
            :return: Optional[TreeNode] - Constructed subtree root
            """
            
            # Base Case: If the left boundary surpasses the right, no elements exist
            if l > r:
                return None  # No subtree to construct

            # Select the current root from preorder traversal
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1  # Move to the next element in preorder
            root = TreeNode(root_val)  # Create the root node
            
            # Find the root in inorder traversal to divide left and right subtrees
            mid = indices[root_val]
            
            # Recursively build left and right subtrees
            root.left = dfs(l, mid - 1)  # Elements before `mid` are in the left subtree
            root.right = dfs(mid + 1, r)  # Elements after `mid` are in the right subtree
            
            return root  # Return the constructed subtree
        
        # Call DFS on the full inorder range
        return dfs(0, len(inorder) - 1)
        