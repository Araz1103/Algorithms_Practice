"""
You are given an array non-negative integers height which represent an elevation map. 
Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9

So below graph looks like this, and 
water is trapped with #


     []# # #[]
  []#[]# # #[][]
  []#[][]#[][][][]
_________________________________________
"""

# Intuition
# @Each index, if we see what is the maximum height @Left and maximum height @Right
# So minimum of them, decides the water level between the 2 max bars this index is between
# Now the water level @index is this water level - height @index
# So for any index:
# Min(MaxL, MaxR) - Height(idx) gives water level @index
# If the current bar is higher than the water level there, so above is -ve, we skip
# Also, if there are no bars on the left or right, then min becomes 0, and then also will result in -ve or 0, skip


# Implementation 1:
# Pre-Calculate MaxL and MaxR @Each Index with 2 passes @O(N)
# Then with 1 last pass, get the values @each index
# So 3*(O(N)) = O(N) Time Complexity
# But needs 2*O(N) Space Complexity too
from typing import List

def trap(height: List[int]) -> int:

    if len(height)==0:
        return 0 #Edge Case

    # Get MaxL @Each idx
    max_l_r = {}
    current_max = 0
    for idx, num in enumerate(height):
        max_l_r[idx] = [current_max]
        if num > current_max:
            current_max = num

    # Get MaxR @Each idx
    # Iterate @Reverse
    current_max = 0
    for idx in range(len(height)-1, -1, -1):
        num = height[idx]
        max_l_r[idx].append(current_max)
        if num > current_max:
            current_max = num

    # Now max_l_r contains maxL and maxR @each idx
    total_water_level = 0
    for idx, num in enumerate(height):
        total_water_level += max(min(max_l_r[idx]) - num, 0)

    return total_water_level

print(trap([0,2,0,3,1,0,1,3,2,1]))
print(trap([0,2,0]))
print(trap([2,0,3]))
print(trap([2, 0, 3, 1, 4, 5, 0, 0, 4]))

# Implementation 2:
# Using a Left and Right Pointer
# Basically keep a track of MaxL and MaxR
# Whichever is lesser, we shift that
# We update MaxL and MaxR whenever we shift
# The trick is since we want min of MaxL, MaxR
# We don't need both @same time, just the min one is ok
# So that's how we don't need to pre-compute
# O(1) Space Complexity

def trap(height: List[int]) -> int:
    if len(height)==0:
        return 0 #Edge Case
    l, r = 0, len(height)-1
    max_l, max_r = height[l], height[r] #Initialise with the values @l,r
    total_water_level = 0
    while l < r:
        if max_l < max_r:
            # Shift l pointer
            l +=1
            max_l = max(max_l, height[l]) # Update Max L
            # We know that this is the minimum of maxl and maxr here
            # max l >= height_l
            # if it was lesser, updated above
            total_water_level += max_l - height[l] # This can be min 0, as we update before above
        else:
            # Shift r pointer
            r-=1
            max_r = max(max_r, height[r])
            total_water_level += max_r - height[r]

    return total_water_level

print(trap([0,2,0,3,1,0,1,3,2,1]))
print(trap([0,2,0]))
print(trap([2,0,3]))
print(trap([2, 0, 3, 1, 4, 5, 0, 0, 4]))