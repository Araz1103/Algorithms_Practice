"""
You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.

Example 1:

Input: digits = [1,2,3,4]

Output: [1,2,3,5]
Explanation 1234 + 1 = 1235.

Example 2:

Input: digits = [9,9,9]

Output: [1,0,0,0]
Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_int = ""
        for digit in digits:
            string_int+=str(digit)

        string_int = int(string_int) + 1
        return [int(digit) for digit in str(string_int)]

    def plusOne(self, digits: List[int]) -> List[int]:
        # Carry addition
        # Start @end, keep a carry
        # Add +1 and check if a digit is 9 or not
        # If it is, we adjust with carry
        new_digits = []
        carry = 1
        for digit in digits[::-1]:
            if digit+carry==10:
                new_digits.append(0)
                carry=1
            else:
                new_digits.append(digit+carry)
                carry=0

        if carry: #@end check if a carry remains, then add (will be 1 or 0)
            new_digits.append(carry)

        return new_digits[::-1]