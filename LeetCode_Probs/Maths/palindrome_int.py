"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:
-231 <= x <= 231 - 1
 
Follow up: Could you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Approach I
        # Make it a string and use 2 pointers to check
        x_str = str(x)
        s,e = 0, len(x_str)-1

        while s <= e:
            if x_str[s]!=x_str[e]:
                return False

            s+=1
            e-=1
        return True
    
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Approach II: Without converting to string
        # %10 gives the right most digit
        # If I divide by 10 and take the floor then the remaining digits are gotten
        # I keep doing this until get 0
        # So I have all the digits in the order along with the highest place (100s or 1000s or 10s, etc)
        # I build the reverse number back and compare with the original number
        # I check if number is < 0 then negative so then False
        # For all positive I can do that

        # All negative are false
        if x < 0:
            return False

        # Single digit positive int true
        if x <= 9:
            return True

        num_digits = 0
        digits = []
        og_x = x

        while x!=0:
            # right most digit
            digits.append(x%10)
            # Now to truncate x, remove right most and keep all @left
            x = x//10 #Python floors this
            num_digits+=1

        # Now we know highest power and we have all the digits in the number
        # Build it up in reverse and compare with original x
        # If same return True else False
        print(digits, num_digits)
        new_x = 0
        for digit in digits:
            new_x += (10**(num_digits-1))*digit
            num_digits-=1
        print(new_x)
        return new_x == og_x


        


