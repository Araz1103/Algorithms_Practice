"""
Search a 2D Matrix
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true

Example 2:

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000
"""

# Approach Unravel the matrix into a single list, and binary search on that!

from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    num_cols = len(matrix[0])
    search_arr = []
    for row in matrix:
        search_arr.extend(row)

    # Search Arr contains all the elements to search on

    # Implementing Binary Search
    l_p = 0
    r_p = len(search_arr) - 1
    found_idx = -1
    while l_p <= r_p:
        m_p = (l_p + r_p)//2
        m_p_val = search_arr[m_p]

        if target == m_p_val:
            found_idx = m_p
            break

        if m_p_val > target: # Go to the left
            r_p = m_p - 1
        else:
            # Go to the right
            l_p = m_p + 1

    if found_idx == -1:
        return [False, []]
    else:
        # We found the element
        # Get the row and col idx for it
        # To get the column index, we need the modulus of the index found with #cols
        # Example: [1, 2, 3], [4, 5, 6], [9, 10, 12]
        # If index found is 4
        # 4//3 = 1 this means that column is at index 1
        # If index found is 7
        # 6//3 = 0, this means column is 1st at index 0
        # 8//3 = 2, this means column is 3rd at index 2
        # Similiarly for row index, need the floor of (index found/#cols)
        # Example: [1, 2, 3, 4], [5, 5, 9, 10], [11, 12, 17, 19]
        # Index found is 7
        # int(7/4) = 1 (2nd Row, 1st index)
        # Index found is 2
        # int(2/4) = 0 (1st Row, 0th index)
        # Index found is 3
        # int(3/4) = 0 (1st Row, 0th index)
        # Index found is 10
        # int(10/4) = 2 (3rd Row, 2nd Index)
        col_idx = (found_idx%num_cols)
        row_idx = int(found_idx/num_cols)
        return [True, [row_idx, col_idx]]
    
print(searchMatrix([[1, 2, 3], [4, 5, 7], [9, 9, 10]], 11))
print(searchMatrix([[1, 2, 3], [4, 5, 7], [9, 9, 10]], 1))
print(searchMatrix([[1, 2, 3], [4, 5, 7], [9, 9, 10]], 9))
print(searchMatrix([[1, 2, 3], [4, 5, 7], [9, 9, 10]], 4))
print(searchMatrix([[1, 2, 3], [4, 5, 7], [9, 9, 10]], 7))
print(searchMatrix([[1, 2, 3], [4, 5, 7], [9, 9, 10]], 0))


        