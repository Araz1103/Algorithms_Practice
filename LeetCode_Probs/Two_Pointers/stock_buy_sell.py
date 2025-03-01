"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # @any given index
        # Max profit is: MaxR - CurrIndex
        # We can solve in O(N)
        # Do 1 pass to store MaxR @each Index
        # Then do 1 pass to calculate profit @each indx
        # Then keep checking if profit is gt max profit
        # Space complexity is O(N)

        # Can we solve with no extra space Hmmm
        # Well when we are calculating MaxR
        # So Starting @Reverse
        # we can calculate the profit then and there
        # So don't need to store the maxR anywhere!
        max_profit = 0
        max_r = 0
        for idx in range(len(prices)-1, -1, -1):
            current_profit = max_r - prices[idx]
            max_profit = max(max_profit, current_profit)
            if prices[idx] > max_r:
                max_r = prices[idx]
        return max_profit
        