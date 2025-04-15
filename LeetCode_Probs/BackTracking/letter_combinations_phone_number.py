from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string containing digits from 2 to 9 inclusive, return all possible letter 
        combinations that the number could represent using the mapping on a telephone keypad.

        The mapping is as follows:
            2 -> "abc"
            3 -> "def"
            4 -> "ghi"
            5 -> "jkl"
            6 -> "mno"
            7 -> "pqrs"
            8 -> "tuv"
            9 -> "wxyz"

        This is solved using a recursive backtracking approach.

        Time Complexity:
            - Let N be the number of digits in the input.
            - At each position, we have at most 4 choices (for digits 7 and 9).
            - So the total number of recursive paths is O(4^N).
            - For each of these combinations, we copy or join a string of length N → O(N).
            - Total time complexity: O(N * 4^N)

        Space Complexity:
            - Recursion depth is at most N → O(N) stack space.
            - We use an auxiliary list `curr_set` of size N → O(N).
            - Final output list holds O(4^N) combinations, each of size N → O(N * 4^N)
            - So overall space complexity: O(N * 4^N)

        Notes:
            - This is a classic example of a recursive decision tree, where each digit corresponds
              to multiple branching paths (choices).
            - Backtracking is used to revert a choice (via `pop()`) and explore the next.
            - No pruning is needed here since all branches are valid.
            - The use of `.copy()` or `"".join()` ensures we store snapshots instead of mutable references.

        Example:
            Input: "23"
            Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

        """
        char_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if not digits:
            return []

        combinations = []

        def get_combinations(curr_index, curr_set):

            # Base Case, digits done
            if curr_index == len(digits):
                combinations.append("".join(curr_set.copy()))
                return

            # For current digit, use the character map and we know possible digits
            # Add them one by one and back track
            curr_digit = digits[curr_index]
            chars_for_digit = char_map[curr_digit]

            for char in chars_for_digit:
                curr_set.append(char)
                get_combinations(curr_index+1, curr_set)
                curr_set.pop()

            return

        get_combinations(0, [])
        return combinations