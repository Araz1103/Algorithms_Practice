from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Approach I: Hashing
        # In O(N), in a set, put all elements
        # Then iterate from 0 to N
        # Whichever is missing return that
        # But space complexity is O(N)
        num_set = set(nums)
        for i in range(len(nums)+1):
            if i not in num_set:
                return i

        # Approach II: Using a bitwise operator to solve in O(1) space
        # XOR: When 2 identical numbers are XOR'ed, we get 0
        # Since 0, 0 is 0 and 1, 1 is also 0
        # Also when you XOR 0 and number, you get the number back
        # 0^3 = 3
        # So 5^5^3 = 0^3 = 3
        # Also this is order invariant
        # So 5^3^5 = 3
        # So now we can take from 0 to n
        # and we can take our numbers
        # We xor all of these
        # All numbers in 0 to n cancel out to 0
        # 1 number remains, and after XORing with 0, we get that
        
        all_nums = [i for i in range(len(nums)+1)] + nums
        # xor all of these, and left is the missing number
        curr_result = all_nums[0]
        for element in all_nums[1:]:
            curr_result = curr_result ^ element

        return curr_result # Now this will have the missing number

        # Approach 3
        # Take sum from 0 to n and subtract sum of nums
        # What you're left with is the missing number
        # O(N) time complexity for sums and O(1) memory!
        return sum([i for i in range(len(nums)+1)]) - sum(nums)


        