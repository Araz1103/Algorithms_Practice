"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. 
In other words, 
an element is always considered to be strictly 
greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 
where the peak element is 2, or index number 5 where the peak element is 6.
 
Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""

# Intuition
# Since elements @end are always gt the out of bounds
# So we can always chase wherver the slope is increasing
# So 

#     |
#    ||   
#   |||

# If we consider above array
# We know that @end is the peak
# Now even if we landed somewhere else

#    |   
#    | |
#   |||||
#  ||||||
# Basically as long as we keep searching on side of increasing slope,
# We will land @peak
# So can do binary search O(Log(N))
# Basically check condition for slope
# Accordingly try searching left or right, wherever it is increasing

def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_len = len(nums)
    if nums_len==1:
        return 0 #Default Peak
    
    L = 0
    R = nums_len-1

    while L <= R:
        middle_element_idx = int(L + (R-L)/2)
        
        if middle_element_idx==0:
            # Check if gt next for peak
            if nums[middle_element_idx] > nums[middle_element_idx+1]:
                return middle_element_idx
            else:
                # We go to the right
                # So shift L
                L+=1
        elif middle_element_idx==nums_len-1:
            # Check if gt prev for peak
            if nums[middle_element_idx] > nums[middle_element_idx-1]:
                return middle_element_idx
            else:
                # We go to the left
                # So shift R
                R-=1
        else:
            if nums[middle_element_idx] > nums[middle_element_idx+1] and nums[middle_element_idx] > nums[middle_element_idx-1]:
                return middle_element_idx
            elif nums[middle_element_idx] > nums[middle_element_idx+1] and nums[middle_element_idx] < nums[middle_element_idx-1]:
                # Peak is towards Left
                # So shift R
                R-=1
            else:
                # Either Peak towards Right
                # Or if this is a valley, default check @Right
                # Peak is towards Right
                # So shift L
                L+=1

    return None #No Peak found
                
            
print(findPeakElement([1, 2, 3]))
print(findPeakElement([3, 2, 1]))
print(findPeakElement([0, 1, 2, 3, 4, -1, 1, 0, 2, 10, 3, 2]))