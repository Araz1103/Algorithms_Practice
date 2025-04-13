class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Returns the number of distinct subsequences of `s` which equals `t`.

        Uses top-down recursion with memoization to avoid recomputation.

        Time Complexity: O(len(s) * len(t))
        Space Complexity: O(len(s) * len(t)) for the memoization cache

        Brute Force would have been:
        Len of Tree is worst case len(s), as iterating through s
        Worst case Upper Bound for brute force: 2^(len(s))

        With memoisation we reduce to: O(len(s)*len(t))

        --------------------
        🔁 Overlapping Subproblems:

        Example:
            s = "babgbag"
            t = "bag"

        Recursion Tree (simplified):

                     (0,0)
                   /      \
              (1,1)       (1,0)
              /   \         \
          (2,2) (2,1)       (2,0)
             \     \        /   \
            (3,2) (3,1)   (3,1) (3,0) ← REPEATED!

        Explanation:
            - (0,0): 'b' == 'b' → can either take it (1,1) or skip (1,0)
            - (1,1): 'a' == 'a' → take (2,2) or skip (2,1)
            - (2,2): 'b' ≠ 'g' → skip → (3,2)
            - (2,1): 'b' ≠ 'a' → skip → (3,1)
            - (2,0): 'b' == 'b' → take (3,1), skip (3,0)

            → (3,1) is repeated in two paths.

        Memoization prevents redundant work by caching results of (i1, i2)
        so they are computed only once.

        --------------------
        """

        def check_subsequence(i1, i2, cache):

            # If i1 is out of bounds, return 0
            # As not found till yet
            if i1 >= len(s):
                # If exceeded s1
                # Check if i2 was incremented and @end
                # If yes, then a subsequence was found
                if i2 == len(t):
                    return 1
                else:
                    return 0

            # If reached end of t, we know found 1 subsequence
            if i2==len(t):
                return 1

            # Check cache
            if cache[i1][i2]!=-1:
                return cache[i1][i2]

            # If i1 and i2 are same characters, we can increment both and increment 1
            # If they are not the same, only increment i1 to check

            # Same
            if s[i1]==t[i2]:
                # Increment both
                # Only increment i1
                num_subseq = check_subsequence(i1+1, i2+1, cache) + check_subsequence(i1+1, i2, cache)
            else:
                # Only increment i1
                num_subseq = check_subsequence(i1+1, i2, cache)

            cache[i1][i2] = num_subseq
            return num_subseq

        # Initialise cache
        cache = [[-1]*len(t) for _ in range(len(s))]
        return check_subsequence(0, 0, cache)
