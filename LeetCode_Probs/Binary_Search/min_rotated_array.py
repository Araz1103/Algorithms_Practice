"""
Finding min in a rotated sorted array
Given all elements are unique


# Approach, Try to do 2 Binary Searches 
# If middle is min element (we know min is where left and right to it are both greater)
# If not, do Binary Searches in the left and right sub-arrays
"""
from typing import List

def check_is_min(idx, arr):
    # If left of idx exists and right of idx exists, and they both are gt: True
    # If only right of idx exists and is gt: True
    # If only left of idx exists and is gt: True
    # If neither exists, then also True

    if len(arr)==1:
        return True
    
    left_idx = idx - 1
    right_idx = idx + 1

    current_val = arr[idx]

    if left_idx >=0 and right_idx < len(arr):
        left_val = arr[left_idx]
        right_val = arr[right_idx]

        if left_val > current_val and right_val > current_val: 
            return True
        else:
            return False
        
    if left_idx >=0:
        left_val = arr[left_idx]
        if left_val > current_val:
            return True
        else:
            return False
        
    if right_idx < len(arr):
        right_val = arr[right_idx]
        if right_val > current_val:
            return True
        else:
            return False


def findMin(nums: List[int]) -> int:
    left_idx = 0
    right_idx = len(nums) - 1

    while left_idx <= right_idx:
        mp_idx = int(left_idx + (right_idx - left_idx)/2)
        mp_val = nums[mp_idx]
        left_val = nums[left_idx]
        right_val = nums[right_idx]

        print(f"Middle IDX: {mp_idx}")
        print(f"Middle Value: {mp_val}")
        print(f"Left Val: {left_val}")
        print(f"Right Val: {right_val}")

        # Check if is_min
        # If left of middle element > and right of middle element is >

        if check_is_min(mp_idx, nums):
            print("Found Min!")
            return mp_idx, mp_val
        
        if mp_val > right_val: #min is towards right array
            left_idx  = mp_idx + 1
        else: #min is towards left array
            right_idx = mp_idx - 1

    return -1, None

print(findMin([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, -1000])) 

