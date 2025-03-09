from collections import deque

# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Shortest path from top left to bottom right
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or
                    r + dr == ROWS or c + dc == COLS or
                    (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1

from typing import List
def shortestPath(grid: List[List[int]]) -> int:
    # We need a queue for BFS
    queue = deque()
    # visit set to keep track of what's visited
    visited = set()

    # Starting vertices are 0,0
    # Add to queue
    queue.append((0,0))
    visited.add((0,0))

    # While queue, we keep checking at each level
    # level for us is length from starting vertice
    length = 0 #for starting vertice, to reach them length is 0
    while queue: #keep popping from it, exploring neighbours, add them and then go to next level with added neighbours
        # We pop all in the queue at this state
        # So all vertices at this level/length
        for i in range(len(queue)): #Is a snapshot of current queue, not affected by appends
            r, c = queue.popleft() #get current row and column

            # We check if we have reached the target or not
            if r==len(grid)-1 and c==len(grid[0])-1: #at bottom right corner
                return length #can directly return current length
                # So if our target was starting vertices, to reach them we need 0
                # That's why length is 0
                # Makes sense
                # We increment length post adding, and since we are checking before, makes sense!

            # Now we want to explore all valid neighbours
            # Using smart addition to row and col to get those
            directions = [  [0, 1], #RIGHT
                            [0, -1], #LEFT
                            [1, 0], #DOWN
                            [-1, 0] #UP
                            ]

            for row_diff, col_diff in directions:
                new_row = r + row_diff
                new_col = c + col_diff
                # Now check if we can go to this neighbour before adding to the queue

                # I: Should not be out of bounds
                # II: Should not be in visited set
                # III: Should not be a '1', Check this only after out of bounds check, else index error!
                if min(new_row, new_col) >=0 and new_col < len(grid[0]) and \
                new_row < len(grid) and grid[new_row][new_col]!=1 and (new_row, new_col) not in visited:
                    # We can add them in the queue
                    queue.append((new_row, new_col))
                    # Add them to the visited set, so we don't try to add same to queue again
                    visited.add((new_row, new_col))

        # Increment length
        length+=1

    # If escapes while loop, means we never reached our target
    # Returning -1
    return -1
