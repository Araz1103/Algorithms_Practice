"""
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array 
such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # if k is 0, this means window of size 1, but cannot have 2 distict indices
    if k==0:
        return False

    # Now Window is of size k+1
    L = 0
    window = set()

    for R in range(len(nums)):
        if (R - L + 1) > (k+1): #Window Exceeded
            window.remove(nums[L]) # Sliding the window, so remove L
            L+=1

        if nums[R] in window:
            return True

        window.add(nums[R]) #Add @Window

    return False

            

        