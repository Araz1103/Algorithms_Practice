"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# 4, 3, 2, 0, 5, 1
# Sets as values
# Take union of sets

# Initial
{4: {4},
 3: {3},
 2: {2},
 0: {0},
 5: {5},
 1: {1}}

# Step I (4)
{
 4: {4, 3, 5},
 3: {3},
 2: {2},
 0: {0},
 5: {5},
 1: {1}
}

# Step II (3)
{
 4: {4, 3, 5},
 3: {3, 4, 5, 2},
 2: [2],
 0: [0],
 5: [5],
 1: {1}
}

# Step III (2)
{
 4: {4, 3, 5},
 3: {3, 4, 5, 2},
 2: {3, 4, 5, 2, 1},
 0: [0],
 5: [5],
 1: {1}
}

# Step IV (0)
{
 4: {4, 3, 5},
 3: {3, 4, 5, 2},
 2: {3, 4, 5, 2},
 0: {0, 1},
 5: [5],
 1: {1}
}

# Step V (5)
{
 4: {4, 3, 5},
 3: {3, 4, 5, 2},
 2: {3, 4, 5, 2},
 0: {0, 1},
 5: {4, 3, 5},
 1: {1}
}

# Step VI (1)
{
 4: {4, 3, 5},
 3: {3, 4, 5, 2},
 2: {3, 4, 5, 2},
 0: {0, 1},
 5: {4, 3, 5},
 1: {1, 3, 4, 5, 2, 0}
}

# @end return the length of the longest value

# My approach
# Since we need to solve in O(n), we probably need to do multiple passes over nums
# In the first pass, we can store all elements as keys of a dict, the value is a list with [element]
# So we have unique values all stored
# If len(dict) is 1, then return 1
# Else:
# Iterate through the keys of the dict:
# For each element, first check if +1 or -1 is in the dict
# If it's not, then move to the next
# If it is, then dict[key] (for +- 1), extend your list with their value

# Now iterate and find the max length of values sets, that is the answer

# def longestConsecutive(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     elements_dict = {}
#     for element in nums:
#         elements_dict[element] = [element]

#     print("Starting", elements_dict)
#     for element in elements_dict:
#         print("@element: ", element)
#         if (element + 1) in elements_dict:
#             elements_dict[element].extend(elements_dict[element + 1])
#             #elements_dict[element + 1] = []

#         if (element - 1) in elements_dict:
#             elements_dict[element].extend(elements_dict[element - 1])
#             #elements_dict[element - 1] = []

#         print(f"elements dict now: {elements_dict}")

#     print(elements_dict)

#     max_chain = 0
#     for element, chain in elements_dict.items():
#         if len(chain) >= max_chain:
#             max_chain = len(chain)

#     print(max_chain)
#     return max_chain

# Problem with above is that this leads to duplicate entries and to solve that is tough

# Instead let's try
# For each element in the set 
# If it has a predecessor, then it means that it must be part of a sequence
# If it doesn't, then we can check onwards from that, to see how far can we go to check
# In this way, we can count for each element the unique sequences and return max length one

def longestConsecutive(nums):
    if not nums:
        return 0
    
    check_in_nums = {num: [] for num in nums}

    max_num = 0
    num_sequence = 0
    for num in nums:
        if num - 1 in check_in_nums: # This means it is a part of a sequence, ignore it
            continue
        else: #This means we can check if a sequence can be made from it
            check_num = num + 1
            while check_num in check_in_nums:
                check_num += 1

            # When it breaks out from above, that is our longest sequence starting from here
            check_in_nums[num] = [i for i in range(num, check_num)]
            len_sequence = (check_num - 1 - num)
            if len_sequence >= max_num:
                max_num = len_sequence
                num_sequence = num

    #@end can return the max sequence along with the length
    #print(check_in_nums)
    return check_in_nums[num_sequence], len(check_in_nums[num_sequence])


# Final Approach, use Sets instead of dictionaries
# No need for additional lists to store
# Just use the pointer and max length to come up with the consecutive sequence

def longestConsecutive(nums):
    if not nums:
        return [], 0
    
    num_set = set(nums)  # O(n)
    max_length = 0
    start_num = None

    for num in num_set:
        if num - 1 in num_set:  # Only process sequence starts
            continue  

        check_num = num + 1
        while check_num in num_set:  # Expand forward
            check_num += 1

        length = check_num - num  # Compute length
        if length > max_length:
            max_length = length
            start_num = num

    return list(range(start_num, start_num + max_length)), max_length

print(longestConsecutive([4, 3, 2, 0, 1, 9]))
print(longestConsecutive([1]))
print(longestConsecutive([-4, 3, 12, 10, 15, 11]))
print(longestConsecutive([-4, -3, 12, -1, 15, -2]))
print(longestConsecutive([4, -3, 12, 1, 15, -21]))
print(longestConsecutive([1,-8,7,-2,-4,-4,6,3,-4,0,-7,-1,5,1,-9,-3]))
print(longestConsecutive([-4, -3, -2, -1, 0, 1, -4, -4, -7, 0, -7, -8, -9, -6]))
print(longestConsecutive([-2,-4,-4,-4,-1,-3]))
print(longestConsecutive([-2,-4,-1,-3]))