"""
You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, 
but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [1,1,3,3]

Output: 4
Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:
Input: nums = [2,9,8,3,6]

Output: 16
Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        def get_max_rob(i, cache):
            if i==0: #max loot at 0th index
                return nums[0]

            if i==1: #max loot at 1st index
                return max(nums[0], nums[1])

            if i in cache:
                return cache[i]

            cache[i] = max(get_max_rob(i-1, cache), (get_max_rob(i-2, cache) + nums[i]))
            # max loot is either a combination of loot till 2 houses before + current house or max loot till last house
            return cache[i]

        return get_max_rob(len(nums)-1, {}) #last index
    
# Time Complexity is O(N) due to memoisation, as for each i, we just calculate once, no sub work done!
# Space Complexity is O(N), to store solution space for len(nums)
        