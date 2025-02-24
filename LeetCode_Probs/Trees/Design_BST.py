from typing import Optional, List

class TreeNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None
        
    def insert(self, key: int, val: int) -> None:
        def insert_element(root, key, val):
            if not root:
                # Make a New Node and Return that
                return TreeNode(key, val)

            if key == root.key:
                # Update Root's Value
                root.val = val
                return root

            elif key > root.key:
                # Go to the Right
                root.right = insert_element(root.right, key, val)
            else:
                # Go to the Left
                root.left = insert_element(root.left, key, val)

            return root

        # Check if root is empty, assign to that
        if not self.root:
            self.root = TreeNode(key, val)
            return
        
        # Find where to insert
        insert_element(self.root, key, val)


    def get(self, key: int) -> int:

        def check_element(root, key):
            if not root:
                return -1 #No More Nodes to Check

            if key==root.key:
                return root.val

            elif key > root.key:
                # Check @RST
                return check_element(root.right, key)

            else:
                # Check @LST
                return check_element(root.left, key)

        return check_element(self.root, key)


    def getMin(self) -> int:
        # Check if root is empty, return -1
        if not self.root:
            return -1
        
        curr_node = self.root
        while True:
            if curr_node.left:
                # If left exists, check that
                # As min is leftmost node of Tree
                curr_node = curr_node.left
            else:
                return curr_node.val
            
    def getMax(self) -> int:
        # Check if root is empty, return -1
        if not self.root:
            return -1
        
        curr_node = self.root
        while True:
            if curr_node.right:
                # If right exists, check that
                # As max is rightmost node of Tree
                curr_node = curr_node.right
            else:
                return curr_node.val


    def remove(self, key: int) -> None:

        # CASE I: Removing a Node with 0 or 1 Children
        # We can just assign the child to the above parent

        # CASE II: Removing a Node with 2 children
        # Find the minimum @RST
        # Replace the val of the node to be removed with Min
        # Remove the Minimum Node

        def get_min_from_root(root):
            # Get min node from this root
            curr_node = root
            while True:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    return curr_node

        def remove_element(root, key):

            if not root:
                return None # Key not in Tree
            
            if key == root.key:
                # Removing here
                # Check CASE I
                # If 0 or 1 child
                # We return the other child to the parent
                if not root.left:
                    return root.right
                
                if not root.right:
                    return root.left
                
                # CASE II
                # Get Minimum from RST (Right Sub Tree)
                # We know since both children, RST Exists
                min_node = get_min_from_root(root.right)
                # Swap the node to remove's key & value from min_node
                root.key = min_node.key
                root.val = min_node.val

                # Remove min node from RST
                root.right = remove_element(root.right, min_node.key)
                return root

            elif key > root.key:
                # Check on the right
                root.right = remove_element(root.right, key)
            else:
                # Check on the left
                root.left = remove_element(root.left, key)

            return root
        
        # The new root of the Tree
        self.root = remove_element(self.root, key)


    def getInorderKeys(self) -> List[int]:
        # LST -> Root -> RST
        def dfs(root):
            keys = []
            if not root:
                return []
            
            keys.extend(dfs(root.left))
            keys.append(root.key)
            keys.extend(dfs(root.right))
            return keys
        
        return dfs(self.root)
