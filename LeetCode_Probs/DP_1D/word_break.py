"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.

Example 1:

Input: s = "neetcode", wordDict = ["neet","code"]

Output: true
Explanation: Return true because "neetcode" can be split into "neet" and "code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen","ape"]

Output: true
Explanation: Return true because "applepenapple" can be split into "apple", "pen" and "apple". Notice that we can reuse words and also not use all the words.

Example 3:

Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]

Output: false
Constraints:

1 <= s.length <= 200
1 <= wordDict.length <= 100
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        def check_word_exists(s, cache):
            if s in cache:
                return cache[s]
            # go letter by letter
            # Keep checking if a word is formed in wordDict
            # When we find it
            # We break off to check with string remaining removing this word
            # And continue checking with current letters
            curr_word = s[0]
            found_word = False
            for i in range(1, len(s)):
                if curr_word in wordDict:
                    # Now try to see if remaining string is valid or not
                    if check_word_exists(s[i:], cache):
                        found_word = True
                        break #Can exit, if we know there exists a word post the pre-fix
                curr_word+=s[i]

            if curr_word in word_set:
                found_word = True

            cache[s] = found_word
            return cache[s]

        return check_word_exists(s, {})
        
# Benefit of Caching
"""
"aaaa"
 ├─ "a" + check("aaa")
 │     ├─ "a" + check("aa")
 │     │     ├─ "a" + check("a")
 │     │     └─ "aa" + check("")
 │     └─ "aa" + check("a")
 └─ "aa" + check("aa")   <-- Without cache, check("aa") is computed again.
"""
# Documented Version for more clarity!

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determine if the input string 's' can be segmented into a sequence of one or more words from 'wordDict'.

        Args:
            s (str): The input string to segment.
            wordDict (List[str]): A list of valid dictionary words.

        Returns:
            bool: True if 's' can be segmented into a space-separated sequence of one or more dictionary words, otherwise False.

        Examples:
            >>> sol = Solution()
            >>> sol.wordBreak("leetcode", ["leet", "code"])
            True
            >>> sol.wordBreak("applepenapple", ["apple", "pen"])
            True
            >>> sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
            False

        Time Complexity Analysis:
            Let n be the length of the input string s.
            
            - Without memoization, the recursive solution may explore an exponential number of segmentations (roughly O(2^n)).
            - With memoization, each unique substring (up to n of them) is computed only once.
            - In each recursive call for a substring of length L, the algorithm loops over up to L positions.
            - In an idealized scenario (assuming constant-time string slicing/concatenation), the time complexity becomes O(n^2).
            - However, in Python, slicing and concatenating strings take O(n) time, so in the worst-case the complexity can approach O(n^3).

        How to Analyze:
            1. Identify unique subproblems: here, each substring s[i:] is a subproblem.
            2. Count subproblems: there are at most O(n) of these.
            3. Determine work per subproblem: a loop over at most n characters gives O(n) work.
            4. Multiply these together and consider any additional overhead (like slicing) to arrive at the overall complexity.
        """
        # Convert wordDict to a set for faster O(1) lookups
        word_set = set(wordDict)

        def check_word_exists(s: str, cache: dict) -> bool:
            """
            Recursively checks whether the string s can be segmented into valid words from word_set,
            using a memoization cache to avoid redundant work.

            Args:
                s (str): The substring to be checked.
                cache (dict): A memoization dictionary mapping substrings to a boolean result.

            Returns:
                bool: True if s can be segmented into valid words, False otherwise.
            """
            # If the result for s has already been computed, return it
            if s in cache:
                return cache[s]
            
            found_word = False
            # Start building a candidate word from the first character
            curr_word = s[0]
            # Try every possible prefix of s (except checking the full string here, which we do later)
            for i in range(1, len(s)):
                # If the current prefix is a valid word, recursively check the remainder of the string.
                if curr_word in word_set:
                    if check_word_exists(s[i:], cache):
                        found_word = True
                        break  # Early exit if a valid segmentation is found
                # Append the next character to curr_word to form a longer candidate word
                curr_word += s[i]

            # Finally, check if the entire string s is a valid word.
            if curr_word in word_set:
                found_word = True

            # Cache the computed result for substring s
            cache[s] = found_word
            return found_word

        return check_word_exists(s, {})
