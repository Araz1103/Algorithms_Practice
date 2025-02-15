"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""

def isPalindrome(s: str) -> bool:
    # We can have 2 pointers, one starting @end, one @beginning
    # Basically checking that @element has to be same from starting and beginning
    # If the element is not alpha numeric, ignore and move forward

    start_pointer = 0
    end_pointer = len(s) - 1

    while start_pointer <= end_pointer:
        
        while not s[start_pointer].isalnum():
            start_pointer +=1
            if start_pointer >= len(s):
                return True

        while not s[end_pointer].isalnum():
            end_pointer -=1
            if end_pointer < 0:
                return True

        start_char = s[start_pointer]
        end_char = s[end_pointer]

        if start_char.lower() != end_char.lower():
            return False
        
        start_pointer +=1
        end_pointer -=1

    # If until now we didn't return False
    # This means all elements matched
    # Now can return True
    return True

print(isPalindrome("araz"))
print(isPalindrome("arazara"))
print(isPalindrome("Was it a car or a cat I saw?"))
print(isPalindrome("   sa  "))
print(isPalindrome("   sas  "))
print(isPalindrome("   s a !s  "))
print(isPalindrome("     "))
print(isPalindrome(""))