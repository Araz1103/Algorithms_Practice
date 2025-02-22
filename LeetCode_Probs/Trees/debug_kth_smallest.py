from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = None

        def dfs(node, depth=0):
            nonlocal cnt, res
            if not node:
                return
            
            print("  " * depth + f"Entering node {node.val} with cnt = {cnt}")
            
            dfs(node.left, depth + 1)  # Explore left subtree

            if cnt == 0:  # Stop after finding the result
                return
            
            cnt -= 1  # Process current node
            print("  " * depth + f"Visiting node {node.val}, cnt now = {cnt}")
            
            if cnt == 0:
                res = node.val
                print("  " * depth + f"Found kth smallest: {res}, stopping recursion!")
                return  # EARLY STOP
            
            dfs(node.right, depth + 1)  # Explore right subtree
            print("  " * depth + f"Exiting node {node.val} with cnt = {cnt}")
        
        dfs(root)
        return res

# Helper function to build BST
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Construct BST
root = None
elements = [5, 3, 8, 2, 4, 9, 1]  # BST Elements
for el in elements:
    root = insert(root, el)

# Find kth smallest
k = 5
solution = Solution()
kth_smallest = solution.kthSmallest(root, k)
print(f"\n{k}th smallest element: {kth_smallest}")
