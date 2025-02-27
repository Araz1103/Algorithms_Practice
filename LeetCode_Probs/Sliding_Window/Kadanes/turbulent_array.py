"""
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
 

Example 1:
Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
                9 > 4 > 2 < 10 > 7 < 8 = 8 > 1 < 9
                9 > 4 > 2 > 1 < 3 > 2 = 2 

Example 2:
Input: arr = [4,8,12,16]
Output: 2

Example 3:
Input: arr = [100]
Output: 1
 

Constraints:

1 <= arr.length <= 4 * 10^4
0 <= arr[i] <= 109
"""

def get_sign(a, b):
    if a > b:
        return '>'
    elif a==b:
        return '='
    else:
        return '<'
    
def check_opposite_signs(curr_sign, last_sign):
    if curr_sign=='<' and last_sign=='>':
        return True
    elif curr_sign=='>' and last_sign=='<':
        return True
    else:
        return False

def maxTurbulenceSize(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    if len(arr) == 1: #Edge Case
        return len(arr)
    
    if len(arr) == 2:
        if get_sign(arr[1], arr[0])=='=':
            return 1
        else:
            return 2
        
    # If all values are equal then max size is 1
    if len(set(arr))==1:
        return 1
    
    L = 0
    last_sign = get_sign(arr[1], arr[0])
    if last_sign == '=':
        max_size = 1
    else:
        max_size = 2

    for R in range(2, len(arr)):
        curr_sign = get_sign(arr[R], arr[R-1])
        # print("Last Sign", last_sign)
        # print("Curr Sign", curr_sign)
        if curr_sign=="=":
            # No longer a valid window
            # Skip L to R+1
            # As we know that at = not valid
            # So start ahead of it
            L = R+1
            last_sign = curr_sign
        elif check_opposite_signs(curr_sign, last_sign):
            # Is a valid window, update max_size
            max_size = max(max_size, R-L+1)
            last_sign = curr_sign
        else:
            # Not a valid window, get L to R-1
            # As from there it can be valid
            L = R-1
            last_sign = curr_sign
    return max_size

arr = [11]
print(maxTurbulenceSize(arr))
arr = [11, 12, 6, 8, 4, 4, 5, 3, 7, 2]
print(maxTurbulenceSize(arr))
arr = [9,4,2,10,7,8,8,1,9]
print(maxTurbulenceSize(arr))
arr = [2, 2, 2, 2, 2]
print(maxTurbulenceSize(arr))
arr = [4,8,12,16]
print(maxTurbulenceSize(arr))
arr = [1, 1, 2]
print(maxTurbulenceSize(arr))
arr = [1, 1, 1]
print(maxTurbulenceSize(arr))


        
        
