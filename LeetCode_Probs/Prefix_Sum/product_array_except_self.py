"""
Products of Array Except Self
Given an integer array nums, 
return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]

Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
"""

from typing import List
# Intuition
# 2 Approaches

# Ist: 
# Store the product of all non-zero elements
# If there is a zero, have that flag
# Then in 1 pass, value is product/element if no 0s
# If 0s, then all are 0, and val at 0 elements is the non-zero product
def productExceptSelf(nums: List[int]) -> List[int]:
    non_zero_product = 1
    has_zero = False
    for num in nums:
        if num!=0:
            non_zero_product*=num
        else:
            has_zero = True

    product_wo_self_array = []
    for num in nums:
        if has_zero and num!=0:
            product_wo_self_array.append(0)
        elif has_zero and num==0:
            product_wo_self_array.append(non_zero_product)
        else:
            product_wo_self_array.append(non_zero_product//num)

    return product_wo_self_array

print(productExceptSelf([1, 1, 1, 2]))
print(productExceptSelf([1, 1, 0, 2]))
print(productExceptSelf([1,2,4,6]))
print(productExceptSelf([-1, 1, 1, 2]))

# IInd:
# For each element, the product w/o element is pre-fix product and post-fix product (w/o including the element)
# Make Pre-fix and Post-Fix Product Arrays in this manner
# @each element, give the product of them

def productExceptSelf(nums: List[int]) -> List[int]:
    prefix_product_array = [None]
    # For Leftmost we store None
    current_product = nums[0]
    for num in nums[1:]:
        prefix_product_array.append(current_product)
        current_product*=num

    postfix_product_array = [1 for i in range(len(nums))]
    postfix_product_array[-1] = None
    # For Rightmost we store None
    current_product = nums[-1]
    for idx in range(len(nums)-2, -1, -1):
        postfix_product_array[idx] = current_product
        current_product*=nums[idx]

    # print(prefix_product_array)
    # print(postfix_product_array)
    # Now for each element in nums, we know it is prefix*postfix
    # Check if prefix is None, return postfix
    # If postfix is None, return pre-fix
    product_wo_self_array = []
    for idx in range(len(nums)):
        product_wo_self = 1
        prefix_product = prefix_product_array[idx]
        if prefix_product is not None:
            product_wo_self*=prefix_product
        
        postfix_product = postfix_product_array[idx]
        if postfix_product is not None:
            product_wo_self*=postfix_product

        product_wo_self_array.append(product_wo_self)

    return product_wo_self_array

print(productExceptSelf([1, 1, 1, 2]))
print(productExceptSelf([1, 1, 0, 2]))
print(productExceptSelf([1,2,4,6]))
print(productExceptSelf([-1, 1, 1, 2]))
        