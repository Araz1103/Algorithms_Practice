"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

      []
    [][]
    [][]
    [][]  []  
[]  [][][][]
[][][][][][]
 2 1 5 6 2 3

 5 and 6 rectangle makes up 10
 5 5 each is the largest rectangle

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:

  []  
  []  
[][]
[][]
 2 4

2 and 2 combined here or 4 itself makes largest rectangle with area 4

Input: heights = [2,4]
Output: 4
"""

# Approach
# Basically we need to find the combinations of making all rectangles, and then return the one with the max area
# So for each bar in the histogram
# If we look to the left and keep finding bars >= length of that bar
# If we look to the right and keep finding bars >= length of that bar
# So the max area with this histogram is #neighbours on both directions >= this bar * height of this bar
# Also, count this bar itself too in this calculation, if there are no neighbours in either directions satisfying this

# So once we iterate through and find all areas, return the max of all of them!

# So basically I can do 1 iteration from left to right, finding the next lesser element
# And while I reach the next lesser element, I keep a track of the elements between them
# So that gives me an idea of -> Right area

# Then I do another iteration from right to left, finding the next lesser element
# Again, I keep track of elements between them
# So that gives me an idea of <- Left area

# Finally add both left and right for each, and that gives total, and the max of that is my answer!
# This is O(2*n) = O(n)

def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """

    #print(heights)

    # First iteration from Left to Right
    #print("LTR")
    l_t_r = [0 for i in range(len(heights))]

    monotonic_stack = [] # This will be increasing, as if decreasing, we pop

    for idx, element in enumerate(heights):
        # print(idx, element)
        # print(f"MS: {monotonic_stack}")
        # print(f"LTR: {l_t_r}")
        if not monotonic_stack:
            monotonic_stack.append(idx)
        else:
            while monotonic_stack and element < heights[monotonic_stack[-1]]:
                # print("Condition Met!")
                # print(f"Top Element: {monotonic_stack[-1]}")
                # print(f"IDX is: {idx}")
                l_t_r[monotonic_stack[-1]] = (idx - 1) - monotonic_stack[-1] #Intentionally doing -1 in diff, to not count that bar, @end will count it
                # print(f"New LTR is: {l_t_r}")
                #Storing diff, and (diff)*height_element is max for that height bar towards right side
                monotonic_stack.pop(-1)
            monotonic_stack.append(idx)

    # Now all elements which are 0 (except the last one), that means that all the elements to the right of them are always increasing
    # So we just need a count of all elements to their right
    # Now all these elements must not be popped from the monotonic increasing stack
    # So the count is (len - 1) - their index (this excludes them)
    # print(l_t_r)
    # print(f"Final MS: {monotonic_stack}")
    for idx in monotonic_stack:
        l_t_r[idx] = (len(heights) - 1) - idx
    # print(l_t_r)

    # Second iteration from Right to Left
    #print("RTL")
    r_t_l = [0 for i in range(len(heights))]

    monotonic_stack = [] # This will be increasing, as if decreasing, we pop

    for idx in range((len(heights) - 1), -1, -1):
        element = heights[idx]
        # print(idx, element)
        # print(f"MS: {monotonic_stack}")
        # print(f"RTL: {r_t_l}")
        if not monotonic_stack:
            monotonic_stack.append(idx)
        else:
            while monotonic_stack and element < heights[monotonic_stack[-1]]:
                # print("Condition Met!")
                # print(f"Top Element: {monotonic_stack[-1]}")
                # print(f"IDX is: {idx}")
                r_t_l[monotonic_stack[-1]] = monotonic_stack[-1] - idx - 1  #Intentionally doing -1 in diff, to not count that bar, @end will count it
                #print(f"New RTL is: {r_t_l}")
                #Storing diff, and (diff)*height_element is max for that height bar towards right side
                monotonic_stack.pop(-1)
            monotonic_stack.append(idx)

    # Now all elements which are 0 (except the last one), that means that all the elements to the left of them are always increasing
    # So we just need a count of all elements to their left
    # Now all these elements must not be popped from the monotonic increasing stack
    # So the count is (len - 1) - their index (this excludes them)
    # print(r_t_l)
    # print(f"Final MS: {monotonic_stack}")
    for idx in monotonic_stack:
        r_t_l[idx] = idx
    #print(r_t_l)

    max_area = 0
    for idx, (ltr_count, rtl_count) in enumerate(zip(l_t_r, r_t_l)):
        total_count = ltr_count + rtl_count + 1
        total_area = heights[idx] * total_count
        if total_area >= max_area:
            max_area = total_area

    return max_area

print(largestRectangleArea([2,1,5,6,2,3]))
print(largestRectangleArea([2,2,3]))
print(largestRectangleArea([2,4]))
print(largestRectangleArea([2,5]))



    


