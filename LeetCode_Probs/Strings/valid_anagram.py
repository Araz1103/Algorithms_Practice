"""
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

# My Approach
# Basically get a list of the characters in s
# Get the list of characters in t
# They both have to match, the order doesn't
# To do it in O(n)

# Ist Approach
# Create a dict, and store chars with their counts for s
# Create a dict, and store chars with their counts for t
# These 2 dicts need to be identical

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dict_s = {}
    for char in s:
        if char not in dict_s:
            dict_s[char] = 1
        else:
            dict_s[char] += 1

    dict_t = {}
    for char in t:
        if char not in dict_t:
            dict_t[char] = 1
        else:
            dict_t[char] += 1

    if dict_t == dict_s:
        return True
    else:
        return False