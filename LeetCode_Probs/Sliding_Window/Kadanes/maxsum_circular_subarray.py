"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. 
Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. 
Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 

Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""


# # Intuition
# # Normal Kadanes, with 1 change
# # Instead of stopping @end of array
# # Keep increasing Right pointer, until R < L
# # So basically go around till 1 less than the Left Pointer

# # So your R pointer has 2 versions
# # 1 is the actual incrementation version
# # You try till at least nums
# # the other is the index version, which tells the array index to use
# # icrementation version % N
# def maxSubarraySumCircular(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     curr_sum = 0
#     max_sum = float("-inf")

#     L = 0
#     R = 0
#     R_Index = R%len(nums)

#     # You keep trying until R is < nums
#     # or R >= nums and R_Index < L

#     while ( (R < len(nums)) or (R >= len(nums) and R_Index < L)):
#         print(f"L is: {L}, num is: {nums[L]}")
#         print(f"R is {R}")
#         print(f"R Index is: {R_Index}, num is: {nums[R_Index]}")
#         if curr_sum < 0:
#             curr_sum = 0
#             L = R_Index
#         curr_sum += nums[R_Index]    
#         if curr_sum > max_sum:
#             max_sum = curr_sum
#         R+=1
#         R_Index = R%len(nums)
#         print(f"Cur Sum is: {curr_sum} and max_sum is: {max_sum}")
#         print(f"@end L is: {L}, num is: {nums[L]}")
#         print(f"@end R is {R}")
#         print(f"@end R Index is: {R_Index}, num is: {nums[R_Index]}")

#     return max_sum

def maxSubarraySumCircular(nums):
    """
    Returns a tuple (max_sum, L, R) where:
      - max_sum is the maximum subarray sum for the circular array,
      - L is the start index, and
      - R is the end index (indices refer to the original array indices).
    """

    # --- Step 1: Compute the maximum subarray sum (linear) using Kadane's algorithm.
    max_kadane, kadane_L, kadane_R = kadane(nums)
    #print(max_kadane)
    
    # --- Step 2: Compute the total sum of the array.
    total_sum = sum(nums)
    
    # --- Step 3: Compute the minimum subarray sum.
    # To do this, we apply Kadane's algorithm on the negated array.
    # The maximum sum on -nums is the negative of the minimum sum on nums.
    min_kadane, min_L, min_R = kadane([-num for num in nums])
    min_kadane = -min_kadane  # Reverse the sign back to get the actual minimum subarray sum
    #print(min_kadane)
    # --- Step 4: Edge case where all numbers are negative.
    # If total_sum equals the negative of the min_kadane,
    # it means that the minimum subarray is the entire array.
    #print(total_sum, min_kadane)
    if total_sum == min_kadane:
        #print("All Negative!")
        return max_kadane, kadane_L, kadane_R

    # --- Step 5: Calculate the maximum circular subarray sum.
    # This is done by subtracting the minimum subarray sum from the total sum.
    circular_max = total_sum - min_kadane

    # --- Step 6: Determine which subarray (normal or circular) gives the best sum.
    if circular_max > max_kadane:
        # The circular subarray is better.
        # Its start is the element after the end of the minimum subarray,
        # and its end is the element before the start of the minimum subarray.
        start = (min_R + 1)# % len(nums)
        end = (min_L - 1)# % len(nums)
        return circular_max, start, end
    else:
        # The normal (linear) subarray is better.
        return max_kadane, kadane_L, kadane_R


def kadane(nums):
    """
    Implements Kadane's algorithm to find the maximum subarray sum
    for a linear (non-circular) array and returns a tuple (max_sum, start, end)
    where 'start' and 'end' are the indices of the subarray.
    """
    max_sum = float("-inf")  # Best sum seen so far
    curr_sum = 0             # Sum of the current subarray
    start = end = temp_start = 0  # Initialize indices

    for i, num in enumerate(nums):
        # If adding the current number makes the current sum negative,
        # it's better to start a new subarray from the current number.
        if curr_sum < 0:
            curr_sum = 0
            temp_start = i  # Potential new start index
        
        # Add the current number to the current subarray sum.
        curr_sum += num

        # If the current subarray sum is better than what we've seen,
        # update the best sum and the corresponding indices.
        if curr_sum > max_sum:
            max_sum = curr_sum
            start, end = temp_start, i

    return max_sum, start, end


# Example test cases
# print(maxSubarraySumCircular([1, -2, 3, -2]))  # Output: (3, 2, 2)
# print(maxSubarraySumCircular([5, -3, 5]))      # Output: (10, 0, 2)
# print(maxSubarraySumCircular([-3, -2, -3]))    # Output: (-2, 1, 1)
# print(maxSubarraySumCircular([5, 2, -3, 5]))   # Output: (9, 0, 3)


print("------------Circular Sub Array-----------")
ip = [1, 2, 29, 3, -40, 2, 1]
print(maxSubarraySumCircular(ip))
print("-----------------")
ip = [-11, -5, -29, -3, -40, -2, -1]
print(maxSubarraySumCircular(ip))
print("-----------------")
ip = [1, 5, -2, 3, -40, 2, -1]
print(maxSubarraySumCircular(ip))
print("-----------------")
ip = [5, 2, -3, 5]
print(maxSubarraySumCircular(ip))
print("-----------------")
print(maxSubarraySumCircular([-3, -2, -3])) 