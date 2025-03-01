"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5

"""

# Intuition, building on the 2 sum problem
# Basically for each element, we take all the other elements in an array
# for each element, start from beginning and take all except that
# Now once we have these
# We can find all pairs satisfying a target in O(N) with O(N) space
# Have a hashmap and store current elements while iterating
# If target - current element in hashmap, then we know pair is there and we get that
# Is added to the outer current element, so we find triplet
# Overall O(N^2) complexity

from typing import Optional, List

def threeSum(nums: List[int]) -> List[List[int]]:
    triplets_set = set()

    for curr_idx, num in enumerate(nums):
        target = 0 - num
        curr_hashmap = {}
        curr_pairs = []
        for idx in range(len(nums)):
            if idx!=curr_idx:
                required = target - nums[idx]
                if required in curr_hashmap:
                    curr_pairs.append([nums[idx], required])
                else:
                    curr_hashmap[nums[idx]] = idx
        for pair in curr_pairs:
            triplet = [num]
            triplet.extend(pair)
            triplet.sort()
            triplets_set.add(tuple(triplet))

    return [list(triplet) for triplet in triplets_set]

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([1, 1, 1]))
print(threeSum([0, 0, 0]))

# Approach two, with in place
# If we first sort the input: O(N*LogN), < N^2

# Now for each number, we can search from the next one
# To avoid duplicate solutions, if the number is same as prev one, can skip over
# Iterate until 3rd last element (as for triplet need 3)
# -4, -1, -1, 0, 1, 2
# For -4, check over -1, -1, 0, 1, 2
# 2 sum problem with sorted, can find with 2 pointers in place
# -1, -1, 0, 1, 2
# L             R
# Keep trying while L < R
# If L + R make up target, good, otherwise we shift R if > Target or L if < Target
# If target found, then also we want to find more pairs
#   We can shift the L until it is at a unique value
#   nums[L]==nums[L-1]
#   Again checking L < R
def threeSum(nums: List[int]) -> List[List[int]]:
    triplet_sets = []
    nums.sort()

    for idx in range(len(nums)-2):
        if idx > 0 and nums[idx]==nums[idx-1]: #Same as previous num, since we want unique, skip
            continue
        L = idx + 1
        R = len(nums) - 1
        target = 0 - nums[idx]
        # Since L to R is sorted, can find relevant pairs with O(1) space
        while L < R:
            L_R_sum = nums[L] + nums[R]
            if L_R_sum == target:
                triplet_sets.append([nums[idx], nums[L], nums[R]])
                L+=1
                # Now let's move L, until we reach a new unique element
                # But make sure L < R
                while nums[L]==nums[L-1] and L < R:
                    L+=1 #If it was the same as previous,won't get a unique triplet
            elif L_R_sum > target:
                # Move R, since bigger, since sorted
                R-=1
            else:
                # Move L, since smaller, since sorted
                L+=1

    return triplet_sets

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([1, 1, 1]))
print(threeSum([0, 0, 0]))
