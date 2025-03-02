from typing import List

# Time complexity: O(N*2^N)
# Memory is: O(N)

def add_subsets_helper(arr, i, curr_set, sub_sets):
    if i >= len(arr): #Last element crossed, fill sub sets
        sub_sets.append(curr_set.copy()) #Fill with a copy, otherwise with reference, can get modified
        return #Stop recursion
    
    # Choose current element
    curr_set.append(arr[i])
    add_subsets_helper(arr, i+1, curr_set, sub_sets)
    curr_set.pop() #Since we also want w/o current element
    # Do not choose current element
    # Now to avoid duplicates, we keep checking for the i which is not current element
    # This ensures we land to a unique branch w/o duplicates
    while i+1 < len(arr) and arr[i]==arr[i+1]:
        # We keep checking if the next element is same as current element
        # To check, make sure i+1 is not out of bounds
        # We increment i only if not out of bound
        i+=1
    add_subsets_helper(arr, i+1, curr_set, sub_sets)

def subsets(nums: List[int]) -> List[List[int]]:

    sub_sets = []
    curr_set = []
    nums.sort() #Sort it, so we know where duplicates are, so we can avoid them

    add_subsets_helper(nums, 0, curr_set, sub_sets)
    return sub_sets

print(subsets([1, 1, 1]))
print(subsets([1, 2, 3, 1]))
print(subsets([1, 2, 3, 5]))

        