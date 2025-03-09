"""
You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. 
If this state is impossible within the grid, return -1.

Example 1:
Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

Output: 4

Example 2:
Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

Output: -1
Constraints:

1 <= grid.length, grid[i].length <= 10
"""

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # The beginning of our queue, we can have all the initial rotting oranges
        # Then we can start doing a BFS, to determine how many neighbours can we rot from 
        # each of them
        # We only add the neighbour if it has a 1 
        # Rather than visited set, let's modify in place, will help us check @end
        # Each level is technically 1 minute
        # We continue the traversal until queue is empty (cannot visit any more)
        # @end we will need to check if any 1s remain, if they do, we return -1
        # otherwise we return the length, which is num
        # since we modified in place, can check @end

        R = len(grid)
        C = len(grid[0])

        queue = deque()

        # Add all 2s in the queue
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==2:
                    queue.append((r, c))

        length = 0

        while queue:
            print(queue)
            for i in range(len(queue)): #Checking @current level, what are available to rot
                r, c = queue.popleft()
                # Basically whatever neighbours we encounter
                # We convert them into rotten
                directions = [
                    [0,1], #RIGHT
                    [0,-1], #LEFT
                    [1,0], #DOWN
                    [-1,0] #UP
                ]

                for row_diff, col_diff in directions:
                    new_row = r + row_diff
                    new_col = c + col_diff

                    # First check if within bounds and check if it is 1, then only we add
                    if min(new_row, new_col) >= 0 and new_row < R and new_col < C \
                    and grid[new_row][new_col]==1:
                        queue.append((new_row, new_col))
                        # Make this a 2, so we don't add later
                        # We rot it basically
                        grid[new_row][new_col] = 2
            
            if len(queue):
                length+=1 #If we were able to find neighbours to rot, we go to next level
            

        # Now when finished with queue, we have tried to rot all possible oranges
        # If there is still a 1, this means it is impossible
        # Return -1
        # Otherwise return length, that is the min possible mins to rot all
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    return -1 #We found 1 orange not rotten

        return length
