"""
Solve the 0 / 1 Knapsack problem.

You are given a list of items, each with a weight and a profit, along with a backpack with a specified maximum capacity. 
Your goal is to calculate the maximum profit you can achieve without exceeding the backpack's capacity. 
You must select items such that the total weight of the items is less than or equal to the backpack's capacity. 
You can select at most one of each item.

Input:

profit - a list of n integers, where profit[i] represents the profit of the i-th item. (1 <= profit[i] <= 100)
weight - a list of n integers, where weight[i] represents the weight of the i-th item. (1 <= weight[i] <= 100)
capacity - an integer representing the maximum weight the backpack can hold. (1 <= capacity <= 100)
Here, n is the number of items, where 1 <= n <= 100. 
You can assume that weight and profit are both the same length and only contain positive integers.

Example 1:

Input:
profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]
capacity = 8

Output:
12
The maximum profit you can achieve is 12, by selecting the items at index 1, 2 and 3. 
The total profit is 4 + 7 + 1 = 12, and the total weight is 2 + 3 + 1 = 6, which is less than the backpack's capacity of 8.
"""

# Brute Force: 2^N
# @each item, choice to include it or not
def find_max_profit(profit, weight, capacity):

    def get_profit(item_index, current_capacity):
        
        # If reached last item, cannot take anything beyond this
        if item_index >= len(weight):
            return 0
        
        # 2 Choices, include item or skip it
        # Skip it
        # current capacity remains the same
        skip_profit = get_profit(item_index + 1, current_capacity)

        # Include it
        # Check if adding this exceeds knapsack capacity or not
        # Check if the weight of this item is <= current capacity
        include_profit = 0
        if weight[item_index] <= current_capacity:
            # Can include it
            include_profit = profit[item_index] + get_profit(item_index + 1, current_capacity - weight[item_index])

        max_profit = max(skip_profit, include_profit)
        return max_profit
    
    return get_profit(0, capacity)

        
# Adding memoisation
# For each item, if at the same capacity, can check from cache
# So cache is: number of items * capacity size
# So Soln space reduces to: O(N*M), N: #items M: Capacity

def find_max_profit(profit, weight, capacity):

    def get_profit(item_index, current_capacity, cache):

        if item_index >= len(weight):
            return 0
        
        # Check in cache
        if cache[item_index][current_capacity] > -1:
            return cache[item_index][current_capacity]
        
        # Include or Skip the items

        # Skip it
        skip_profit = get_profit(item_index + 1, current_capacity, cache)

        # Include it
        include_profit = 0
        # Check if we can, from current capacity
        if weight[item_index] <= current_capacity:
            include_profit = profit[item_index] + get_profit(item_index + 1, current_capacity - weight[item_index], cache)

        max_profit = max(skip_profit, include_profit)
        cache[item_index][current_capacity] = max_profit
        return max_profit
    
    # Initialise cache
    # Num Rows is Items, since first index gets to row
    # Num cols is capacity + 1, since second index gets to column
    # We take capacity + 1, as from 0 to capacity
    cache = [[-1]*(capacity + 1) for _ in range(len(weight))]
    return get_profit(0, capacity, cache)


profit=[4,4,7,1]
weight=[5,2,3,1]
capacity=8

print(find_max_profit(profit, weight, capacity))

from typing import Optional, List
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # We can include an item or not include
        # Try both paths, and return whichever is max from that
        # First code recursive soln
        # Then use memoization to optimize
        def choose_item(curr_item_idx, curr_capacity):
            # if item index out of bounds, we return 0
            if curr_item_idx >= len(profit):
                return 0

            # include it
            include_profit = 0
            if weight[curr_item_idx] <= curr_capacity:
                include_profit = profit[curr_item_idx] + choose_item(curr_item_idx+1, curr_capacity - weight[curr_item_idx])
                
            # skip it
            skip_profit = choose_item(curr_item_idx+1, curr_capacity)
                
            max_profit = max(include_profit, skip_profit)
            return max_profit
        
        return choose_item(0, capacity) 

class Solution:
    #Using Memoization
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # We can include an item or not include
        # Try both paths, and return whichever is max from that
        # First code recursive soln
        # Then use memoization to optimize
        # We maintain a cache for curr item idx with current capacity
        # So 2D Array, for all items for all capacities from 0 to capacity (C + 1)
        cache = [[-1]*(capacity+1) for _ in range(len(profit))]
        # Size is: #items * capacity + 1 (as 0 included, then 1 to C)
        def choose_item(curr_item_idx, curr_capacity, cache):
            # if item index out of bounds, we return 0
            if curr_item_idx >= len(profit):
                return 0

            if cache[curr_item_idx][capacity] != -1:
                return cache[curr_item_idx][curr_capacity]

            # include it
            include_profit = 0
            if weight[curr_item_idx] <= curr_capacity:
                include_profit = profit[curr_item_idx] + choose_item(curr_item_idx+1, curr_capacity - weight[curr_item_idx], cache)
                
            # skip it
            skip_profit = choose_item(curr_item_idx+1, curr_capacity, cache)
                
            max_profit = max(include_profit, skip_profit)
            cache[curr_item_idx][curr_capacity] = max_profit
            return cache[curr_item_idx][curr_capacity]
        
        return choose_item(0, capacity, cache)   