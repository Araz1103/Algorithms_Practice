"""The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
 

Follow up: Could you find an O(nums1.length + nums2.length) solution?
"""

# Approach

# First find all the Next Greater Elements for all elements in nums2
# Then @end, just return for all the ones nums1 is asking

# Now to find the NGE in nums 2
# So first we have a result array, length of nums 2, with initialised to -1
# Now we keep a 'stack', where we will keep adding indexes as we need them
# So conditions are as follows
# Iterate through nums 2 (along with indexes)
# 1. If stack is empty, push the index of the current element in the stack
# 2. If stack is NE:
# Keep checking until, the value of the current index <= top index
# 2A. Value of the current index is > the value of the top most index @stack -> This means that this is the NGE for the top index
# 2A. So update the result[top_index] = value of result of current index
# 2A. Pop the top index from the stack (As we've found the NGE for it, no longer need it)
# 2B. Value of the current index is <= value of the top most index @stack -> Push the current index in stack

# So the logic is that the stack is monotonically keeping decreasing order of elements
# If nums 2 was monotinically decreasing, then this stack will keep on adding indexes in that order
# And then result array will be all -1s

# If we wanted to find next smaller element, we need to do the reverse
# We want to keep a monotinically increasing array

# Then, we keep checking until value of current index is >= top index
# If it is < top index, we update the result array, and then pop
# Else we push
# So for a monotinically increasing nums 2, the stack will have all indexes, result will be all -1s

def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    monotonic_stack = []
    result_array = [-1 for i in nums2]
    #print(result_array)

    for idx, val in enumerate(nums2):
        #print(monotonic_stack)
        if monotonic_stack:
            # print(monotonic_stack[-1])
            # print(nums2[monotonic_stack[-1]])
            # print(result_array[monotonic_stack[-1]])
            # Check until that top element is <= current element
            # Ensure that if all popped, we break
            while monotonic_stack and val > nums2[monotonic_stack[-1]]:
                #print("Checking")
                result_array[monotonic_stack[-1]] = val
                monotonic_stack.pop(-1)
                #print("Done")
            monotonic_stack.append(idx)
        else:
            monotonic_stack.append(idx)

    #print(result_array)
    # Now from Result array, return for elements in nums1
    # Using dictionary to lookup
    nge_dict = {}
    for idx, val in enumerate(nums2):
        nge_dict[val] = result_array[idx]

    final_array = []
    for val in nums1:
        final_array.append(nge_dict[val])

    #print(f"Final Array: {final_array}")
    return final_array


nextGreaterElement([3, 1, 2], [1, 2, 3, 4, 5, 6, 7])
nextGreaterElement([1, 3, 6, 7], [1, 3, 4, 2, 6, 7])
nextGreaterElement([0], [1, 2, 3, 9, 5, 0, 7])
