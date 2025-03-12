"""
Searching in a rotated sorted array

1. If target is @middle -> Return it
2. If middle < right (right index @end): Means right side is sorted
    - If target is > middle and < right, then we can do a Binary Search on this right side and get target
    - If not, this means that the target is in the left array, adjust right pointer and continue
3. If middle > right (right index @end): Means left side is sorted
    - If target < middle and > left, then we can do a Binary Search on the left side and get target
    - If not, this means that target is in the right array, adjust left pointer and continue
"""

from typing import List

def binary_search(target, arr, l_p, r_p):
    print(f"IN BS with l_p: {l_p} r_p: {r_p}")
    while l_p <= r_p:
        m_p = int(l_p + (r_p - l_p)/2)

        if arr[m_p]==target:
            return m_p
        
        if arr[m_p] > target:
            r_p = m_p - 1
        else:
            l_p = m_p + 1

    return -1


def search(nums: List[int], target: int) -> int:
    l_p = 0
    r_p = len(nums) - 1

    while l_p <= r_p:
        m_p = int(l_p + (r_p - l_p)/2)
        print(f"MP is: {m_p}, val: {nums[m_p]}")

        if nums[m_p]==target:
            print("Found Target in OG Function!")
            return m_p
        
        if nums[m_p] < nums[r_p]:
            # Right side sorted
            if target > nums[m_p] and target <= nums[r_p]:
                print("On the Right Side, going for BS")
                # This means is in the right array, fetch it with BS
                return binary_search(target, nums, m_p+1, r_p)
            else:
                # Not on right side, so on left side
                print("Not on the Right Side, Will Search @Left")
                r_p = m_p - 1

        else:
            # Left side sorted
            if target < nums[m_p] and target >= nums[l_p]:
                print("On the Left Side, going for BS")
                # This means on left side, fetch with BS
                return binary_search(target, nums, l_p, m_p-1)
            else:
                print("Not on the Left Side, Will Search @Right")
                # Not on left side, so on right side
                l_p = m_p + 1

    return -1
        
#print(search([1, 2, 3, 4, 5], 0))
print(search([6, 7, 8, 1, 2, 3, 4, 5], 8))