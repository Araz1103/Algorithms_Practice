from typing import List

# Time complexity: O(N*2^N)
# Memory is: O(N)

"""
Generates all possible subsets (the power set) of a given list using backtracking.

Time Complexity:
- O(N × 2^N), where:
    - 2^N is the number of subsets.
    - Each subset takes up to O(N) time to copy and append.

Space Complexity:
- Output storage (sub_sets): O(N × 2^N)
    - We store 2^N subsets.
    - Each subset can be up to size N.
- Call stack: O(N), due to recursion depth.
- curr_set (temporary list used in recursion): O(N)
    - This is reused and does not add to total output space.

Key Notes:
- curr_set is dynamically modified (append/pop) in the recursion.
- curr_set is explicitly copied (`curr_set.copy()`) before adding to output to avoid referencing the same list object.
"""


def add_subsets_helper(arr, i, curr_set, sub_sets):
    if i == len(arr): #Last element crossed, fill sub sets
        sub_sets.append(curr_set.copy()) #Fill with a copy, otherwise with reference, can get modified
        return #Stop recursion
    
    # Choose current element
    curr_set.append(arr[i])
    add_subsets_helper(arr, i+1, curr_set, sub_sets)
    curr_set.pop() #Since we also want w/o current element
    # The pop is important to backtrack!
    # Do not choose current element
    add_subsets_helper(arr, i+1, curr_set, sub_sets)

def add_subsets_helper(arr, i, curr_set, sub_sets):
    if i == len(arr): #Last element crossed, fill sub sets
        sub_sets.append(curr_set.copy()) #Fill with a copy, otherwise with reference, can get modified
        return #Stop recursion
    
    # Do not choose current element
    add_subsets_helper(arr, i+1, curr_set, sub_sets)
    # Choose current element
    curr_set.append(arr[i]) #Since we also want with current element
    add_subsets_helper(arr, i+1, curr_set, sub_sets)
    curr_set.pop() #Need this to backtrack!

def subsets(nums: List[int]) -> List[List[int]]:

    sub_sets = []
    curr_set = []

    add_subsets_helper(nums, 0, curr_set, sub_sets)
    return sub_sets

print(subsets([1, 2, 3]))
print(subsets([1, 2, 3, 5]))

        