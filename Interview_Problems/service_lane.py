"""

You will be given an array of widths at points along the road (indices), then a list of the indices of entry and exit points. Considering each entry and exit point pair, calculate the maximum size vehicle that can travel that segment of the service lane safely.
Example
n = 4
width = [2, 3, 2, 1]
cases = [[1, 2], [2, 4]]


If the entry index,i=1 and the exit,j=2 , there are two segment widths of 2 and 3 respectively. The widest vehicle that can fit through both is 2. 
If i=2 and j=4, the widths are [3, 2, 1] which limits vehicle width to 1.

Complete the serviceLane function in the editor below.
serviceLane has the following parameter(s):
int n: the size of the width array
int cases[t][2]: each element contains the starting and ending indices for a segment to consider, inclusive
Returns
int[t]: the maximum width vehicle that can pass through each segment of the service lane described
"""
"""
# So basically for each slice, we need to find the minimum
# Naive way, take the slice, and find the minimum
# Complexity: #Cases*O(width of the slice)
# O(t)*O(widths)
# Best Case: 1*O(2)
# Worst Case: 1000*1000

# But is there any way we can pre-compute, so we can find the minimum faster?
# Hmmmmmm
# Using Sparse Array
# Pre-Computing Time is N*LogN
# But Querying time is O(1)
# Intuition: We store min of intervals of 1, 2, 4, 8.. (Powers of 2)
# Any range can be broken down in @max 2 intervals of above
# Ex: 1-6: 1-4 and 5-6
# Ex: 1-3: 1-2 and 2-3
# Ex: 3-10: Is an interval of size 8
# Ex: 3-11: 3-10 and 10-11

# To build the array:
# Ex: [1, 2, 0, 4, 5, 2, 1, 3]
# First of 1 is elements itself: [1, 2, 0, 4, 5, 2, 1, 3]
# To make 2, we use min of previous: 
# min(1,2) - min(2, 0) - min(0, 4)... min (1-3)

# [1, 0, 0, 4, 2, 1, 1] 
# For 4, we use the previous arrays
# min(1, 2, 0, 4) = min(min(1, 2) & min(0, 4)) and we already have values of the 2 mins from previous array


st[i][j] = min( st[i][j−1], st[ i+ (2^(j−1)) ][j−1] )

This formula is saying:

- We're computing the minimum for a range of size 2^j starting at index i
- Instead of looking at all elements in this range, we break it into two smaller precomputed parts.
- Those two parts are of size 2^(j−1) (half the size of the current range).
- We take the minimum of those two parts.
- taking j-1 index of 2nd list as that gives of the previous pre-computed minimum

The key observation is that any range of size 2^j can be decomposed into two overlapping smaller ranges of size 2^(j-1)

Base Case: j=0
st[i][0] = arr[i]

j=1, Ranges of Size (2^1 = 2)

st[i][1] = min(st[i][0], st[i + 2^0][0])
st[i][1] = min(st[i][0], st[i + 1][0])

j=2, Ranges of Size (2^2 = 4)
st[i][2] = min(st[i][1], st[i + 2^1][1])
st[i][2] = min(st[i][1], st[i+2][1])

[1, 2, 0, 4, 5, 2, 1, 3]

st[0][2] = min(st[0][1], st[2][1])

st[0][1] = min(1, 2)
st[2][1] = min(0, 4)
So makes sense that min(1, 2, 0, 4) = min(min(1,2), min(0,4))

Therefore taking min till 1 and from i to i + 2^j-1 as these are 2 halfs

"""

def serviceLane(widths, cases):
    # Write your code here
    min_widths = []
    for case in cases:
        n_slice = widths[case[0]:case[1]+1]
        min_widths.append(min(n_slice))

    return min_widths

print(serviceLane([2, 3, 1, 2, 3, 2, 3, 3], [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]))

import math

def build_sparse_table(arr):
    """ Builds a Sparse Table for Range Minimum Queries """
    n = len(arr)
    k = math.floor(math.log2(n)) + 1  # Maximum power of 2 that fits in `n`
    
    # Create Sparse Table `st` with dimensions (n x k)
    st = [[0] * k for _ in range(n)]

    # Step 1: Initialize the first column (j = 0) with original array values
    for i in range(n):
        st[i][0] = arr[i]

    # Step 2: Build the table using the recurrence relation
    j = 1
    while (1 << j) <= n:  # While 2^j <= n
        i = 0
        while (i + (1 << j) - 1) < n:  # Ensure we don't go out of bounds
            st[i][j] = min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
            i += 1
        j += 1

    return st

# Explaining << Operator!
print(1 << 3)  # 1 * 2^3 = 8
print(2 << 2)  # 2 * 2^2 = 8

# Same as
j = 3
(2 ** j)   # Using exponentiation
j = 2
(2 ** j)   # Using exponentiation

import math


# If we change min to max, can compute for Max in a Range
# Also works with GCD
# Because gcd(gcd(a, b), c) = gcd(a, gcd(b, c)), it works well.

def build_sparse_table(arr):
    """
    Builds a Sparse Table for Range Minimum Queries (RMQ).
    
    This table allows us to efficiently query the minimum value in any subarray using O(1) time
    after an O(N log N) preprocessing step.
    
    Explanation:
    - We store the minimum values of subarrays of length 2^j in `st[i][j]`
    - We use a bottom-up approach to build the table

    Parameters:
    arr (list): The input array for which the sparse table is built.

    Returns:
    list: A 2D list representing the Sparse Table.
    """
    n = len(arr)

    # Step 1: Compute the maximum power of 2 that fits in `n`
    k = math.floor(math.log2(n)) + 1  # k is the number of levels (columns) in the table

    # Step 2: Initialize Sparse Table `st` with dimensions (n x k)
    st = [[0] * k for _ in range(n)]

    # Step 3: Fill the first column (j = 0) with the original array values
    for i in range(n):
        st[i][0] = arr[i]

    # Step 4: Build the table iteratively
    j = 1  # Represents subarray sizes of 2^j
    while (2 ** j) <= n:  # Ensures we don't go beyond the array size
        i = 0  # Start from the beginning of the array
        
        while (i + (2 ** j) - 1) < n:  # Ensures subarrays stay within bounds
            """
            The core recurrence relation:
            st[i][j] = min(
                st[i][j - 1],                    # Minimum in the first half (2^(j-1) size)
                st[i + (2 ** (j - 1))][j - 1]    # Minimum in the second half (2^(j-1) size)
            )
            """
            st[i][j] = min(st[i][j - 1], st[i + (2 ** (j - 1))][j - 1])

            # Move to the next starting position
            i += 1
        
        # Move to the next power of 2
        j += 1

    return st


