"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 
Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = 0
        min_count = len(nums) + 1 #As never possible or can set float('inf')
        L = 0

        for R in range(len(nums)):
            curr_sum += nums[R]
            while curr_sum >= target: #Keep trying with shrinking window as well
                # first update the minimum
                curr_window = (R - L) + 1
                min_count = min(min_count, curr_window)
                curr_sum -= nums[L] #Update some, when window shrunk, to subtract L
                L +=1

        return min_count if min_count!=(len(nums) + 1) else 0 #If mincount was len +1, then no such sub-array
        