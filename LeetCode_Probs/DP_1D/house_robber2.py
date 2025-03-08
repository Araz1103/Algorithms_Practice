"""
You are given an integer array nums where nums[i] represents the amount of money the ith house has.
The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, 
but you cannot rob two adjacent houses because the security system will automatically alert the police 
if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [3,4,3]

Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. 
The maximum you can rob is nums[1] = 4.

Example 2:
Input: nums = [2,9,8,3,6]

Output: 15
Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses. 
The maximum you can rob is nums[1] + nums[4] = 15.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

"""
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Using House Robber 1 solution
        # Just run it from index 1 to n-1
        # Then from 0 to n-2
        # Then take the max from either of them
        # 2, 9, 8, 3, 6
        # First let's see max from 9,8,3,6 -> Is allowed as we never consider 2
        # Then let's see max from 2,9,8,3 -> Is allowed as we never consider 6
        # Return max from both

        def get_max_rob(i, nums, cache):
            if i==0:
                return nums[i]

            if i==1:
                return max(nums[0], nums[1])

            if i in cache:
                return cache[i]

            cache[i] = max( get_max_rob(i-1, nums, cache) ,(get_max_rob(i-2, nums, cache) + nums[i]) )

            return cache[i]

        if len(nums)==1:
            return nums[0]

        rob1 = get_max_rob(len(nums[1:])-1, nums[1:], {}) #O(N)
        rob2 = get_max_rob(len(nums[:-1])-1, nums[:-1], {}) #O(N)
        return max(rob1, rob2) #Total Time & Space complexity is still O(N)