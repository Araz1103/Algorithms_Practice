def max_adjusted_increasing_subarray_sum(arr):
    """
    Problem:
    --------
    Given an array of integers, the goal is to select a contiguous subarray and "adjust" 
    its elements so that they form a strictly increasing sequence when read from left to right.
    The adjustment means you can lower an element's value (but not raise it), and the sequence 
    must satisfy: adjusted[i] < adjusted[i+1] for all valid i.
    
    The objective is to maximize the sum of these adjusted values. For example:
      - For arr = [7, 4, 5, 2, 6, 5], one optimal solution is to choose subarray [7, 4, 5] 
        and adjust it to [3, 4, 5] (since 3 < 4 < 5), giving a sum of 12.
      - Alternatively, using the subarray [5, 2, 6, 5] and adjusting it to [1, 2, 4, 5] also gives a sum of 12.
    
    Approach:
    ---------
    1. Iterate over every possible ending index `j` in the array, considering a subarray that ends at `j`.
    2. For the subarray ending at `j`, start by taking arr[j] as the last (rightmost) element.
    3. Then extend the subarray backwards (to the left) one element at a time.
    4. For each new element arr[i] added to the left, its maximum allowed adjusted value is:
            min(arr[i], (adjusted value of next element) - 1)
       This enforces that the sequence is strictly increasing.
    5. If at any point the allowed adjusted value becomes 0 or negative, stop extending the subarray.
    6. Keep track of the sum of the adjusted subarray, updating the maximum sum found.
    
    Data Structures and Concepts:
    -----------------------------
    - Brute Force / Exhaustive Search: We try every possible subarray ending at each index.
    - Greedy Adjustment: Each element is adjusted to the maximum possible value without breaking the increasing order.
    - Early Termination: The inner loop stops when further extension is impossible (i.e., adjusted value ≤ 0).
    """
    
    # Debug: print the input array (can be commented out later)
    print("arr", arr)
    
    # Get the length of the array.
    n = len(arr)
    
    # Initialize the variable to store the maximum sum found.
    # If negative values are possible in the input, consider initializing with float('-inf').
    max_sum = 0
    
    # Outer loop: consider every possible subarray ending at index j.
    for j in range(n):
        # Debug: print the current end index of the subarray.
        print("j", j)
        
        # Start with a sum of 0 for the current subarray.
        current_sum = 0
        
        # For the subarray ending at index j, the adjusted value for arr[j] is taken as is.
        adjusted = arr[j]
        current_sum += adjusted
        
        # Debug: print the initial adjusted value and current sum.
        print("Adjusted", adjusted)
        print("Current Sum", current_sum)
        
        # Update max_sum considering the single-element subarray [arr[j]].
        max_sum = max(max_sum, current_sum)
        
        # Inner loop: try to extend the subarray to the left.
        # i goes from j-1 down to 0.
        for i in range(j - 1, -1, -1):
            # Debug: print the current index being considered for extension.
            print("i", i)
            
            # Calculate the allowed adjusted value for arr[i]:
            # It must be less than the previously adjusted value (i.e., adjusted - 1)
            # but cannot be greater than the original arr[i].
            adjusted = min(arr[i], adjusted - 1)
            
            # If the allowed adjusted value is not positive, we stop extending this subarray.
            if adjusted <= 0:
                break
            
            # Add this adjusted value to the current subarray's sum.
            current_sum += adjusted
            
            # Update the maximum sum found so far.
            max_sum = max(max_sum, current_sum)
    
    # Return the maximum adjusted subarray sum found.
    return max_sum

# Example tests and usage:
if __name__ == "__main__":
    # Test Example 1:
    # For the array [7, 4, 5, 2, 6, 5], the optimal adjustment yields a sum of 12.
    arr1 = [7, 4, 5, 2, 6, 5]
    print("Max sum for [7,4,5,2,6,5]:", max_adjusted_increasing_subarray_sum(arr1))
    # Expected output: 12

    # Test Example 2:
    # For the array [2, 9, 4, 7, 5, 2], the optimal adjusted subarray sum is 16.
    arr2 = [2, 9, 4, 7, 5, 2]
    print("Max sum for [2,9,4,7,5,2]:", max_adjusted_increasing_subarray_sum(arr2))
    # Expected output: 16

    # Additional Example:
    # Testing on another array to illustrate usage.
    arr = [7, 7, 4, 5, 2, 6, 5]
    print("Maximum sum of strictly increasing contiguous subarray:", max_adjusted_increasing_subarray_sum(arr))
