"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    positive_int = 1 # Is the smallest positive integer
    # First Sort the Array in increasing order
    # Then we keep iterating through it
    # If we encounter the current smallest positive int, we increase it by 1
    # The increased won't be present before, as this is sorted in increasing order
    nums.sort() #Is O(n logn)
    for num in nums:
        # If we encounter the smallest positive int, we increase pi += 1
        if num == positive_int:
            positive_int +=1
    return positive_int

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Using Cyclic Sort to ensure all nums are in correct position
    # The first number which is not, gives the position, which is the missing positive
    # [1, n] where n is len of list
    #print(nums)
    n = len(nums)
    for i, num in enumerate(nums):
        print(i, num)
        # We keep swapping until the number at this position is correct nums[i] - 1
        # Or it is not in the range [1, n]
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            # Swap nums[i] with the number at that position
            # We want to swap with what nums[i] belongs
            # Position of nums[i] is nums[i] - 1
            print("Swapping", nums)
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            print("Swapped", nums)
            print(nums[i])

        print(nums)
    
    #print(f"Final Nums: {nums}")
    # Now find the missing positive number
    for i, num in enumerate(nums):
        if nums[i] != i + 1:
            return i + 1
        
    # If all numbers are in their right place
    return n + 1
    
#print(firstMissingPositive([-1, 10, 2, 3, 5]))
#print(firstMissingPositive([-1, 0, 2, 3, 5, 1]))
#print(firstMissingPositive([-1, 4, 1, 10, 2, 3, 5]))
# print(firstMissingPositive([1, 10, 2, 3, 5, 8]))
# print(firstMissingPositive([-1, 110, 12, -3, 5]))
#print(firstMissingPositive([1,1]))
print(firstMissingPositive([4,5,1,2,3]))