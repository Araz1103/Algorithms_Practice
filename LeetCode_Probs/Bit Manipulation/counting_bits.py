"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""

# O(N*Log(N))
# As Every shift to right is /2
# Until we reach 0 is log(n) for n
# So technically counting 1 bits with function is log(n)
def num1bits(n):
    count = 0
    while n > 0:
        if n&1==1:
            count+=1
        n = n>>1
    return count

def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    num_1s = []
    for i in range(n):
        num_1s.append(num1bits(i))
    return num_1s


def countBitsDP(n):
    """
    :type n: int
    :rtype: List[int]
    """
    
    # Offset is 1 rn
    # dp[i] = 1 + dp[i - offset]
    # offset decided by the current most significant bit
    # MSB starts @1
    # Then @2 its 2
    # Then 4
    # Then @8
    #
    # 0: 00'00'
    # 1: 00'01' : numbits: 1 + dp[n-1]
    # 2: 00'10' : numbits: 1 + dp[n-2]
    # 3: 00'11' : numbits: 1 + dp[n-2]
    # 4: 01'00' : numbits: 1 + dp[n-4]
    # 5: 01'01' : numbits: 1 + dp[n-4]
    # 6: 01'10' : numbits: 1 + dp[n-4]
    # 7: 01'11' : numbits: 1 + dp[n-4]
    # 8: 1'000' : numbits: 1 + dp[n-8]

    curr_offset = 1
    dp = [0]*(n+1)
    # Since we know dp[0] = 0 bits
    # Starting from 1
    for i in range(1, n+1):
        if i==curr_offset*2:
            curr_offset*=2
        dp[i] = 1 + dp[i-curr_offset]
    return dp

# Time complexity is O(N), thanks to DP!

print(countBitsDP(9))