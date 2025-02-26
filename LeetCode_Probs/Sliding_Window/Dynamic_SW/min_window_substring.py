"""
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s 
such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 
Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
from collections import Counter, defaultdict

def check_has_dict(s_dict, t_dict):
    for t_key, t_val in t_dict.items():
        if s_dict.get(t_key, 0) < t_val:
            return False
    return True

def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if len(t) > len(s):
        return "" #No Substring Possible
    
    if len(t)==len(s)==1:
        if t==s:
            return t
        else:
            return ""
    
    t_dict = Counter(t)
    L = 0
    min_substring = ""
    min_substring_len = len(s)+1
    curr_dict = defaultdict(int)
    for R in range(len(s)):
        #print(min_substring)
        curr_dict[s[R]]+=1

        # Now let's increment L until this is not true
        while check_has_dict(curr_dict, t_dict): #this means valid window
            window_len = R - L + 1
            if window_len <= min_substring_len:
                min_substring = s[L:R+1]
                min_substring_len = len(min_substring)
            curr_dict[s[L]]-=1
            L+=1

    return min_substring

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))

s = "ADOBECODEBANC"
t = "ABBC"
print(minWindow(s, t))

s = "ADOBECODEBANC"
t = "A"
print(minWindow(s, t))

s = "ADOBEDOBCAA"
t = "ABBC"
print(minWindow(s, t))

s = "ADOBEDOBCAA"
t = "ABC"
print(minWindow(s, t))

s = "cabwefgewcwaefgcf"
t = "cae"
print(minWindow(s, t))

def minWindowOptimal(s, t):
    if len(t) > len(s):
        return ""

    t_dict = Counter(t)  # Count frequency of characters in t
    curr_dict = defaultdict(int)  # Current window's character frequency

    required_chars = len(t_dict)  # Unique characters in t
    formed_chars = 0  # Number of characters that have met their required frequency

    L = 0
    min_substring = ""
    min_substring_len = float("inf")

    for R in range(len(s)):
        curr_dict[s[R]] += 1

        # If this character is now fully matched, increase formed_chars
        if curr_dict[s[R]] == t_dict[s[R]]:
            formed_chars += 1

        # Try shrinking the window if it's valid
        while formed_chars == required_chars:
            window_len = R - L + 1
            if window_len < min_substring_len:
                min_substring = s[L:R+1]
                min_substring_len = window_len

            # Shrink window by moving L
            curr_dict[s[L]] -= 1
            if s[L] in t_dict and curr_dict[s[L]] < t_dict[s[L]]:
                formed_chars -= 1  # This character is no longer fully satisfied
            L += 1

    return min_substring

            


        