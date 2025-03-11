"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. 
A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.


Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])
        def count_paths(r , c, cache_grid):
            # if out of bounds
            if r==R or c==C:
                return 0

            # If the position is a 1/obstacle
            if obstacleGrid[r][c]==1:
                return 0

            # If reached target
            if r==R-1 and c==C-1:
                return 1

            if cache_grid[r][c] > 0:
                return cache_grid[r][c]

            cache_grid[r][c] = count_paths(r+1, c, cache_grid) + count_paths(r, c+1, cache_grid)

            return cache_grid[r][c]
        #return count_paths(0, 0, [[0]*C for i in range(R)])

        def bottoms_up_dp():
            prev_row = [0]*C
            prev_row[-1] = 1 #Target starts at 1

            for row in range(R-1, -1, -1):
                
                curr_row = [0]*C
                curr_row[-1] = prev_row[-1] if obstacleGrid[row][-1]!=1 else 0
                for col in range(C-2, -1, -1):
                    if obstacleGrid[row][col]==1:
                        curr_row[col] = 0
                    else:
                        curr_row[col] = curr_row[col+1] + prev_row[col]
                print(prev_row, curr_row)
                prev_row = curr_row
            #print(prev_row)
            return prev_row[0]
        return bottoms_up_dp()