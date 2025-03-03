"""
You are given an array of distinct integers nums and a target integer target. 
Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. 
Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

Input: 
nums = [2,5,6,9] 
target = 9

Output: [[2,2,5],[9]]
Explanation:
2 + 2 + 5 = 9. We use 2 twice, and 5 once.
9 = 9. We use 9 once.

Example 2:

Input: 
nums = [3,4,5]
target = 16

Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]
Example 3:

Input: 
nums = [3]
target = 5

Output: []
Constraints:

All elements of nums are distinct.
1 <= nums.length <= 20
2 <= nums[i] <= 30
2 <= target <= 30

"""

# Intuition
# @each element, either include it and keep including it until reach target or > target
# Otherwise do not include it and include the next element
# This allows taking uptil needed and then taking next
# As we know that it will only increase sum
# As all are positive

from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of numbers in 'nums' that sum up to 'target'.
        Each number in 'nums' can be used an unlimited number of times.
        
        Approach:
        - This uses **Backtracking with Choice Repetition Allowed**.
        - At each index 'i', we have 2 choices:
            1. Include nums[i] in the current combination (and stay at i to allow repeats).
            2. Skip nums[i] and move to the next index.
        - This recursive tree explores all combinations and prunes paths where the sum exceeds the target.

        Time Complexity:
        - In the **worst case**, we could be repeatedly using the smallest element.
        - Example: nums = [2], target = 20
          This would generate combinations like:
          [2, 2, 2, ..., 2] (10 times)
        - For each subset, appending and copying takes O(k) time (where k = length of the subset).
        - The number of recursive calls (nodes in the recursion tree) is bounded by the number of ways to make the target (exponential).
        - Overall: O(2^T) subsets where T = target (each number can be repeatedly chosen or skipped).
        - Each subset takes O(k) to copy — so total:
        
        **Time: O(2^T * k)**, where T = target and k = average length of a valid combination.

        Each number can be taken repeatedly, so the number of potential combinations can explode 
        if the numbers are small and the target is large.

        If nums = [2] and target = 20, you could have [2,2,2,2,...] (10 times).
        In general, number of combinations is roughly exponential in target 
        (because for each value, you could take it 0, 1, 2, ... Target times).
        This gives us a factor like: O(2^T)

        Each valid combination (subset) is stored in the final list. 
        Copying each combination takes O(k) time where k = length of the combination.

        In worst case, k = target/min(nums)
        Example: nums = [2], target = 20, max length = 10.

        Space Complexity:
        - Recursive call stack depth: up to O(T) if smallest number repeatedly chosen.
        - Storage for results: O(2^T * k)

        Overall Space: **O(2^T * k)**

        Args:
            nums (List[int]): List of distinct positive integers.
            target (int): The target sum we want to achieve.

        Returns:
            List[List[int]]: All unique combinations where sum equals target.
        """

        subsets = []

        def helper(i, sum_till_now, curr_set):
            
            # Base case: if we hit the exact target, store the valid subset
            if sum_till_now == target:
                subsets.append(curr_set.copy())
                return  # End this branch of recursion

            # Base case: if sum exceeds target, or we run out of numbers
            if sum_till_now > target or i >= len(nums):
                return  # Prune this branch

            # Choice 1: Take nums[i] (can repeat this number)
            curr_set.append(nums[i])
            helper(i, sum_till_now + nums[i], curr_set)

            # Choice 2: Skip nums[i] and move to the next index
            curr_set.pop()
            helper(i + 1, sum_till_now, curr_set)

        helper(0, 0, [])
        return subsets
