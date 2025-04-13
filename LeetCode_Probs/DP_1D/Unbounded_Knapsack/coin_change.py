"""
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) 
and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. 
If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.

Example 1:

Input: coins = [1,5,10], amount = 12

Output: 3
Explanation: 12 = 10 + 1 + 1. Note that we do not have to use every kind coin available.

Example 2:

Input: coins = [2], amount = 3

Output: -1
Explanation: The amount of 3 cannot be made up with coins of 2.

Example 3:

Input: coins = [1], amount = 0

Output: 0
Explanation: Choosing 0 coins is a valid way to make up 0.

Constraints:

1 <= coins.length <= 10
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10000

"""

# Can take each coin again, until we reach target sum
# Keep a count of num coins till then
# Handle edge cases of amount 0

def get_min_coins(coins, target_amount):

    if target_amount==0:
        return 0
    
    INF = float('inf')

    def check_num_coins(coin_index, current_amount, cache):

        # Check if current amount at 0, therefore reached target
        if current_amount==0:
            #print("Found Target!")
            return 0 #Reached Target, don't need to take anymore coins
        
        # If all coins taken
        if coin_index >= len(coins):
            return INF #Did not reach Target, using INF
            
        # Check cache
        if cache[coin_index][current_amount]!=-1:
            return cache[coin_index][current_amount]
        
        # Can include the current coin or skip it

        # Skipping it
        num_coins_skip = check_num_coins(coin_index + 1, current_amount, cache)

        # Including it, if we can
        num_coins_include = INF
        if coins[coin_index] <= current_amount:
            # We use this coin, so 1 for that, and then check
            # Also can take same coin again and again, so do not increment coin index
            num_coins_include = 1 + check_num_coins(coin_index, current_amount - coins[coin_index], cache)

        # Set to minimum coins from each path
        min_coins = min(num_coins_skip, num_coins_include)
        cache[coin_index][current_amount] = min_coins
        return min_coins
    
    # Initialise cache
    cache = [[-1]*(target_amount + 1) for _ in range(len(coins))]
    min_coins = check_num_coins(0, target_amount, cache)
    #print(cache)
    return -1 if min_coins==INF else min_coins

coins=[1,2,5,6]
amount=11

print(get_min_coins(coins, amount))