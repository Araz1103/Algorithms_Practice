"""
You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. 
You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.

Example 1:
Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

Output: 6
Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.

Constraints:
1 <= grid.length, grid[i].length <= 50

"""

from typing import List
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # We explore all elements in the grid
        # When we find a 1, we explore with BFS or DFS
        # When exploring, we keep a count of num_1s we find
        # That is the area of the island
        # Keep updating max area

        max_area = 0
        R = len(grid)
        C = len(grid[0])
        visited = set() #to keep track of visited while exploring
        directions = [
            [0,1], #RIGHT
            [0,-1], #LEFT
            [1,0], #DOWN
            [-1,0] #UP
        ]
        # recursive dfs
        def dfs(r,c):
            # if grid[r][c]==0: #stop exploring
            #     return 0
            num_1s = 1 #current coordinate
            # make this coordinate as visited too!
            visited.add((r,c))
            for row_diff, col_diff in directions:
                new_row = row_diff + r
                new_col = col_diff + c
                if min(new_row, new_col) >=0 and new_row < R and new_col < C \
                and (new_row, new_col) not in visited and grid[new_row][new_col]==1:
                    visited.add((new_row, new_col))
                    num_1s += dfs(new_row, new_col)
            return num_1s

        # Better recursive
        # def dfs(r, c):
        #     # Check current coordinate, if not valid return 0 for this
        #     if min(r,c) < 0 or r >=R or c >=C or (r, c) in visited \
        #     or grid[r][c]==0:
        #         return 0 # No count of island from here
        #     visited.add((r,c)) #add this current one as visited
        #     # Otherwise we explore all and return their counts
        #     return (1 + dfs(r, c+1) + dfs(r, c-1) + dfs(r+1, c) + dfs(r-1, c))

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            #imp after appending starting point, add to visited
            visited.add((r,c))
            num_1s = 0
            while queue:
                #print(queue)
                curr_r, curr_c = queue.popleft()
                num_1s += 1 #Everytime we pop a 1 from the queue

                for row_diff, col_diff in directions:
                    new_row = curr_r + row_diff
                    new_col = curr_c + col_diff

                    # Check if out of bounds
                    # Check if in visited or not
                    # Check if it is a 1
                    if min(new_row, new_col) >= 0 and new_row < R and new_col < C \
                    and (new_row, new_col) not in visited and grid[new_row][new_col]==1:
                        # Add to queue for exploring
                        queue.append((new_row, new_col))
                        # mark as visited
                        visited.add((new_row, new_col))

            return num_1s

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in visited:
                    #area = bfs(r,c)
                    area = dfs(r,c)
                    #print(area)
                    max_area = max(max_area, area)

        return max_area