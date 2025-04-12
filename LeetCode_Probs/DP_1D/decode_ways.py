"""
Decode Ways
Solved 
A string consisting of uppercase english characters can be encoded to a number using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, "1012" can be mapped into:

"JAB" with the grouping (10 1 2)
"JL" with the grouping (10 12)
The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.

Example 1:

Input: s = "12"

Output: 2

Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "01"

Output: 0
Explanation: "01" cannot be decoded because "01" cannot be mapped into a letter.

Constraints:

1 <= s.length <= 100
s consists of digits
"""

class Solution:
    def numDecodings(self, s: str) -> int:

        def num_ways(curr_index, cache):

            # If curr index is valid + rest__
            # If (curr_index curr_index+1) is valid + rest__
            # Implement caching
            if curr_index >= len(s):
                return 1 #Reached @end, so possible

            if curr_index in cache:
                return cache[curr_index]

            if int(s[curr_index])==0:
                # Cannot make anything from here
                cache[curr_index] = 0
                return 0

            if int(s[curr_index]) in range(1, 27):
                # Valid ways
                num_ways_1 = num_ways(curr_index + 1, cache)
            else:
                num_ways_1 = 0

            # Check if curr_index + 1 in bounds
            if curr_index + 1 < len(s):
                if int(s[curr_index] + s[curr_index + 1]) in range(10, 27):
                    num_ways_2 = num_ways(curr_index + 2, cache)
                else:
                    num_ways_2 = 0
            else:
                num_ways_2 = 0

            cache[curr_index] = num_ways_1 + num_ways_2
            return cache[curr_index]

        return num_ways(0, {})

        