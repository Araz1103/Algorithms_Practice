"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

# My Approach
# We have 2 aspects for area
# X-Axis, Where Length of Rectangle is decided
# Y-Axis where Height of Rectangle is decided

# Basically start a pointer @start and @end
# This is the max length possible
# Keep a max_area variable
# Only update it if you find a bigger max area
# Since you're limited by the smaller bar always (height) in area
# Move the pointer at the smaller bar, inwards
# Keep repeating until the pointers cross each other or at the same bar
# Essentially you will be calculating all the max spans
# The core logic is that since you're moving when the bar is smaller, the bigger bar can lead to bigger area

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    left_pointer = 0
    right_pointer = len(height) - 1

    while left_pointer != right_pointer:
        lenght = (right_pointer - left_pointer)
        if height[left_pointer] <= height[right_pointer]:
            smaller_height = height[left_pointer]
            # Since left is smaller, we increment it to +1, to move it to right
            left_pointer +=1
        else:
            smaller_height = height[right_pointer]
            # Since right is smaller, we increment it to -1, to move it to left
            right_pointer -=1

        current_area = lenght*smaller_height
        if current_area >= max_area:
            max_area = current_area

    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
print(maxArea([3, 2, 3, 5]))

# Same logic, 2 pointers, worded differently

from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Start from L and R
        # We can calculate Area @any given L and R
        # Now instead of calculating for all, our aim is to see maximum possible
        # We know that our area can increase by lenght x width
        # Length not in control, whenever we shift 1, length decreases by 1
        # But Width controlled by the bars
        # The shorter bar is the one which restricts the area
        # So start L=0 and R@end
        # Keep calculating area, and updating max area
        # Move whichever has a shorter bar, as that restricts your area

        L = 0
        R = len(heights)-1
        max_area = 0

        while L < R: #Can't be equal as no container possible
            curr_area = (R-L)*min(heights[L], heights[R])
            # Update maximum
            max_area = max(max_area, curr_area)
            if heights[L] > heights[R]:
                R-=1
            else:
                L+=1

        return max_area
        