"""
# Find the length of longest subarray with the same 
# value in each position: O(n)
Example:
[1, 2, 3, 3, 4, 3, 3, 4, 4, 4]
Longest is 3 of [4, 4, 4]
"""

def get_longest_subarray_dups(arr):
    L = 0
    longest_len = 0
    longest_arr = []
    for R in range(len(arr)):
        if arr[L]==arr[R]:
            longest_len = max(longest_len, (R - L +1))
            longest_arr = arr[L:R+1]
        else:
            # Rather than incrementally upgrade L until they are equal
            # Just directly assing
            # As logically all till R must not be equal
            L = R

    return longest_len, longest_arr

print(get_longest_subarray_dups([1, 1, 1, 2, 1, 3, 4, 5, 2, 2, 2, 2, 2, 1, 0]))
print(get_longest_subarray_dups([1, 2, 3, 3, 4, 3, 3, 4, 4, 4]))
print(get_longest_subarray_dups([1, 2, 2, 3, 4, 3, 4]))