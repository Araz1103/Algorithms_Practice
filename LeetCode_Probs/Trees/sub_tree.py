"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [1,2,3,4,5], subRoot = [2,4,5]
Output: true

Example 2:
Input:root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
Output: false

Constraints:

0 <= The number of nodes in both trees <= 100.
-100 <= root.val, subRoot.val <= 100
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

# TC: For every node in Main Tree, we have to traverse it, and compare with the subroot tree
# So for n nodes in main tree and m nodes in subtree
# O(m*n)

# Space Complexity:
# Recursion Stack for each traversal is O(log(N)) for a balanced tree
# But worst case: O(N)

"""
Time Complexity:
    O(n * m)
    - For each of the n nodes in the main tree (`root`), we may compare it to the m-node `subRoot`.
    - Each tree comparison (same_tree) is a DFS that takes O(m) time in the worst case.
    - Hence, total time complexity is O(n * m).

Space Complexity:
    O(n + m)
    - O(n): In the worst case, `check_all_nodes` traverses the entire depth of the main tree (e.g., a skewed tree), 
            and each recursive call adds to the call stack.
    - O(m): During a same_tree comparison, we do a DFS on the subRoot and the corresponding subtree from root, 
            adding up to m calls on the stack.

    🔍 Why space is not O(n * m):
    - Although we perform up to n comparisons (one per node in the main tree), 
      only **one** comparison (`same_tree`) is active at a time.
    - The recursion stacks for `check_all_nodes` and `same_tree` are **nested**, not parallel.
      So the deepest possible call stack is the sum of both: O(n + m), not their product.

    For balanced trees:
    - h1 = O(log n), h2 = O(log m) → space = O(log n + log m)
"""

class Solution:   
    def same_tree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        def dfs(curr_node1, curr_node2):
            if not curr_node1 and not curr_node2:
                return True

            if curr_node1 and curr_node2 and curr_node1.val==curr_node2.val:
                if dfs(curr_node1.left, curr_node2.left) and dfs(curr_node1.right, curr_node2.right):
                    return True
                else:
                    return False
            else:
                return False

        return dfs(t1, t2)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # @every node in root tree, compare if that tree is equal to tree @subroot 
        is_present = [0]
        def check_all_nodes(curr_node):
            if not curr_node:
                if not subRoot:
                    is_present[0] = 1
                return 

            if self.same_tree(curr_node, subRoot):
                is_present[0] = 1
                return
            
            # Check Left and Right Children
            if check_all_nodes(curr_node.left):
                is_present[0] = 1
                return

            if check_all_nodes(curr_node.right):
                is_present[0] = 1
                return

            return 

        check_all_nodes(root)
        return bool(is_present[0])