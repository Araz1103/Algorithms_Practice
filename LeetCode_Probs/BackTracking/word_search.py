"""
Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true
Example 2:



Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: false
Constraints:

1 <= board.length, board[i].length <= 5
1 <= word.length <= 10
board and word consists of only lowercase and uppercase English letters.
"""
from typing import List
class Solution:
    # Time Complexity:
    # We need to in worst case explore from each cell in the board
    # So m*n for board dimensions
    # For each grid, we do a dfs call
    # But internally each dfs call will do 4 calls for each neighbour
    # Recursion stack is w, since post that we stop
    # So for each call: 4*4*.....4 w times
    # So: O(m*n*4^w)
    # So: O(m*n*4^w) where m and n are board dimensions and w is length of word

    # Space Complexity:
    # We have a curr word list and visited set
    # Each of which in worst case can contain upto word length of characters
    # Recursion call stack can also be max upto word length
    # So: O(w)

    def exist(self, board: List[List[str]], word: str) -> bool:
        # Start @everyposition on the grid
        # Take only vertical and horizontal neighbours and keep track of visited and out of bounds
        # Go uptill length of the word, keeping the list appended
        # Pop and Backtrack back 
        # If found, update global
        # Or return fast

        #found_word = [False]
        directions = [
            [0, 1], #Right
            [0, -1], #Left
            [1, 0], #Down
            [-1, 0] #Up
        ]
        R = len(board)
        C = len(board[0])

        def dfs(curr_row, curr_col, curr_word_list, visited_set):

            # Base Case when length of word
            if len(curr_word_list)==len(word):
                if ''.join(curr_word_list)==word:
                    #found_word[0] = True
                    return True

            # @current position explore all neighbours
            for dr, dc in directions:
                new_row = curr_row + dr
                new_col = curr_col + dc

                if min(new_row, new_col) >= 0 and new_row < R and new_col < C:
                    if (new_row, new_col) not in visited_set:
                        curr_word_list.append(board[new_row][new_col])
                        visited_set.add((new_row, new_col))
                        if dfs(new_row, new_col, curr_word_list, visited_set):
                            return True
                        # Backtrack and pop
                        curr_word_list.pop()
                        visited_set.remove((new_row, new_col))

        for r in range(R):
            for c in range(C):
                visited_set = set()
                visited_set.add((r, c))
                if dfs(r, c, [board[r][c]], visited_set):
                    return True

        return False






        