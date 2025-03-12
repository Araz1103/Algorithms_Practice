from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # We know if we use XOR
        # All the numbers coming twice XOR out to 0
        # And the numbers coming once remain as their xor with 0 is the number itself
        # Now since final output will be uniquenum xor uniquenum2, we have their xor, not the num
        

        if len(nums) == 2:
            return nums

        # Now when we have our final xor output
        # We check which bit in it is 1 at which place
        # Based on that, we can have 2 groups
        # Our unique numbers will be in separate groups
        # Since 1 of them has a 1 at that place and the other has a 0
        # all others can be in either group
        # If we xor the groups, we get a and b, and return them in the array
        xor = nums[0]
        for num in nums[1:]:
            xor^= num

        # Now to get which bit here is 1 (where the unique number bits differed)
        diff_bit = 1 #00001
        while not (xor & diff_bit): #When this is 1, we found the bit where there is a 1
            diff_bit = diff_bit << 1 #shift to left to check

        # So now to get our groups a and b
        a = 0 #Start @0, as 0 xor number is number itself
        b = 0
        for num in nums:
            if (num & diff_bit):
                a = a^num
            else:
                b = b^num
        return [a,b]

         

        