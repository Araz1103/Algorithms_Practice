"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt"

Example 1:
Input: nums = [9,1,4,2,3,3,7]

Output: 4
Explanation: The longest increasing subsequence is [1,2,3,7], which has a length of 4.

Example 2:
Input: nums = [0,3,1,3,2,3]

Output: 4
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
"""
from typing import List
class Solution:
    # Brute Force, 2^N, Exponential!
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Take the first element and 
        #keep checking against the ones on right
        #If there is an element > first element
        #When you do, you increment count and again split
        #Base case, when there are no elements on right
        
        max_sequence = []
        def check_any_increase(start_idx, sequence):
            nonlocal max_sequence
            start_element = nums[start_idx]
            sequence.append(start_element)
            if len(sequence) >= len(max_sequence):
                print("updating")
                print("Sequence", sequence)
                print("max sequence:", max_sequence)
                max_sequence = sequence[:]
                
            idx = start_idx + 1
            #print(start_idx, sequence)
            while idx < len(nums):
                if nums[idx] > start_element:
                    check_any_increase(idx, sequence)
                idx+=1
            sequence.pop()
        
        for idx in range(len(nums)):
            check_any_increase(idx, [])
        
        print(max_sequence)
        return len(max_sequence)
"""
Time Complexity Analysis
You start recursion from every index of nums, so you have O(N) recursive calls at the first level.
From each index, you recursively check all increasing elements to the right, leading to branching at each step.
The worst case occurs when each element is increasing, meaning you can make 2^N recursive calls in the worst case (each number either belongs to a subsequence or doesn’t).
Thus, the time complexity is O(2^N), which is exponential.
"""

class Solution:
    # Bottom Up DP Approach
    def lengthOfLIS(self, nums: List[int]) -> int:
        # We know that if we start @last element
        # Num sub-sequences from there is technically 1 (itself)
        # From second last element, depends if it is < last element
        # If not, we can only conclude that we can take itself
        # So LIS[i] = max(1, 1 + LIS[i+1], 1 + LIS[i+2], .. 1 + LIS[n-1])
        # Above for all where if nums[i] < nums[i+x]
        # Example: 11, 12, 14, 13
        # Indexes: 0, 1, 2, 3
        # LIS[3] = 1 Since it is n-1
        # LIS[2] = 1 since nums[2] >= nums[3]
        # LIS[1] = max(1, 1 + LIS[2], 1 + LIS[3]) 
        # since nums[1] < nums[2], nums[1] < nums[3]
        # LIS[0] = max(1, 1 + LIS[1], 1 + LIS[2], 1 + LIS[3])
        # Be careful, we need LIS from those points where element is >
        # Because after that point we don't know what is greater than those elements
        # Ex: 11 < 14, but post 14 we don't want to re-compute which elements are gt 14
        # Since we calculated LIS @14, we can use that
        # So complexity becomes O(N^2)

        LIS_Map = [0 for i in range(len(nums))]
        for idx in range(len(nums)-1, -1, -1):
            to_compare_list = [1] # 1 for this element as a sub-sequence
            for jdx in range(idx+1, len(nums)):
                # We check all elements > idx element
                # We want max of all such 1 + LIS[jdx] elements
                if nums[idx] < nums[jdx]:
                    to_compare_list.append(1 + LIS_Map[jdx])
            LIS_Map[idx] = max(to_compare_list)
        print(LIS_Map)
        return max(LIS_Map)


