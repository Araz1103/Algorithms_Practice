"""
Given a sorted input array, return 2 indices of 2 elements which sum up to a target value
Array can contain -ve integers too

Example:
arr = [-1, 2, 3, 4, 7, 9]
target = 7
"""

# Intuition
# Since the array is sorted, we know that the end has the max value and beginning has min value
# We start with a pointer at each end
# We sum up L + R
# If L + R is bigger than the target -> 
# This means that no value can be added with R to bring it down
# Since L is the smallest value available, so shift the R pointer to the left (R-=1)
# If L + R is less than the target ->
# This means that we have to add some bigger value than L for it to add up to the target
# We cannot shift R, as the sum is already lesser than the target
# So try a higher value of L, shift L to the right (L+=1)
# We keep doing this until either we find a L & R meeting the target
# Or L >= R
# (2 unique indices, so L cannot be equal to R as well)
def get_indices(arr, target):
    L = 0
    R = len(arr)-1
    while L < R:
        curr_sum = arr[L] + arr[R]
        if curr_sum==target:
            return (L, R)
        elif curr_sum > target:
            # Shift R
            R-=1
        else:
            # Shift L
            L+=1
    return None #No possible pair of indices

print(get_indices([-1, 2, 3, 4, 7, 9], 7))
print(get_indices([-1, 2, 3, 4, 7, 9], 10))
print(get_indices([-1, 2, 3, 4, 7, 9], 15))
print(get_indices([-1, 2, 3, 4, 7, 9], 8))
print(get_indices([-1, 2, 3, 4, 7, 9], 2))
print(get_indices([-1, 2, 3, 4, 7, 9], 0))