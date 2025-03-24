from typing import List
from collections import deque

# BRUTE FORCE
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Intuition Brute Force
        # For each cell, we want to check if we can reach either 1st row or colmn
        # and either last row or colmn
        # So we do a BFS to explore all valid nodes (where height <=)
        # If in between we tick off both of these flags, then we know from this cell
        # water can flow to both A and P
        num_row, num_col = len(heights), len(heights[0])
        dirs = [
            [0,1], #RIGHT
            [0,-1],#LEFT
            [1,0],#DOWN
            [-1,0]#UP
        ]
        def bfs(start_row, start_col):
            queue = deque()
            visited = set()
            queue.append((start_row, start_col))
            visited.add((start_row, start_col))

            reach_pacific = False
            reach_atlantic = False

            while queue:
                curr_row, curr_col = queue.popleft()

                # Check if reached pacific
                if curr_row==0 or curr_col==0:
                    reach_pacific = True

                # Check if reached atlantic
                if curr_row==num_row-1 or curr_col==num_col-1:
                    reach_atlantic = True

                # If both are satisfied can stop exploring
                if reach_pacific and reach_atlantic:
                    break

                # Otherwise let's keep exploring all valid neighbours
                for dr, dc in dirs:
                    new_row = curr_row + dr
                    new_col = curr_col + dc
                    
                    # Check if out of bounds and not visited
                    if min(new_row, new_col) >=0 and new_row < num_row and new_col < num_col and (new_row, new_col) not in visited:
                        # Check if water level is <= current water level
                        if heights[new_row][new_col] <= heights[curr_row][curr_col]:
                            # Can explore it
                            # Add to visited
                            queue.append((new_row, new_col))
                            visited.add((new_row, new_col))

            return (reach_pacific and reach_atlantic)

        valid_cells = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if bfs(r, c):
                    valid_cells.append([r, c])

        return valid_cells


# OPTIMISED
# Start from Pacific and Atlantic Edges
# First Col, First Row and Last Col, Last Row
# Keep checking for each from which cells you can visit them, and keep marking those
# @end iterate through grid and the cells where both can visit are your answer!
# This is O(M*N) as Pacific and Atlantic Searches can only visit each cell in grid once
# Since their visit sets are there
# The visit set ensures that in last col, for example, if we try with a cell and that leads to a visited cell for 
# atlantic, we don't visit it again
# So Time Complexity is: 2*O(M*N) + O(M*N) -> 2 for Atlantic and Pacific searches and 1 for final cells check
# So TC: O(M*N)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_row, num_col = len(heights), len(heights[0])
        dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        # BFS to modify visited in place
        def bfs(start_row, start_col, visited):
            queue = deque()
            if (start_row, start_col) not in visited:
                visited.add((start_row, start_col))
                queue.append((start_row, start_col))

            while queue:
                curr_row, curr_col = queue.popleft()

                for dr, dc in dirs:
                    new_row, new_col = curr_row + dr, curr_col + dc

                    # Check if out of bounds and not in visited
                    if min(new_row, new_col) >=0 and new_row < num_row and new_col < num_col \
                    and (new_row, new_col) not in visited:
                        # Check if can flow from here
                        if heights[new_row][new_col] >= heights[curr_row][curr_col]:
                            queue.append((new_row, new_col))
                            visited.add((new_row, new_col))
        
        # Maintain 2 sets for Pacific and Atlantic Flow
        pacific_visited = set()
        atlantic_visited = set()

        # First Let's do a BFS from Pacific
        # First Row and First Col
        pacific_start = [ (0, c) for c in range(num_col) ] + [ (r, 0) for r in range(num_row) ]
        for r, c in pacific_start:
            bfs(r, c, pacific_visited)

        # Now Atlantic 
        # Last Row and Last Col
        atlantic_start = [ (num_row-1, c) for c in range(num_col) ] + [ (r, num_col-1) for r in range(num_row)]
        for r, c in atlantic_start:
            bfs(r, c, atlantic_visited)

        # Now iterate over the grid and check all r, c's in both sets
        valid_cells = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    valid_cells.append([r, c])

        return valid_cells

