# Time: O(n^2 * n!)
# Space: n! lists and each list has n numbers: O(n*n!)
def permutationsRecursive(nums):
    return helper(0, nums)
        
def helper(i, nums):   
    if i == len(nums):
        return [[]]
    
    resPerms = []
    perms = helper(i + 1, nums)
    for p in perms:
        for j in range(len(p) + 1):
            pCopy = p.copy()
            pCopy.insert(j, nums[i])
            resPerms.append(pCopy)
    return resPerms


# Time: O(n^2 * n!)
def permutationsIterative(nums):
    perms = [[]]

    for n in nums:
        nextPerms = []
        for p in perms:
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, n)
                nextPerms.append(pCopy)
        perms = nextPerms
    return perms

from typing import List

class Solution:
    # n! permutations exist!
    # For each permutation, we are inserting n elements
    # So time for insertion is n^2
    # So TC: O(n!*n^2)
    # SC: n!*n for storing outputs, n! each having n elements
    # For intermediate copies as well n!*n
    # So SC: O(n!*n)

    def permute(self, nums: List[int]) -> List[List[int]]:
        def get_permutations(curr_index):

            if curr_index==len(nums)-1:
                # Have reached last index
                return [[nums[curr_index]]]

            permutations_set = get_permutations(curr_index+1)

            # Basically for each permutation in the set
            # We take current number and add it at all possible positions
            result_permutations = []
            for perm in permutations_set:
                for idx in range(0, len(perm)+1):
                    new_perm = perm.copy()
                    new_perm.insert(idx, nums[curr_index])
                    result_permutations.append(new_perm)
            
            return result_permutations

        permutations = get_permutations(0)
        return permutations

    # Iteration, same time and space complexities
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Trying with iteration

        permutations = [[]]

        for n in nums:
            # For each number we try to insert in all permutations at all positions
            new_perms = [] #As if we keep appending to permutations while iterating over it, can cause run time issues
            for perm in permutations:
                for i in range(len(perm)+1): #Adding @end so len(perm) position needed
                    perm_copy = perm.copy()
                    perm_copy.insert(i, n)
                    new_perms.append(perm_copy)

            permutations = new_perms

        return permutations
        

        
