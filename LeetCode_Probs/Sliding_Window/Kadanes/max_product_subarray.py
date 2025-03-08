"""
Given an integer array nums, find a subarray that has the largest product within the array and return it.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

Example 1:

Input: nums = [1,2,-3,4]

Output: 4
Example 2:

Input: nums = [-2,-1]

Output: 2
Constraints:

1 <= nums.length <= 1000
-10 <= nums[i] <= 10

"""
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min, curr_max = 1, 1
        max_res = nums[0] #initialise with an element from nums, since if all negative can't take 1 

        for element in nums: 
            # we keep track of curr max and curr min, due to negatives
            tmp_curr_max = curr_max #as we update below
            # we check with the current element, current * prev max or min
            # only these 3 combinations can lead to a maximum
            curr_max = max(element, element*curr_max, element*curr_min)
            curr_min = min(element, element*tmp_curr_max, element*curr_min)
            # After each element, check if we get a new max
            max_res = max(max_res, curr_max)
            
        return max_res #Since just 1 iteration, O(N), had we done brute force: O(N^2)
        