"""
Lowest Common Ancestor in Binary Search Tree

Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, 
return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. 
The ancestor is allowed to be a descendant of itself.

Example 1:
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
Output: 5

Example 2:
Input root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
Output: 3
Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.

Constraints:
2 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
p != q
p and q will both exist in the BST.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time Complexity:
# Traversing Height of the Tree @max
# So O(log(N)) for balanced tree and O(N) for skewed tree
# Space Complexity:
# Recursion Call Stack: O(Log(N)) for balanced and O(N) for skewed

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 3 cases
        # Ist: Given the root, both nodes lie in different sub trees, then root is LCA
        # root < a and root > b OR root > a and root < b

        # IInd: Given the root, both nodes lie in the same sub tree
        # Then we have to shift root to go to that sub tree and check
        # root < a and root < b OR root > a and root > b

        # IIIrd: Given the root, one of the nodes is the root itself
        # Then that node is the LCA
        # We know both can't be equal to the root, since p!=q given
        # root==a OR root==b
        p_val = p.val
        q_val = q.val

        def check_lca(curr_node):
            if not curr_node:
                return None #Ideally cannot happen, unless p and q not in tree, but given that they are

            # Ist
            root_val = curr_node.val
            if (root_val > p_val and root_val < q_val) or (root_val < p_val and root_val > q_val):
                return curr_node #Is LCA

            # IInd
            if (root_val > p_val and root_val > q_val):
                # LCA lies in LST
                return check_lca(curr_node.left)

            if (root_val < p_val and root_val < q_val):
                # LCA lies in RST
                return check_lca(curr_node.right)

            # IIIrd
            if root_val==p_val:
                return curr_node

            if root_val==q_val:
                return curr_node

        return check_lca(root)
    
# If not a BST, we have to use Post Order DFS!
class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        """
        General LCA solution for any binary tree (not necessarily a Binary Search Tree).
        
        The idea is to use a **post-order traversal** to find the **Lowest Common Ancestor (LCA)** of two nodes `p` and `q`.
        The algorithm works as follows:
        
        1. If the current node is `None`, we return `None` (this happens when we hit a leaf node or the end of a branch).
        2. If the current node is either `p` or `q`, return the current node (this is a base case, since if we find either node, we want to return it).
        3. Recursively search the left and right subtrees.
        4. If both left and right subtrees return non-`None` values, the current node is the **LCA** because `p` is in one subtree and `q` is in the other.
        5. If only one side returns a non-`None` value, that side contains both nodes or one of the nodes, so we propagate that side's result.

        **Example 1:**
        Given the following tree:
        
                    3
                   / \
                  5   1
                 / \   \
                6   2   8
                   / \
                  7   4
                 
        Input: `root = [3,5,1,6,2,8,null,null,7,4]`, `p = 5`, `q = 1`
        
        The LCA of nodes `5` and `1` is `3`, because `p` is on the left subtree and `q` is on the right subtree of `3`.

        Output: `3`
        
        **Example 2:**
        Input: `root = [3,5,1,6,2,8,null,null,7,4]`, `p = 5`, `q = 4`
        
        The LCA of nodes `5` and `4` is `5`, because `p` is the ancestor of `q`, i.e., `5` is the LCA of `5` and `4`.

        Output: `5`
        
        **Example 3:**
        Input: `root = [3,5,1,6,2,8,null,null,7,4]`, `p = 6`, `q = 8`
        
        The LCA of nodes `6` and `8` is `3`, because both nodes are in different subtrees of `3`.
        
        Output: `3`
        
        **Time Complexity:**
        - The algorithm visits each node at most once. Since there are `N` nodes in the tree, the time complexity is `O(N)`, where `N` is the number of nodes in the tree.

        **Space Complexity:**
        - The space complexity is determined by the depth of the recursion stack. In the worst case, for a skewed tree, the space complexity is `O(N)`. For a balanced tree, the space complexity is `O(H)`, where `H` is the height of the tree.

        **Steps Involved:**
        1. **Base Case 1:** If `root` is `None`, return `None` because there's no ancestor to find.
        2. **Base Case 2:** If `root` is equal to `p` or `q`, return `root` because we have found one of the target nodes.
        3. Recursively find the LCA in the left subtree (`left = lowestCommonAncestor(root.left, p, q)`).
        4. Recursively find the LCA in the right subtree (`right = lowestCommonAncestor(root.right, p, q)`).
        5. If both `left` and `right` are non-`None`, then `root` is the LCA, because one node is found in the left subtree and the other node is found in the right subtree.
        6. If only one of `left` or `right` is non-`None`, return that non-`None` child because both nodes are either in the same subtree, or one of the nodes is at the current `root`.
        """
        if not root or root == p or root == q:
            return root  # Found one of the nodes, or reached a leaf

        # Recursively find the LCA in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right subtrees have the nodes, the current node is the LCA
        if left and right:
            return root

        # Otherwise, return whichever side is non-None
        return left if left else right










        