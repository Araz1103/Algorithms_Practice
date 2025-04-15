"""
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. 
You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

Example 2:
Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4

Constraints:
1 <= grid.length, grid[i].length <= 100
grid[i][j] is '0' or '1'.
"""
from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Basically we check all the elements in the grid
        # When we find a '1', we keep checking around it if there are more
        # Whatever we find, we mark those as visited or convert to '0'
        # Everytime we find this '1' and we are done exploring, we can say we finished 
        # with 1 island
        # So can increment count
        # Since we maintain a visited set or convert to 0, we will always find unique island groups
        visited = set()
        R = len(grid)
        C = len(grid[0])
        num_islands = 0
        # define global directions, since use them everytime
        directions = [
            [0,1], #RIGHT
            [0,-1], #LEFT
            [1,0], #DOWN
            [-1,0] #UP
        ]


        # BFS
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r, c)) #IMP Add
            while queue:
                curr_r, curr_c = queue.popleft()
                for row_diff, col_diff in directions:
                    new_row = curr_r + row_diff
                    new_col = curr_c + col_diff
                    # Check should not be out of bounds
                    # Should not be visited
                    # Only explore if we find a '1'
                    if min(new_row, new_col) >= 0 and new_row < R and new_col < C \
                    and (new_row, new_col) not in visited and grid[new_row][new_col]=='1':
                        # Add to queue for exploring
                        queue.append((new_row, new_col))
                        # mark visited
                        visited.add((new_row, new_col))

        # DFS Iterative
        def dfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r, c)) #IMP Add
            while queue:
                # Instead of popping from left
                # We pop from end, so LIFO
                curr_r, curr_c = queue.pop()
                for row_diff, col_diff in directions:
                    new_row = curr_r + row_diff
                    new_col = curr_c + col_diff
                    # Check should not be out of bounds
                    # Should not be visited
                    # Only explore if we find a '1'
                    if min(new_row, new_col) >= 0 and new_row < R and new_col < C \
                    and (new_row, new_col) not in visited and grid[new_row][new_col]=='1':
                        # Add to queue for exploring
                        queue.append((new_row, new_col))
                        # mark visited
                        visited.add((new_row, new_col))

        # DFS Recursive
        def dfs(r,c):
            if grid[r][c]=='0':
                return # No need to explore further

            for row_diff, col_diff in directions:
                new_row = r + row_diff
                new_col = c + col_diff
                # If not out of bounds
                # If not already visited
                # If land ('1'), then we explore
                # before exploring mark as visited
                if min(new_row, new_col) >= 0 and new_row < R and new_col < C \
                and (new_row, new_col) not in visited and grid[new_row][new_col]=='1':
                    visited.add((new_row, new_col))
                    dfs(new_row, new_col)

        # Explore all elements in grid
        for r in range(R):
            for c in range(C):
                if grid[r][c]=="1" and (r,c) not in visited:
                    # Can use either bfs or dfs to explore!
                    dfs(r,c)
                    #bfs(r,c)
                    num_islands+=1

        return num_islands