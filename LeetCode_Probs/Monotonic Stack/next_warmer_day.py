"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

# Approach, same as finding next greater element, but instead of element, find the diff between the elements
# So in the array to store -1s, store 0, and replace with diff instead of NGE
# Iterate through the current temps
# If empty stack -> Push current
# Else:
# If current element > top element, add index diff between them in the array and pop top element (as found NGE)
# If current element < top element, push index it on the stack (for comparing with next) -> Break
# We keep indexes in the stack, so we can update result diff with index stored
# If let's say there is one element which is > both of these, then both of these will one by one get popped and array will have the diffs
# So in the else, do until current element < top element
# Make sure to check for empty stack cases before popping

def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    result_diffs = [0 for i in range(len(temperatures))]
    monotonic_stack = [] #decreasing in this case, as if current element > top, then we pop top, so not increasing

    for idx, element in enumerate(temperatures):
        if not monotonic_stack:
            monotonic_stack.append(idx)
        else:
            while monotonic_stack and element > temperatures[monotonic_stack[-1]]:
                result_diffs[monotonic_stack[-1]] = (idx - monotonic_stack[-1])
                monotonic_stack.pop(-1)
            monotonic_stack.append(idx)

    return result_diffs

# Time Space Complexity

# I: Time
# Since we do 1 pass in temperatures, it takes O(n), n is #temps
# Append in a list takes O(1)
# Pop of last element in list takes O(1)
# Updating element at an index in result diffs take O(1)
# Updating at an index is O(1) but insertion takes O(n), as you need to shift elements in list for a new memory block!
# Accessing elements from temps take O(1)
# So final complexity is O(n)

# II: Space
# We're using 2 lists, so O(n + m) = O(n)


print(dailyTemperatures([10, 20, 30, 10]))
print(dailyTemperatures([10, 20, 30, 50]))
print(dailyTemperatures([100, 210, 30, 50]))
print(dailyTemperatures([73,74,75,71,69,72,76,73]))