"""
Given a string s, return the number of substrings within s that are palindromes.

A palindrome is a string that reads the same forward and backward.

Example 1:
Input: s = "abc"

Output: 3
Explanation: "a", "b", "c".

Example 2:
Input: s = "aaa"

Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa". 
Note that different substrings are counted as different palindromes even if the string contents are the same.

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

def check_palindrome(L, R, s):
    valid_substrings = []
    while L>=0 and R<len(s) and s[L]==s[R]:
        valid_substrings.append(s[L:R+1])
        L-=1 #Expanding L
        R+=1 #Expanding R

    return valid_substrings

def countSubstrings(s: str) -> int:
    # Check sub-string by expanding from each char, and checking if that is a palindrome or not
    # For odd and even lengths
    palindrome_substrings = []
    for idx in range(len(s)):

        # Checking Odd Length
        L, R = idx, idx
        # Here we take 2 chars, as middle of palindromes, then expand
        palindrome_substrings.extend(check_palindrome(L, R, s))

        # Checking Even Length
        L, R = idx, idx+1
        # Here we take 2 chars, as middle of palindromes, then expand
        palindrome_substrings.extend(check_palindrome(L, R, s))
    return palindrome_substrings, len(palindrome_substrings)

print(countSubstrings("araza"))
print(countSubstrings("aaa"))

        
