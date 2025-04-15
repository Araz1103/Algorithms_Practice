"""
Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:
Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]
Output: ["cat","back","backend"]

Example 2:
Input:
board = [
  ["x","o"],
  ["x","o"]
],
words = ["xoxo"]
Output: []

Constraints:

1 <= board.length, board[i].length <= 10
board[i] consists only of lowercase English letter.
1 <= words.length <= 100
1 <= words[i].length <= 10
words[i] consists only of lowercase English letters.
All strings within words are distinct.
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Given a 2D board and a list of words from the dictionary, finds all words 
        that can be constructed from letters of sequentially adjacent cells, 
        where "adjacent" cells are horizontally or vertically neighboring. 
        The same letter cell may not be used more than once in a word.

        Approach:
        - We build a Trie (prefix tree) from the input list of words.
        - We then perform DFS starting from each cell in the board.
        - At each DFS step, we check if the current path exists in the Trie.
        - This helps prune invalid paths early, improving performance.
        - If a Trie node marks the end of a word, we add it to the results.
        - We use backtracking (DFS + visited set) to explore paths and revert changes after exploring a branch.

        Time Complexity:
        Let:
        - R = number of rows in board
        - C = number of columns in board
        - W = maximum length of a word
        - L = total number of characters in all words (i.e., sum(len(w) for w in words))

        1. Building the Trie: O(L)
        2. DFS Traversal:
            - We can start DFS from each cell: R × C
            - At each DFS, in the worst case we branch up to 3 directions (after the first move),
              and the depth is at most W (max word length).
            - So DFS per cell is O(3^W)
        Therefore, total DFS cost: O(R × C × 3^W)

        Total Time Complexity: O(L + R × C × 3^W)

        Space Complexity:
        - Trie requires O(L) space to store all characters in the words.
        - Recursion call stack, visited set, and current character path can go up to W in size.
        
        Total Space Complexity: O(L + W)

        Returns:
            A list of unique words from the given list that can be formed in the board.
        """
        class TrieNode:
            def __init__(self):
                self.is_word = False
                self.children = {}

        # First let's create a Trie from the words given
        trie_root = TrieNode()

        def print_trie(root):
            print("Node Children", root.children.keys())
            print(f"Is word: {root.is_word}")
            for child in root.children:
                print(f"In Child: {child}")
                print_trie(root.children[child])

        def insert_word(root, word):
            curr_node = root
            for char in word:
                if char not in curr_node.children:
                    curr_node.children[char] = TrieNode()
                curr_node = curr_node.children[char]
            curr_node.is_word = True

        for word in words:
            insert_word(trie_root, word)

        #print_trie(trie_root)

        # Now when we do DFS on the grid
        # We pass in the current node in the trie we are at
        # So when searching the neighbours, if neighbour not in the children of trie node
        # We know that wouldn't lead to matches
        # Also if word present at that cell, we can store the word till here for output
        found_words = []
        directions = [
            [0, 1], #Right
            [0, -1],#Left
            [1, 0], #Down
            [-1, 0] #Up
        ]

        R = len(board)
        C = len(board[0])

        def dfs(curr_row, curr_col, curr_node, curr_char_list, visited_set):
            if curr_node.is_word:
                # Found word
                word = "".join(curr_char_list)
                if word not in found_words: # To avoid duplicates in found_words
                    found_words.append(word)

            # Explore neighbours
            for dr, dc in directions:
                new_row = curr_row + dr
                new_col = curr_col + dc

                # Check out of bounds
                if min(new_row, new_col) >= 0 and new_row < R and new_col < C:
                    # Check if we can visit this
                    if (new_row, new_col) not in visited_set:
                        char = board[new_row][new_col]
                        # Check if it will lead to a possible match or not
                        if char in curr_node.children:
                            # Let's explore it
                            curr_char_list.append(char)
                            visited_set.add((new_row, new_col))
                            dfs(new_row, new_col, curr_node.children[char], curr_char_list, visited_set)
                            # Backtrack so pop
                            visited_set.remove((new_row, new_col))
                            curr_char_list.pop()

        # Now we run dfs only on those grid cells which are in children of trie root
        for r in range(R):
            for c in range(C):
                char = board[r][c]
                visited_set = set()
                if char in trie_root.children:
                    visited_set.add((r, c))
                    #print(f"Going for DFS with: {char}")
                    dfs(r, c, trie_root.children[char], [char], visited_set)

        return found_words
