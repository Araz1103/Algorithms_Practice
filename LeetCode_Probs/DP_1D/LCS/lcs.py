class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Returns the length of the longest common subsequence between text1 and text2.

        Uses top-down DP with memoization to avoid recomputation.

        Time Complexity: O(M * N), where M = len(text1), N = len(text2)
            - Each (i1, i2) state is computed at most once.

        Space Complexity:
            - Cache: O(M * N)
            - Recursion stack depth: O(M + N)
                This is because in any single recursive path, we only increase i1 or i2
                one step at a time until we hit the base case. The longest path is when
                we go from i1=0 → M and i2=0 → N, totaling at most M + N depth.
        
                Example:
                text1 = "abcde"    # M = 5
                text2 = "fghij"    # N = 5

                # Worst Case Path (no matching chars):
                (0,0) → (1,0) → (2,0) → (3,0) → (4,0) → (5,0) → (5,1) → (5,2) → (5,3) → (5,4) → (5,5)
                Total of M + N = 10 calls on stack at once.

        """
        def check_lcs(i1, i2, cache):
            # i1 is pointer for text1
            # i2 is pointer for text2

            # if character at i1 and i2 is equal
            # We know LCS is 1 + LCS(text1[i1+1:], text2[i2+1:])
            # if they are not equal
            # then we check both paths
            # if we increment i1 and i2 remains same
            # if we increment i2 and i1 remains the same
            # we don't need to increment both, as future recursion handles that

            # Handle Base Case i1 or i2 out of bounds
            if i1 >= len(text1) or i2 >= len(text2):
                return 0

            if cache[i1][i2]!=-1:
                return cache[i1][i2]

            if text1[i1]==text2[i2]:
                max_len = 1 + check_lcs(i1+1, i2+1, cache)

            else:
                # increment i1 and i2 remains same
                # increment i2 and i1 remains the same
                max_len = max(check_lcs(i1 + 1, i2, cache), check_lcs(i1, i2+1, cache))
            
            cache[i1][i2] = max_len
            return cache[i1][i2]

        # Initialise cache
        cache = [[-1]*len(text2) for _ in range(len(text1))]
        return check_lcs(0, 0, cache)
