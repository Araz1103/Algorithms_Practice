"""
Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [
  [1,2],
  [3,4]
]

Output: [
  [3,1],
  [4,2]
]

Example 2:
Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Basically 1st column becomes 1st row in reverse
        # 2nd column becomes 2nd row in reverse
        # ..... nth column becomes nth row in reverse

        # To do in place
        # column index becomes row index
        # row index becomes: n (#rows) - row index

        # But to do in place, start layer by layer
        # First we want to rotate the outermost square
        # Then the inner square and so on

        # Make 2 pointers, l and r
        # They will initially be @outermost square
        # l at 0 and r at last cell from right
        # Then for the inner square, l moves ahead and r comes back
        # For the width, again, since square, l and r at 0 and bottom cell
        # Since n x n, l and r is same as above l and r
        # We keep shifting l and r until l no longer < r

        l,r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l): # We have to rotate/shift all cells in between
                # i helps to shift one by one
                top, bottom = l, r

                # We can save top left, and move all others, @end put top left
                topLeft = matrix[top][l + i]

                # Move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Finally move the top left into top right
                matrix[top + i][r] = topLeft

            r-=1 # R towards left
            l+=1 #L towards right
        