"""
Given two strings s1 and s2, return true 
if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

# Technically checking if an anagram of s1 is in s2
# Checking anagrams is with dictionary
# Make a dict and check if they are equal
# With a sliding window the size of s1, add and remove elements from the dict
from collections import Counter

def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if len(s1) > len(s2):
        print("S1 GT S2!")
        return False #Not possible for s2 to contain s1
    
    s1_dict = Counter(s1)

    if len(s1)==len(s2):
        print("Len is Equal!")
        # Since only 1 sub-string, directly check
        return s1_dict==Counter(s2)
    
    window_size = len(s1)
    print("WS", window_size)
    curr_dict = Counter(s2[:window_size-1])
    L=0
    for R in range(window_size-1, len(s2)):
        curr_dict[s2[R]]+=1
        print(curr_dict)
        if curr_dict==s1_dict:
            return True
        # Otherwise we now increment L
        # Before that we do the following:
        #   Remove current L (decrement count) and the new R will be added
        #   If after decrementing current L, it's count is 0, pop that
        curr_dict[s2[L]]-=1
        if curr_dict[s2[L]]==0:
            curr_dict.pop(s2[L])
        L+=1
    return False #If until now not found, return False

# a = "abdesgsaba"
# b = "ba"
# print(checkInclusion(b, a))

# s = "cbaebabacd"
# p = "abc"
# print(checkInclusion(s, p))

# s = "abab"
# p = "ab"
# print(checkInclusion(p,s))

# s = "a"
# p = "ab"
# print(checkInclusion(p,s))

# s = "ababababab"
# p = "aab"
# print(checkInclusion(p,s))

a = "ab"
b = "eidbaooo"
print(checkInclusion(a, b))

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # We have a sliding window of fixed size
        # We keep checking in that if that is same as s1 or not
        # Use a hashmap, so keep adding and subtracting from that

        s1_hashmap = Counter(s1)

        len_s1 = len(s1) #Size of Fixed Window

        if len(s2) < len_s1:
            return False

        current_hashmap = Counter(s2[:len_s1])
        if current_hashmap==s1_hashmap:
            return True
        
        # Now check in this fixed window
        # Keep sliding it, and remove from behind and add new char
        p0 = 0

        for p1 in range(len_s1, len(s2)):
            # Remove from Hashmap and add to it
            current_hashmap[s2[p0]]-=1
            if current_hashmap[s2[p0]]==0:
                del current_hashmap[s2[p0]]

            current_hashmap[s2[p1]]+=1

            if current_hashmap==s1_hashmap:
                return True
            p0+=1

        return False

        