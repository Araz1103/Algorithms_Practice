"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""


def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_len = len(s)
    t_len = len(t)
    if s_len and t_len:
        # Checking if both strings are not empty
        s_pointer = 0
        for i in range(t_len):
            # print(i)
            # print(t[i])
            if t[i] == s[s_pointer]:
                s_pointer +=1
                # Check if s_pointer reached @end
                # Don't need to check further then
                if s_pointer == len(s):
                    return True
        # If after iterating through t didn't reach, then return False
        return False
    else:
        # CASE I: s is empty and t is not
        if t_len and not s_len:
            return True # Can delete all of t to get s
        # CASE II: Both Empty
        elif not t_len and not s_len:
            return True # Don't need to delete from t to get s
        # CASE III: s is not empty and t is
        else:
            return False #Can't add to t
        
print(isSubsequence("b", "abc"))

# If we had a lot of s strings, then we pre-process t

from collections import defaultdict
import bisect

def isSubsequence(s: str, t: str) -> bool:
    # Step 1: Preprocess `t`
    char_positions = defaultdict(list)
    for i, char in enumerate(t):
        char_positions[char].append(i)

    # Step 2: Check each character in `s`
    prev_index = -1  # Tracks last matched position in `t`
    for char in s:
        if char not in char_positions:
            return False  # Character not in `t`

        # Find the next valid position using binary search
        pos_list = char_positions[char]
        next_pos = bisect.bisect_right(pos_list, prev_index)

        if next_pos == len(pos_list):
            return False  # No valid position found
        
        prev_index = pos_list[next_pos]  # Move forward in `t`
    
    return True

# bisect_right(positions, prev_index) finds the first index strictly greater than prev_index.
# Ensures that characters in s match in order with t.
# Efficient: O(log n) lookup per character in s.

# Test Cases
print(isSubsequence("aabc", "aaahbgaadcb"))  # True
print(isSubsequence("aabc", "aaahbgdb"))    # False


