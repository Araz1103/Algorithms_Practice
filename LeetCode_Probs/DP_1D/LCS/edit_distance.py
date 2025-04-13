"""
You are given two strings word1 and word2, each consisting of lowercase English letters.

You are allowed to perform three operations on word1 an unlimited number of times:

Insert a character at any position
Delete a character at any position
Replace a character at any position
Return the minimum number of operations to make word1 equal word2.

Example 1:

Input: word1 = "monkeys", word2 = "money"

Output: 2
Explanation:
monkeys -> monkey (remove s)
monkey -> monkey (remove k)

Example 2:

Input: word1 = "neatcdee", word2 = "neetcode"

Output: 3
Explanation:
neatcdee -> neetcdee (replace a with e)
neetcdee -> neetcde (remove last e)
neetcde -> neetcode (insert o)

Constraints:

0 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Problem: Minimum Edit Distance (Levenshtein Distance)

        Given two strings `word1` and `word2`, return the minimum number of operations 
        required to convert `word1` to `word2`. Operations allowed: 
        - Insert a character
        - Delete a character
        - Replace a character

        Approach:
        - Recursive top-down DP with memoization.
        - For each (i1, i2) position in word1 and word2:
            - If characters match, no operation needed — move both pointers forward.
            - Else, try all three operations and choose the one with the minimum cost.
              • Insert: keep i1, increment i2
              • Delete: increment i1, keep i2
              • Replace: increment both i1 and i2
        - Cache results to avoid recomputation.

        Time Complexity: O(M * N) 
            - M = len(word1), N = len(word2)
            - Each (i1, i2) pair is visited once and stored in the cache.
        
        Space Complexity: 
            - O(M * N) for memoization cache
            - O(M + N) for the recursion call stack in worst case
        
        Brute Force (Without Memoization):
            - 3 recursive choices at each step, up to depth M+N
            - Time: O(3^(M + N)) → Exponential
        
        Memoization Prevents:
            - Recomputing subproblems like (i1=2, i2=3), (i1=2, i2=4) multiple times
            - Example: If several paths reach (2, 3), cached value is reused.

        Example:
            word1 = "horse", word2 = "ros"
            Output = 3
            Explanation:
              - Replace 'h' with 'r'
              - Remove 'o'
              - Remove 'e'
        """
        # Time Complexity:
        # O(M*N), M is len of word1, N is len of word2
        # Space is: O(M*N) from cache and O(M+N) from recursion stack depth
        # Upper Bound is: O(M*N)

        # Brute Force would be a decision tree, with 3 decisions @each point
        # Since max depth is M+N, BF would be: 3^(M+N)
        def check_operations(i1, i2, cache):

            # Base cases
            # I: both i1 and i2 are out of bounds, therefore no operations needed, matched w1 to w2
            if i1==len(word1) and i2==len(word2):
                return 0 #No ops needed anymore

            # II: i1 is out of bounds (empty string) and i2 is not, ops is len of w2 left
            if i1==len(word1):
                return len(word2) - i2

            # III: i2 is out of bounds (empty string) and i1 is not, ops is len of w1 left
            if i2==len(word2):
                return len(word1) - i1

            # Check cache
            if cache[i1][i2]!=-1:
                return cache[i1][i2]

            # Now check if the chars at i1 and i2 are same
            if word1[i1]==word2[i2]:
                # Since matching, no ops needed, can increment both and check ahead
                num_ops = check_operations(i1 + 1, i2 + 1, cache)
            else:
                # Now check ahead for all 3 operations

                # Insertion
                # Insert @w1, matches so increment i2 but i1 remains here, as inserted before i1
                insert_ops = 1 + check_operations(i1, i2+1, cache)
                # Deletion
                # Delete @w1, move ahead hoping it can match, so i1 incremented and i2 remains here
                delete_ops = 1 + check_operations(i1+1, i2, cache)
                # Replace
                # Replace @w1, matches with both, incrementing both
                replace_ops = 1 + check_operations(i1 + 1, i2 + 1, cache)
                # We want minimum from all 3
                num_ops = min(insert_ops, delete_ops, replace_ops)

            cache[i1][i2] = num_ops
            return num_ops

        # Initialise cache
        cache = [[-1]*len(word2) for _ in range(len(word1))]
        return check_operations(0, 0, cache)
