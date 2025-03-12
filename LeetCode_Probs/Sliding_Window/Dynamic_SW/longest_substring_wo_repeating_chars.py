"""
Given a string s, find the length of the longest substring 
without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.
"""

# Intuition, we have a dynamic window
# We keep exploring with R, adding to our current list of elements
# If it is w/o duplicates (check len of list == len of set of list)
# We update max substring len
# Otherwise we shrink window by incrementing L until it is w/o duplicates
# So worst case, L comes upto R
# Stop when R goes out of bounds
# This way O(N)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        else:
            L = 0
            current_list = []
            max_substring = 0
            for R in range(len(s)):
                current_list.append(s[R])
                while len(current_list)!=len(set(current_list)):
                    # Until our current list has all unique elements
                    # Keep incrementing L
                    current_list.pop(0) #Remove first element
                    L+=1
                max_substring = max(max_substring, len(current_list))
            return max_substring
        
# True: O(N) Time complexity and O(1) space since 26 letters for lowercase
def substring(chars):
    l = 0
    max_l, max_r = 0,0
    char_count = {} #stores count of chars
    for r in range(len(chars)):
        if chars[r] not in char_count: #Not seen this character yet
            char_count[chars[r]] = 1
        else:
            char_count[chars[r]]+=1
            # Check if count is >1
            if char_count[chars[r]] > 1:
                # Means duplicate, we keep shrinking window, until this goes down to 0
                while char_count[chars[r]] > 1:
                    char_count[chars[l]]-=1
                    l+=1
                # Now is a valid window
        # Update Max Substring with max_l and max_r
        if r-l+1 >= (max_r-max_l+1):
            max_l = l
            max_r = r
    return chars[max_l:max_r+1]

print(substring("abcabcbbefghhibtacs"))
                

        