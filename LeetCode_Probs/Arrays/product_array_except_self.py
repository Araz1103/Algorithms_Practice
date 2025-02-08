"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


def get_product_list(ip_list):
    prod = 1
    for i in ip_list:
        prod = prod * i

    return prod

# Solution 1: Brute Force, Slow
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    print(f"IP: {nums}")
    answer_array = []
    for i in range(len(nums)):
        print(i)
        sub_array = []
        print(nums[:i])
        print(nums[i:])
        sub_array.extend(nums[:i])
        sub_array.extend(nums[i+1:])
        print("Sub Array", sub_array)
        answer_array.append(get_product_list(sub_array))

    return answer_array
    
print(productExceptSelf([1,2,3,4]))

# Solution 2: Hopefully Faster
# 4 Cases (Zero(es) in List (3 Sub Cases), Zero(es) not in list)
# CASE I: List is only zeroes: Return Zero in all elements
# CASE II: If only 1 zero in list
# Compute product of all non-zero elements
# Iterate through list, if element is not a zero, return zero
# If element is zero, return product
# CASE III: More than 1 zero in list
# Return Zero in all elements
# CASE IV: Compute product of all elements
# Iterate through list, return product divided by element

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    print(f"IP: {nums}")
    answer_array = []
    list_product = 1
    has_zero = 0
    count_zero = 0
    for num in nums:
        if num == 0:
            has_zero = 1
            count_zero +=1
        else:
            list_product *= num

    # CASE I and II
    if count_zero == len(nums) or count_zero > 1:
        return [0 for i in range(len(nums))]

    # CASE III
    if has_zero:
        for num in nums:
            if num != 0:
                answer_array.append(0)
            else:
                answer_array.append(list_product)
    # CASE IV
    else:
        for num in nums:
            answer_array.append(list_product//num)

    return answer_array

print(productExceptSelf([-1,2,3,4]))

print(productExceptSelf([-1,2,3,4,0]))
    


        