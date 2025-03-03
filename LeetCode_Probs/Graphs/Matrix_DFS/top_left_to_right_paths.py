"""
Matrix Depth First Search

You are given a binary matrix Grid where 0s represent land and 1s represent rocks that can not be traversed.

Return the number of unique paths from the top-left corner of Grid to the bottom-right corner 
such that all traversed cells are land cells. You may only move vertically or horizontally through land cells. 
For an individual unique path you cannot visit the same cell twice.

Example 1:

Input: grid = [
  [0, 0, 0, 0],
  [1, 1, 0, 0],
  [0, 0, 0, 1],
  [0, 1, 0, 0]
]

Output:
2
"""
from typing import List

def countPaths(grid: List[List[int]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])

    # We basically do a DFS
    # We keep expanding 
    # We can try to go UP, DOWN, LEFT or RIGHT @each position on our grid
    # Whenever we cannot go further, we have to backtrack, and return count 0
    # If we reach the bottom right corner, we have to backtrack, and return count 1

    # Keep a visited set, so we know which nodes to not visit again
    # Add and Pop from it accordingly

    def dfs(visited_set, current_row, current_col):

        # Base cases first
        # If we go out of bounds
        if current_row < 0 or current_col < 0 or current_row == num_rows or current_col == num_cols:
            # 0 indexed, so #rows and #cols is out of bounds
            return 0 #Count is 0, and we stop looking further
        # If we attempt to visit a node, which is already visited
        if (current_row, current_col) in visited_set:
            return 0
        # If we attempt to go to a node which is 1, not allowed
        if grid[current_row][current_col]==1:
            return 0 
        
        # Now the case when we reach our target, bottom right corner
        if current_row==(num_rows-1) and current_col==(num_cols-1):
            return 1# We will add to our count of paths found
        
        # Now let's do exploration
        count = 0 #Initialising count from here, will check in all directions and increment
        # @end will return count, with backtracking, num paths from each node (count) get returned
        # So @end, from 0, 0 will know count, which is #unique paths to reach bottom right corner

        #Let's add current row and col in visited, so doesn't visit this again
        visited_set.add((current_row, current_col))

        #UP
        count+=dfs(visited_set, current_row-1, current_col)
        #DOWN
        count+=dfs(visited_set, current_row+1, current_col)
        #LEFT
        count+=dfs(visited_set, current_row, current_col-1)
        #RIGHT
        count+=dfs(visited_set, current_row, current_col+1)

        # Now to backtrack, we pop the current row col from visited
        visited_set.remove((current_row, current_col))

        # Return count
        return count
    
    num_paths = dfs(set(), 0, 0)

    return num_paths

        