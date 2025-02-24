class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""
Given a binary tree, we want to determine if there exists a path from the root to a leaf node 
without having a value of 0 in the path. 
If such a path exists, we return true, otherwise we return false.
"""
def canReachLeaf(root):
    if not root or root.val == 0:
        return False
    
    if not root.left and not root.right:
        return True
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    return False

"""
Given a binary tree, we want to determine if there exists a path from the root to a leaf node 
without having a value of 0 in the path. 
If such a path exists, we want the path now.
The path should contain the values of the root to leaf path in the order they are visited.
"""

def leafPath(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)

    if not root.left and not root.right:
        return True
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop()
    return False
