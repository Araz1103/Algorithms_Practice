from typing import List
# This is ok, but the squares can be done better
# Also in 1 pass can compute for all

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First maintain Hashset for each Row and check if dups
        # Then maintain Hashset for each Column and check if dups
        # Then for each box, need to do the same
        # If all valid True
        # Whenever not found return False

        # Rows
        for board_row in board:
            row_hm = set()
            for val in board_row:
                if val != ".":
                    if val not in row_hm:
                        row_hm.add(val)
                    else:
                        return False #Duplicate found

        # Cols
        for board_col in range(len(board[0])):
            col_hm = set()
            for board_row in board:
                val = board_row[board_col]
                if val!=".":
                    if val not in col_hm:
                        col_hm.add(val)
                    else:
                        return False
        
        # Squares
        for r_idx in range(0, 9, 3):
            for c_idx in range(0, 9, 3):
                square_hm = set()
                for row_idx in range(r_idx, r_idx+3):
                    for col_idx in range(c_idx, c_idx + 3):
                        val = board[row_idx][col_idx]
                        if val!=".":
                            if val not in square_hm:
                                square_hm.add(val)
                            else:
                                return False

        return True


        
# Basically
# Maintain Hash Sets for Rows, Cols and Squares
# For the 9x9
#
#     0   0      1      2
#     |      |      |      |
#      -------------------
#     |      |      |      |
#     1 --------------------
#     |      |      |      |
#     2 ---------------------
# For each of the square, the square itself can have an index
# And we can check if the curr element belongs to which square
# And does the Hash Set of that square has this already or not
# Key for Squares: r//3, c//3
# Example: 7, 8 is in the square 2, 2
# 7//3, 8//3 = 2,2
# 3, 4 is in the square 1, 1
# 3//3, 4//3 = 1, 1
# So we maintain a hashset for each square and when encountering elements of a square check dups
# Similiarly for rows and cols

def isValidSudoku(board: List[List[str]]) -> bool:
    num_rows = len(board)
    num_cols = len(board[0])
    row_sets = {r: set() for r in range(num_rows)}
    col_sets = {c: set() for c in range(num_cols)}
    square_sets = {}
    for i in range(3):
        for j in range(3):
            square_sets[(i, j)] = set()

    for r in range(num_rows):
        for c in range(num_cols):

            # Check if val in any of the sets or not
            val = board[r][c]

            if val == '.':
                continue

            if val in row_sets[r] or \
            val in col_sets[c] or \
            val in square_sets[(r//3, c//3)]:
                return False
            
            # Add in all sets now
            row_sets[r].add(val)
            col_sets[c].add(val)
            square_sets[(r//3, c//3)].add(val)

    return True
                
