from typing import List

# Time complexity: O(N*2^N)
# Memory is: O(N)

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

        