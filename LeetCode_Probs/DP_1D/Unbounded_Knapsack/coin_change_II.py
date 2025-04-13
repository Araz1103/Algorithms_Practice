"""
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) 
and an integer amount representing a target amount of money.

Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.

You may assume that you have an unlimited number of each coin and that each value in coins is unique.

Example 1:

Input: amount = 4, coins = [1,2,3]

Output: 4
Explanation:

1+1+1+1 = 4
1+1+2 = 4
2+2 = 4
1+3 = 4
Example 2:

Input: amount = 7, coins = [2,4]

Output: 0
Constraints:

1 <= coins.length <= 100
1 <= coins[i] <= 1000
0 <= amount <= 1000
"""
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Time Complexity:
        # Brute Force would be: 2^amount (as can keep taking upto amount for coin of value 1)
        # With memoization, reduces to: num_coins*amount
        # Time Complexity is: O(N*A)
        # Space is: O(N*A) for cache, and recursion stack depth: O(A) in worst case, for value 1 taking A times
        # So Space is also: O(N*A), as that is upper bound
        def get_ways(coin_index, current_amount, cache):

            if current_amount==0:
                # Reached target, found 1 way
                return 1

            if coin_index >= len(coins):
                return 0 # No more ways

            if cache[coin_index][current_amount]!=-1:
                return cache[coin_index][current_amount]

            # We can either include this coin or skip it

            # Skip
            skip_ways = get_ways(coin_index + 1, current_amount, cache)

            # Include it, if allowed
            take_ways = 0
            if coins[coin_index] <= current_amount:
                take_ways = get_ways(coin_index, current_amount - coins[coin_index], cache)

            total_ways = skip_ways + take_ways
            cache[coin_index][current_amount] = total_ways
            return total_ways

        # Initialise cache
        cache = [[-1]*(amount + 1) for _ in range(len(coins))]
        return get_ways(0, amount, cache)
        