def inorder(root): # L -> Root -> R
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root): # Root -> L -> R
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root): # L -> R -> Root
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeTraversal:
    def __init__(self):
        self.result = []

    # ------------------------
    # 🟩 1. INORDER TRAVERSAL
    # Order: LEFT → NODE → RIGHT
    # BST: This gives sorted order of elements
    # ------------------------

    def inorder_recursive(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.result.append(node.val)
            dfs(node.right)
        
        self.result = []
        dfs(root)
        return self.result

    def inorder_iterative(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result

    # ------------------------
    # 🟨 2. PREORDER TRAVERSAL
    # Order: NODE → LEFT → RIGHT
    # Use: Tree cloning, building expression trees
    # ------------------------

    def preorder_recursive(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return
            self.result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        self.result = []
        dfs(root)
        return self.result

    def preorder_iterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)
            # Push right first, so left is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    # ------------------------
    # 🟥 3. POSTORDER TRAVERSAL
    # Order: LEFT → RIGHT → NODE
    # Use: Tree deletion or expression evaluation
    # ------------------------

    def postorder_recursive(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            self.result.append(node.val)
        
        self.result = []
        dfs(root)
        return self.result

    def postorder_iterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack1 = [root]
        stack2 = []
        
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            # Push children to first stack
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        # Now process from second stack
        return [node.val for node in reversed(stack2)]

