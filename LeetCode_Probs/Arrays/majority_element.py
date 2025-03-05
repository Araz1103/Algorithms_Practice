"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

def get_majority_element(ip_list):
    # Sort the IP List in Ascending Order
    # The element in the middle will be majority, as it's occurences are >= n/2
    # This is assuming a majority element is always present

    ip_list.sort()
    print(ip_list, len(ip_list))
    return ip_list[(len(ip_list)//2) - 1]

print(get_majority_element([1, 2, 1, 3, 1]))
print(get_majority_element([1, 2, 2, 3, 2]))
print(get_majority_element([1, 2, 1, 3, 2, 2, 2, 4, 5, 4, 6, 4, 4, 5, 2, 2, 2, 2, 2, 2]))
print(get_majority_element([1, 2, 1, 3, 2, 2, 1, 4, 3, 3, 1, 5, 1, 1, 1]))

# OR Get a counter and check which has occurences > n/2
def get_majority_element(ip_list):
    cnt_dict = {}
    for num in ip_list:
        if num not in cnt_dict:
            cnt_dict[num] = 1
        else:
            cnt_dict[num] += 1

    for num, cnt in cnt_dict.items():
        if cnt > len(ip_list)//2:
            return num
        
print(get_majority_element([1, 2, 1, 3, 1]))
print(get_majority_element([1, 2, 1, 3, 1, 0, 1]))
print(get_majority_element([1, 2, 2, 3, 2]))
print(get_majority_element([1, 2, 1, 3, 2, 2, 2, 4, 5, 4, 6, 4, 4, 5, 2, 2, 2, 2, 2, 2, 2]))
print(get_majority_element([1, 2, 1, 3, 2, 2, 1, 4, 1, 1,  3, 3, 1, 5, 1, 1, 1]))