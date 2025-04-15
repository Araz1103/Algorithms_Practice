from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all unique permutations of a list of numbers that may contain duplicates.

        This version uses a recursive approach to generate all possible permutations
        (including duplicates), and then uses a set to filter out duplicate permutations.

        Args:
            nums (List[int]): A list of integers, possibly containing duplicates.

        Returns:
            List[List[int]]: A list of all unique permutations.

        Approach:
            - Recursively generate all possible permutations.
            - For each recursive call, insert the current element at all positions
              in the smaller permutations.
            - Store the generated permutations in a set (converted to tuple for hashing)
              to eliminate duplicates.
            - Convert the final set back to a list of lists and return.

        Time Complexity:
            - Generating all permutations (including duplicates): O(n × n!)
              - n! permutations × O(n) insertion/copy time each.
            - Deduplication via set insertion and tuple conversion: O(n × n!)
            - Total: O(n × n!)

        Space Complexity:
            - Output storage: O(n × n!) for storing the result.
            - Set for deduplication: O(n × n!)
            - Recursive call stack: O(n)
            - Total: O(n × n!)

        Limitations:
            - Inefficient when many duplicates are present due to redundant work.
            - Generates all permutations before deduplication, increasing time and memory usage.

        Example:
            Input: nums = [1, 1, 2]
            Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        """

        
        def get_permutations(curr_index):

            if curr_index==len(nums)-1:
                return [ [nums[curr_index]] ]

            permutations = get_permutations(curr_index + 1)

            res_perms = []

            for perm in permutations:
                for idx in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(idx, nums[curr_index])
                    res_perms.append(perm_copy)
            return res_perms

        dups_perms = get_permutations(0)
        perms_set = set()
        for perm in dups_perms:
            perms_set.add(tuple(perm))

        return [list(perm) for perm in perms_set]
    

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all unique permutations of a list of numbers that may contain duplicates.

        This version uses backtracking with a frequency map to build only valid unique
        permutations directly, avoiding the need to deduplicate.

        Args:
            nums (List[int]): A list of integers, possibly containing duplicates.

        Returns:
            List[List[int]]: A list of all unique permutations.

        Approach:
            - Use a frequency hashmap (Counter-style) to track how many times each
              unique number can be used.
            - Perform DFS (backtracking) to build permutations by only adding numbers
              that have not yet been used up (count > 0).
            - Backtrack by undoing the choice after the recursive call.
            - Continue until the permutation length matches the input size.

        Time Complexity:
            - O(n × n!) in the worst case:
              - Each permutation is of length n.
              - Total unique permutations for duplicates: ≤ n!
              - Building and copying permutations takes O(n) each.

        Space Complexity:
            - Output storage: O(n × n!) for storing the result.
            - Frequency map: O(n) unique numbers at most.
            - Call stack: O(n) for recursion depth.
            - Temporary list for current permutation: O(n)
            - Total: O(n × n!)

        Advantages:
            - Much more efficient than brute-force + deduplication.
            - No need for post-processing or hash sets.
            - Avoids generating duplicate permutations from the start.

        Example:
            Input: nums = [1, 1, 2]
            Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        """

        # Keep a Hashmap of unique values and their counts
        # Backtrack to generate
        final_perms = []
        current_perms = []

        count_nums = {n:0 for n in nums}
        for n in nums:
            count_nums[n]+=1

        def dfs():
            #Base case when reached len of nums, perms is complete
            if len(current_perms)==len(nums):
                final_perms.append(current_perms.copy())
                return

            # Add from Hashmap one by one if allowed to take from it
            # Iterate through unique values in Hashmap
            for n in count_nums:
                if count_nums[n] > 0:
                    current_perms.append(n)
                    count_nums[n]-=1
                    dfs()
                    # back track
                    current_perms.pop()
                    count_nums[n]+=1
            return

        dfs()
        return final_perms

        
