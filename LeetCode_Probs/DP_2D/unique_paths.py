"""
There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths 
that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

You may assume the output will fit in a 32-bit integer.

Example 1:
Input: m = 3, n = 6
Output: 21

Example 2:
Input: m = 3, n = 3
Output: 6

Constraints:

1 <= m, n <= 100
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # We can have a recursive soln to try the 2 directions
        # Whenever we go out of bounds, we return a 0
        # If we reach the target we know count is 1 from that vertice
        
        # Time complexity of Brute Force
        # We try 2 directions for all the paths
        # Each path length is r + c, since only down and right allowed
        # So TC: O(2^(r+c))
        # Doing repeated work for a lot of cells
        def count_paths(r,c):
            if r == m or c == n:
                # out of bounds
                # since we can only go down or right, can only
                # go out of bounds when reach mth row or nth column
                return 0 
            
            if r == m-1 and c==n-1:
                # reached target
                return 1

            return (count_paths(r+1, c) + count_paths(r, c+1)) # Only 2 possible directions

        # With memoization, we only need to visit each cell @max once
        # TC: O(m*n)
        # Space complexity: Size of grid: O(m*n)
        def count_paths_memoization(r,c, cache_grid):
            if r == m or c == n:
                # out of bounds
                # since we can only go down or right, can only
                # go out of bounds when reach mth row or nth column
                return 0 
            
            if r == m-1 and c==n-1:
                # reached target
                return 1

            if cache_grid[r][c] > 0:
                return cache_grid[r][c]

            cache_grid[r][c] = (count_paths_memoization(r+1, c, cache_grid) + count_paths_memoization(r, c+1, cache_grid)) # Only 2 possible directions
            return cache_grid[r][c]

        #return count_paths_memoization(0,0, [[0]*n for i in range(m)])

        # Bottoms Up Approach
        # Start @target, work our way towards start node
        # Each cell is dependent on the right and down neighbour for their paths
        # For last row, since nothing down, only immediate right determines it's path
        # For last column, nothing on immediate right, only down
        # So last column is all 1s, since target we start @1 to reach
        # And we go row by row from last to first, from last column to first
        # Since we only need the bottom row to determine the above row, we just need one row in memory 
        # So space complexity can become: O(n) (one row has n cols, so array of len n)
        # Time remains same, as we work @each cell, to get it's count
        def bottom_up_dp(m,n):
            prev_row = [0]*n
            prev_row[-1] = 1
            print(prev_row)
            for row in range(m-1, -1, -1): #Start @last row
                prev_col = 1
                curr_row = [0]*n
                curr_row[-1] = 1
                for col in range(n-2, -1, -1): #Start @second last col, as we know last col is 1s
                    curr_row[col] = prev_row[col] + prev_col
                    prev_col = curr_row[col]

                prev_row = curr_row
            print(prev_row)
            return prev_row[0]

        #return bottom_up_dp(m,n)

        def bottom_up_dp2(m,n):
            prev_row = [0]*n

            for row in range(m-1, -1, -1):
                curr_row = [0]*n
                curr_row[-1] = 1
                for col in range(n-2, -1, -1):
                    # Sum from col on right and col below
                    # For below, we keep the prev row in memory
                    curr_row[col] = curr_row[col+1] + prev_row[col]
                prev_row = curr_row

            return prev_row[0]
                    
        