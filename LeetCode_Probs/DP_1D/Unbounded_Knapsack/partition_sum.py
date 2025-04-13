"""
You are given an array of positive integers nums.

Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). 
Otherwise, return false.

Example 1:

Input: nums = [1,2,3,4]

Output: true
Explanation: The array can be partitioned as [1, 4] and [2, 3].

Example 2:

Input: nums = [1,2,3,4,5]

Output: false
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 50

"""
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Since we want 2 partitions of equal sums
        # Each partition should be  sum of array/2
        # I. Check if sum of array is even, if odd then anyways not possible as integers
        # II. So the aim is to check if any we can take any combination adding up to half sum
        # Similar to Knapsack, where we can choose an element or not, and have some capacity, 
        # in our case the sum, and we check the remaining sum
        # Once we find a combination, we automatically know the rest of elements is the other partition
        # Since total sum of array is 2*half sum

        # If number of elements is <= 1, not possible
        if len(nums) <= 1:
            return False

        sum_array = sum(nums)
        if sum_array%2!=0:
            return False #Sum of Array is Odd, cannot have 2 partitions of equal sums

        half_sum = int(sum_array/2)

        # Can add cache based on the num index at and remaining sum here

        def check_sum(num_index, remaining_sum, cache):
            
            # Check if we reached final condition
            if remaining_sum==0:
                return True #Found elements adding up to half sum

            # Check @end of nums, cannot take any more num
            if num_index >= len(nums):
                return False #cannot take anymore

            # Check @cache
            if cache[num_index][remaining_sum] != -1:
                return cache[num_index][remaining_sum]

            # Have 2 choices, include this number or skip it

            # Skip this number
            found_partition_skip = check_sum(num_index + 1, remaining_sum, cache)

            # Include this number
            found_partition_include = False
            # Check if we can include it and not exceed sum
            if nums[num_index] <= remaining_sum:
                found_partition_include = check_sum(num_index + 1, remaining_sum - nums[num_index], cache)

            # If we found from either of these ways, valid
            cache[num_index][remaining_sum] = found_partition_skip or found_partition_include
            return cache[num_index][remaining_sum]

        # Initialise cache
        cache = [[-1]*(half_sum + 1) for _ in range(len(nums))]
        # Time complexity is: O(n * target (half sum))
        return check_sum(0, half_sum, cache)

        
            


