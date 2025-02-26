"""
Given two strings s and p, 
return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
"""
from collections import Counter, defaultdict

def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    # P has a string, and we want to find all anagrams of P in S
    # Return the start indices
    # Check the windows of len of P in S
    # In window, set of window has to equal to set of P

    
    window_len = len(p)
    s_len = len(s)
    p_dict = dict(Counter(p))
    #print(f"Window Len: {window_len}")
    #print(f"Check String Len: {s_len}")
    # Edge Cases, if len(p) > len(s), no possible indice
    # If both equal, check if their sets are equal
    if window_len > s_len:
        #print("Window Len > S Len!")
        return []
    elif window_len == s_len:
        if p_dict == dict(Counter(s)):
            return [0]
        else:
            return []  
    else:
        #print("Finding Anagrams!")
        anagrams = []
        L = 0
        curr_dict = defaultdict(int)
        for letter in s[:window_len-1]:
            curr_dict[letter]+=1
        
        # Now using a sliding fixed window check
        for R in range(window_len-1, s_len):
            #print(curr_dict)
            curr_dict[s[R]]+=1
            if curr_dict == p_dict:
                #anagrams.append((L, s[L:R+1]))
                anagrams.append(L)
            # Move R and L
            # remove L from Set and will add new R @next iteration
            curr_dict[s[L]]-=1
            if curr_dict[s[L]]==0:
                curr_dict.pop(s[L])
            L+=1
        return anagrams

a = "abdesgsaba"
b = "ba"
print(findAnagrams(a,b))

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))

s = "abab"
p = "ab"
print(findAnagrams(s,p))

s = "a"
p = "ab"
print(findAnagrams(s,p))

s = "ababababab"
p = "aab"
print(findAnagrams(s,p))