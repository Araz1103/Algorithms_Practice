"""
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length
"""
# Intuition
# Keep a window
# @Each window, we find the max occuring element
# The number of replacements to make sure all elements in window are that are
# Window Size - Freq of Max Occuring Element
# If #Replacements <= K: we know this is a valid window
# Len of this window can be considered for max possible with replacements
# Otherwise, we shrink (L +=1), until window is valid!

from collections import defaultdict
def characterReplacement(s: str, k: int) -> int:
    if len(s)==1:
        return 1 #If s is 1, K can be at most 1, so 1

    max_valid_window = 1
    L = 0
    curr_dict = defaultdict(int)
    for R in range(len(s)):
        #print("L", L, "R", R)
        #print(curr_dict)
        curr_dict[s[R]]+=1
        most_freq_element = max(curr_dict.values())
        window_len = R - L + 1
        allowed_replacements = window_len - most_freq_element
        #print(allowed_replacements, k)
        while allowed_replacements > k:
            # print("Shifting L")
            # print(curr_dict)
            # Keep shifting L, until we have valid window
            curr_dict[s[L]]-=1
            #print(curr_dict.values())
            most_freq_element = max(curr_dict.values())
            #print(most_freq_element)
            L+=1
            window_len = R - L + 1
            allowed_replacements = window_len - most_freq_element
            #print(allowed_replacements)
            
        # Now we have a valid window
        max_valid_window = max(max_valid_window, window_len)

    return max_valid_window

s="AAAB"
k=0
print(characterReplacement(s, k))

s = "XYYX"
k = 2
print(characterReplacement(s, k))

