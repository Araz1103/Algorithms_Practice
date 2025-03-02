"""
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.

Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-10^4 <= matrix[i][j] <= 10^4
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 10^4 calls will be made to sumRegion.
"""

# Intuition
# Initialise the Matrix
# For each row, maintain prefix sums

# When a rectangle corners are given
# Figure out the l,r's for the rows of the rectangle
# Make O(1) calls for each row with range sum using prefix sum logic
# Return total sum of that for area of a rectangle

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        self.prefix_sums = [[] for row in range(num_rows)] #List of lists, 1 for each row
        for row_idx, row in enumerate(matrix):
            # Each row is a list
            # We calculate prefix sums for each row and store
            total = 0
            for val in row:
                total+=val
                self.prefix_sums[row_idx].append(total)

        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # For each row in this rectangle
        # Will use Prefix Sums of the row to calculate sum of row
        # Get rows, col_l and col_r's
        # Rows are between row1 and row2
        # col_l is col1
        # col_r is col2
        total_sum = 0
        for row_idx in range(row1, row2+1):
            total_sum+=self.get_range_sum(row_idx, col1, col2)
        return total_sum


    def get_range_sum(self, row_idx, col_l, col_r):
        # Given for a row, col l and r
        # Calculate the sum between them (inclusive)

        prefix_row_sums = self.prefix_sums[row_idx]
        if col_l > 0:
            return prefix_row_sums[col_r] - prefix_row_sums[col_l-1]
        else:
            return prefix_row_sums[col_r]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)