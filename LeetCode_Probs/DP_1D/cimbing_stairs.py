def climbStairs(self, n: int) -> int:
    # We can reach each stairs either from the stairs before it
    # or from the stairs one before it, since 1 or 2 steps allowed
    # base case: if at stair 2, 2 ways to reach it
    # base case: if at stair 1, 1 way to reach it
    # Use Memoization to make more efficient
    def get_ways(n, cache):
        if n<=2:
            return n
        
        if n in cache:
            return cache[n]

        cache[n] = get_ways(n-2, cache) + get_ways(n-1, cache)
        return cache[n]

    return get_ways(n, {})

# Use Bottoms Up Approach
# Build from base cases

def climbStairs(self, n: int) -> int:
    # We can reach each stairs either from the stairs before it
    # or from the stairs one before it, since 1 or 2 steps allowed
    # base case: if at stair 2, 2 ways to reach it
    # base case: if at stair 1, 1 way to reach it
    if n <=2:
        return n

    dp = [1, 2] # for case 1 and 2
    i = 3 #Starting from 3, building up to n
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[1] + dp[0]
        dp[0] = tmp
        i+=1
    return dp[1] #will have num ways for n