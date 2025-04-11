"""
Problem: Sorted Transformed Array

Given a sorted array A of doubles. Compute a new *sorted* array B where each element is obtained
by applying the following quadratic transformation function:

    f(x) = a * x^2 + b * x + c

Input:
    - a, b, c (where a > 0 or a < 0)
    - A sorted array A of doubles

Output:
    - A sorted array B such that B[i] = f(A[i]), and B is sorted.

Example:
    a = 2, b = -2, c = 1
    A = [-5, -4, 1, 2]
    Applying the transformation gives:
        B' = [61, 41, 1, 5]
    After sorting: B = [1, 5, 41, 61]

Goal:
    Achieve the result in O(n) time using two pointers.

--------------------------------------------
Approach & Intuition:

1. **Quadratic Functions and Parabolas**:
   - The transformation is a quadratic function f(x) = ax^2 + bx + c.
   - Depending on the sign of 'a', the parabola opens upwards (a > 0) or downwards (a < 0).
   - In a sorted array, this has a key implication:
     - If a > 0 (U-shaped): Maximum transformed values will be at the ends of the input array.
     - If a < 0 (n-shaped): Minimum transformed values will be at the ends.

2. **Two Pointer Strategy**:
   - Because A is sorted, we can use two pointers (left and right) to scan and compare f(A[l]) and f(A[r]).
   - Based on the sign of 'a', we either fill the resulting array from the end (if a > 0) or from the start (if a < 0).
   - This avoids full sorting (O(n log n)) and gives an O(n) solution.

3. **Decision Points**:
   - When a > 0:
     - Fill the transformed array from the end.
     - At each step, insert the larger of f(A[l]) and f(A[r]) and move the corresponding pointer inward.

   - When a < 0:
     - Fill the transformed array from the beginning.
     - Insert the smaller of f(A[l]) and f(A[r]).

"""

def transform_and_sort(a, b, c, A):

    # Quadratic function to apply transformation
    def fx(x):
        return a * (x ** 2) + b * x + c

    len_A = len(A)
    transform_array = [0 for _ in range(len_A)]

    # Determine where to start inserting into the result array
    if a > 0:
        # Parabola opens upwards -> Larger values at the ends
        # So we fill the result array from the end
        element_pointer = len_A - 1
    else:
        # Parabola opens downwards -> Smaller values at the ends
        # So we fill the result array from the beginning
        element_pointer = 0

    l, r = 0, len_A - 1

    while l <= r:
        l_transform = fx(A[l])
        r_transform = fx(A[r])

        if a > 0:
            # Fill from the end with the larger transformed value
            if l_transform >= r_transform:
                transform_array[element_pointer] = l_transform
                l += 1
            else:
                transform_array[element_pointer] = r_transform
                r -= 1
            element_pointer -= 1
        else:
            # Fill from the beginning with the smaller transformed value
            if l_transform <= r_transform:
                transform_array[element_pointer] = l_transform
                l += 1
            else:
                transform_array[element_pointer] = r_transform
                r -= 1
            element_pointer += 1

    return transform_array

# Test case 1: a > 0 (Parabola opens upwards)
a = 2
b = -2
c = 1
A = [-5, -4, 1, 2]
print(transform_and_sort(a, b, c, A))  # Expected: [1, 5, 41, 61]

# Test case 2: a < 0 (Parabola opens downwards)
a = -2
b = 20
c = 1
A = [-5, -4, 1, 2]
print(transform_and_sort(a, b, c, A))  # Expected: [-119, -95, 15, 17]
