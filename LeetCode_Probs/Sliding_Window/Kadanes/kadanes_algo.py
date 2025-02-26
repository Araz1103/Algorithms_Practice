"""
Q: Find a non-empty subarray with the largest sum.
We need to find a group of contiguous elements in an array that result in the maximal sum.

The elements can be negative (otherwise the entire array's sum is maximum lol)

The brute force way to approach this would be to go through every single subarray and calculate the sum,
 while keeping track of the maximum sum.

For every iteration of our outer for loop, our inner loop does linear work. This makes the complexity O(N^2)

But can we do better?
"""

# Intuition
# Basically Kadane's algo says that we can keep iterating through the sub array and keep track of the current sum
# That is like expanding the sub-array
# Until: The current sum is negative
# When that happens, this means that uptil then, whatever we have as the max sum, we just consider till then
# Post that, let's consider new sub arrays starting from there, as previous will only decrease the sum

# Example: Array is:
# 1, 2, 29, 3, -40, 2, 1
# Max sum uptil 3 is: 35
# But when we include -40, the sum becomes -5
# Now if we include 2, we know that the previous sum is negative, so we are better off just starting from 2 a new sub array
# So then from 2 to 1 we have a sub array with sum 3
# So if we keep tracking max sum sub array, it was up till 3
# Therefore in 1 pass, we found that!

def kadanes(arr):
    curr_sum = 0
    #max_sum = arr[0] #As the array can have -ve elements, so either start with any element or -ve infinity
    max_sum = float('-inf')

    for num in arr:
        print(f"@ num: {num}")
        curr_sum = max(curr_sum, 0) # We discard sum of sub array till then if < 0
        curr_sum += num #include element
        print(f"CS is: {curr_sum}")
        max_sum = max(max_sum, curr_sum)
        print(f"Max Sum till now: {max_sum}")

    return max_sum

ip = [1, 2, 29, 3, -40, 2, 1]
print(kadanes(ip))
print("-----------------")
ip = [-11, -5, -29, -3, -40, -2, -1]
print(kadanes(ip))

# Now let's find the sub array for the max sum
# Will use pointers to keep track of the window

def kadanes_sliding_window(arr):
    curr_sum = 0
    #max_sum = arr[0]
    max_sum = float('-inf')

    max_L = 0
    max_R = 0

    L, R = 0, 0 # To track the current sliding window

    for num in arr:
        if curr_sum < 0:
            # Set it to 0, as change our window now
            curr_sum = 0
            # Our Left Pointer becomes equal to the Right Pointer
            L = R
        curr_sum += num
        if curr_sum > max_sum:
            # This is the latest max sum sub array
            max_L = L
            max_R = R
            max_sum = curr_sum # Update the max sum
        R+=1 # Right Pointer keeps expanding the window

    return (max_sum, max_L, max_R)

print("------------Sliding Window-----------")
ip = [1, 2, 29, 3, -40, 2, 1]
print(kadanes_sliding_window(ip))
print("-----------------")
ip = [-11, -5, -29, -3, -40, -2, -1]
print(kadanes_sliding_window(ip))
print("-----------------")
ip = [1, 5, -2, 3, -40, 2, -1]
print(kadanes_sliding_window(ip))