"""
Two Sum

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

        # O(N^2) Solution
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # If we wanted to do in 1 pass
        # Assuming there is always a pair
        # Then let's just search once
        # At each element we know what the element is and what is required to get to target
        # If we already encountered the required element before, we know both indexes and we can return
        store_target_pairs = {} #In keys store element and index @value
        
        # Only 1 Pass so is O(N) !!
        for idx, element in enumerate(nums):
            target_element = target - element
            # If target element already in target_pairs
            # We can use it
            if target_element in store_target_pairs: #Target complete
                return [store_target_pairs[target_element], idx]
            else: #Let's add it in dict and keep checking
                # If element already in dict, then don't add, as we want smaller indexes first
                if element not in store_target_pairs:
                    store_target_pairs[element] = idx
