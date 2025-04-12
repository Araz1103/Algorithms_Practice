"""
You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

You may choose to start at the index 0 or the index 1 floor.

Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

Example 1:

Input: cost = [1,2,3]

Output: 2
Explanation: We can start at index = 1 and pay the cost of cost[1] = 2 and take two steps to reach the top. The total cost is 2.

Example 2:

Input: cost = [1,2,1,2,1,1,1]

Output: 4
Explanation: Start at index = 0.

Pay the cost of cost[0] = 1 and take two steps to reach index = 2.
Pay the cost of cost[2] = 1 and take two steps to reach index = 4.
Pay the cost of cost[4] = 1 and take two steps to reach index = 6.
Pay the cost of cost[6] = 1 and take one step to reach the top.
The total cost is 4.
Constraints:

2 <= cost.length <= 100
0 <= cost[i] <= 100

"""

from typing import List

# My Code
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # cost to reach a particular step is minimum of cost from i-1 and i-2 steps

        def min_cost(stair_index, cache):
            # Base Cases Index 0 and 1
            if stair_index == 0:
                return cost[0]
        
            if stair_index == 1:
                return cost[1]

            # other wise check in cache
            if stair_index in cache:
                return cache[stair_index]

            # cost at this stair_index is min of cost to reach here
            # cost to reach here is min of cost from -1 or -2, and then cost of the stair here
            cache[stair_index] = min(cost[stair_index] + min_cost(stair_index-1, cache), cost[stair_index] + min_cost(stair_index-2, cache))
            return cache[stair_index]

        # can reach top either from last stair or second last stair
        return min(min_cost(len(cost)-1, {}), min_cost(len(cost)-2, {}))
    
# Documented Better
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Given an array 'cost' where cost[i] is the cost to step on the i-th stair,
        find the minimum cost to climb to the top of the staircase.
        
        Rules:
        - You can start from stair 0 or stair 1.
        - From a given stair, you can move either 1 step or 2 steps forward.
        - You must pay the cost at a stair when you step on it.
        - The top is just beyond the last stair, i.e., index len(cost).

        Goal:
        Find the minimum total cost to reach the top (just past the last index).

        Strategy:
        - Use top-down dynamic programming (memoized recursion).
        - Define min_cost(i) as the minimum cost to reach stair i.
        - For any stair i, to reach it, we must have come from:
            - stair i-1 and paid cost[i] to step here
            - OR stair i-2 and paid cost[i] to step here
        - So: min_cost(i) = cost[i] + min(min_cost(i-1), min_cost(i-2))
        - Base cases: min_cost(0) = cost[0], min_cost(1) = cost[1]
        - To reach the "top", we can arrive from either:
            - the last stair (n-1)
            - or the second last stair (n-2)
          So answer = min(min_cost(n-1), min_cost(n-2))

        Example:
        cost = [1, 2, 1, 2, 1, 1, 1]

        Step-by-step:
        - Start at index 0 → pay 1 → jump to 2
        - At index 2 → pay 1 → jump to 4
        - At index 4 → pay 1 → jump to 6
        - At index 6 → pay 1 → jump to top
        Total cost = 1 + 1 + 1 + 1 = 4

        Time Complexity: O(n)
        Space Complexity: O(n) for recursion stack + memoization
        """

        def min_cost(stair_index: int, cache: dict) -> int:
            """
            Recursive function to calculate minimum cost to reach stair_index.
            Uses memoization to avoid recomputation.
            """
            # Base case: if stair is 0 or 1, return the cost directly
            if stair_index == 0:
                return cost[0]
            if stair_index == 1:
                return cost[1]

            # If already computed, return cached result
            if stair_index in cache:
                return cache[stair_index]

            # Otherwise, compute cost to reach this stair
            # Option 1: Come from (i-1) and pay cost[i]
            # Option 2: Come from (i-2) and pay cost[i]
            # Pick the cheaper one
            cost_here = cost[stair_index]
            from_one_step_before = min_cost(stair_index - 1, cache)
            from_two_steps_before = min_cost(stair_index - 2, cache)
            cache[stair_index] = cost_here + min(from_one_step_before, from_two_steps_before)
            return cache[stair_index]

        n = len(cost)

        # You can reach the top (index n) from either the (n-1)th stair or (n-2)th stair
        return min(min_cost(n - 1, {}), min_cost(n - 2, {}))
