"""
You are given an image represented by an m x n grid of integers image, 
where image[i][j] represents the pixel value of the image. 
You are also given three integers sr, sc, and color. 
Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, 
either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and 
modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

 
Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation:

From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel),
all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

Output: [[0,0,0],[0,0,0]]

Explanation:

The starting pixel is already colored with 0, which is the same as the target color. 
Therefore, no changes are made to the image.

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n
"""

from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # Perform BFS and Keep adding if horizontally and vertically adjacent, starting color same and already not in colour
        # Ensure that you check for out of bounds
        # In place keep filling
        num_r, num_c = len(image), len(image[0])
        # Since with given constraints we know sr, sc are always valid
        # Otherwise check edge case before adding to queue and visited
        queue = deque()
        visited = set()
        queue.append((sr, sc))
        visited.add((sr, sc))
        starting_colour = image[sr][sc]
        dirs = [[0, 1], # Right
                [0, -1], # Left
                [1, 0], # Down
                [-1, 0] # UP
                ]

        while queue:
            curr_r, curr_c = queue.popleft()
            # Fill with colour now
            image[curr_r][curr_c] = color

            # Iterate through all adjacent and vertical
            for dr, dc in dirs:
                new_r, new_c = curr_r + dr, curr_c + dc
                # Check in bounds
                if min(new_r, new_c) >= 0 and new_r < num_r and new_c < num_c:
                    # Check if is same as starting color and not in visited
                    if (new_r, new_c) not in visited and image[new_r][new_c] == starting_colour:
                        # Add to visited and append to queue
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))

        return image
        