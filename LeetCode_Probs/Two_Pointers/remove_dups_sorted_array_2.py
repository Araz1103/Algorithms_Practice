"""
Given an integer array nums sorted in non-decreasing order, 
remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. 
You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

# Intuition, building on the sorted array dups 1 approach
# Basically keep a pointer which is counting the unique elements
# Allow for at most 2 occurences
# Now we know that the place after the 2 most occurences, is where the next unique element must come
# So our pointer, when it finds the next unique element, swaps it with the pointer which has the next place
# 1, 1, 1, 1, 2, 3, 4, 4, 4, 5, 6, 6 ,6
# L and R both @0
# R goes and finds the unique element
# Then R is again incremented, and we are keeping a counter
# Either the counter is 0 (2 occurences found) or another element found
# L + 1 has the place to swap with
# Basically if found another unique element or valid occurence of same
# Swap with L
# L+=1
# @end return L+1, as we know that will tell number of elements 

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 1
    
    L = 0
    unique_count = 1
    for R in range(1, len(nums)):
        print(nums, nums[L], L, unique_count)
        if nums[R]!=nums[L]:
            #or unique_count>0: 
            #means we found another unique element
            # Swap @L+1
            nums[L+1], nums[R] = nums[R], nums[L+1]
            print("New Unique Element!")
            # Unique Count is set back to 2
            unique_count = 1
            L+=1
        else:
            # Same unique element
            # Decrease the count
            unique_count-=1
            # If count is not gt 0
            # This means that not allowed any more elements
            # L stays here
            if unique_count >= 0: #If occurences allowed, we swap and shift L to next
                print("L+=1")
                # Swap @L+1
                nums[L+1], nums[R] = nums[R], nums[L+1]
                L+=1
        
    return L+1, nums

k, nums = removeDuplicates([1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6])
print(nums[:k])