"""
Climbing Stairs
You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:

Input: n = 2

Output: 2
Explanation:

1 + 1 = 2
2 = 2
Example 2:

Input: n = 3

Output: 3
Explanation:

1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3
Constraints:

1 <= n <= 30

n = 4
5 ways
1 + 1 + 2 = 4
1 + 1 + 1 + 1 = 4
1 + 2 + 1 = 4
2 + 2 = 4
2 + 1 + 1 = 4

n = 4 is (n = 3 +1) or (n = 2 + 2)
n = 3 is (n = 2 + 1) or (n = 1 + 2)
Basically for n steps
We need all the ways to come till n-1 steps + 1 step
All the ways to come till (n-2) steps + 2 steps

But #ways = (#ways - 1) + (#ways-2)

n = 5 is n=4 + n=3 -> 5 + 3 = 8
1 + 1 + 1 + 1 + 1 = 5
1 + 1 + 1 + 2 = 5
1 + 1 + 2 + 1 = 5
1 + 2 + 1 + 1 = 5
1 + 2 + 2 = 5
2 + 1 + 1 + 1 = 5
2 + 1 + 2 = 5
2 + 2 + 1 = 5
"""

def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2 # 2 ways to come
    else:
        return climbStairs(n-1) + climbStairs(n-2)
    
print(climbStairs(5))
print(climbStairs(6))
print(climbStairs(4))

# Returning the paths till n stairs
def climbStairs(n: int, path=[]) -> int:
    #print(f"In {n}")
    if n == 1:
        #print("1 Case")
        return [[1]] # 1 way to come
    elif n == 2:
        #print("2 Case")
        return [[1, 1], [2]] # 2 ways to come
    else:
        num_ways_n_1 = [(path_stairs + [1]) for path_stairs in climbStairs(n-1, path)]
        #print(f"{n} path: Got Num Ways n-1({n-1}): {num_ways_n_1}")
        num_ways_n_2 = [(path_stairs + [2]) for path_stairs in climbStairs(n-2, path)]
        #print(f"{n} path: Got Num Ways n-2({n-2}): {num_ways_n_1}")
        return num_ways_n_1 + num_ways_n_2
    
print(climbStairs(3))
print(climbStairs(4))
print(climbStairs(5))