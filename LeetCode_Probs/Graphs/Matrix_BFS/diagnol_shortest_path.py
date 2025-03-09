"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. 
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
 
Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 
Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""

# Since share corner, this means can go diagnally also!
from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # So this is like standard BFS, but instead of just 4 directions
        # We can go diagnally as well!
        R = len(grid) #numrows
        C = len(grid[0]) #numcols
        queue = deque()
        visited = set()
        # Check starting point is allowed, otherwise return -1
        if grid[0][0]==1:
            return -1
        queue.append((0,0)) #starting point
        visited.add((0,0)) #started, so add to visited
        length = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r==R-1 and c==C-1: #Reached @bottom right
                    return length

                directions = [
                    [0,1], #RIGHT
                    [0,-1], #LEFT
                    [1, 0], #DOWN
                    [-1, 0], #UP
                    [1,1], #DIAGNAL UP RIGHT
                    [1,-1], #DIAGNAL UP LEFT
                    [-1,1], #DIAGNAL DOWN RIGHT
                    [-1,-1] #DIAGNAL DOWN LEFT
                ]

                for row_difference, col_difference in directions:
                    new_row = r + row_difference
                    new_col = c + col_difference

                    # Check Cases
                    # I: Not out of bounds
                    # II: Should not be visited already
                    # III: Should not be a 1
                    if min(new_row, new_col) >= 0 and new_row < R and new_col < C \
                       and (new_row, new_col) not in visited and grid[new_row][new_col]!=1:
                        # Can add to the queue
                        queue.append((new_row, new_col))
                        # Add in visisted, so we don't add same in queue again
                        visited.add((new_row, new_col))

            length+=1
        return -1
        
        