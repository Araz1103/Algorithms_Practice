
# Approach I: Using Subsets, but stopping exploration when curr set size is K

def combinations(n, k):
    """
    Generate all possible combinations of size exactly k from numbers 1 to n.

    Explanation:
    - There are n numbers: {1, 2, ..., n}.
    - We want to generate all subsets of size exactly k (this is "n choose k").

    Time Complexity Analysis:
    - There are exactly C(n, k) = binom(n, k) valid combinations of size k.
    - For each valid combination, copying it to the result array costs O(k).
    - Total time = O(k * binom(n, k))

    Important Note:
    - This is **not a powerset generation (2^n)**.
    - The recursion tree is similar to the powerset tree (each number is included or excluded),
      but the tree is pruned aggressively once the current subset reaches length k.
    - This pruning saves a lot of work compared to full subset generation.

    Space Complexity:
    - Recursion depth = O(n) (in the worst case if k = n, you recurse from 1 to n)
    - Result storage = O(k * binom(n, k)) for all combinations stored.

    Overall:
    - Time: O(k * binom(n, k))
    - Space: O(k * binom(n, k)) for results, plus O(n) recursion stack.
    If we consider upper bound then O(k*2^N), worst case
    """
    combs = []
    helper(1, [], combs, n, k)
    return combs

def helper(i, curComb, combs, n, k):
    """
    Recursive helper to generate combinations.

    Parameters:
    - i: Current number being considered (ranging from 1 to n)
    - curComb: Current partial combination being formed
    - combs: Final list of all valid combinations (output)
    - n: Total numbers (1 to n)
    - k: Desired size of each combination
    """
    if len(curComb) == k:
        # Reached desired size k — this is a valid combination.
        # Make a copy since curComb is mutable and reused.
        combs.append(curComb.copy())
        return

    if i > n:
        # Out of bounds — no more numbers to pick.
        return

    # Choice 1: Include the current number i in the combination.
    curComb.append(i)
    helper(i + 1, curComb, combs, n, k)

    # Backtrack — remove i and explore paths that exclude i.
    curComb.pop()

    # Choice 2: Skip the current number i.
    helper(i + 1, curComb, combs, n, k)


print(combinations(5, 2))

# In python if we want to calculate nCk
import math
n = 5
k = 2
print(math.comb(n, k))

# Approach II, slightly more efficient
"""
We can use a more optimized approach that is O(k * C(n,k)) where 
C(n,k) is the number of combinations we need to generate.

Instead of choose which elements to include or exclude, we can simply choose which elements to include.

For the first element, we can choose from 1 to n.

For the next element, we can choose any except for the one we just chose.

The easiest way to keep track of this and also eliminate duplicate solutions at the same time is to do this: 
- only choose elements in ascending order.
- Choose from 1 to n.
- Choose from x+1 to n where x is the element we chose in step 1.
This way each combination is always generated in sorted order, which is useful because it means 
if we generate [1,2] we will never generate the duplicate [2,1].
"""
# Time: O(k * C(n, k))
def combinations2(n, k):
    combs = []
    # Start from 1 to n
    helper2(1, [], combs, n, k)
    return combs

def helper2(i, curComb, combs, n, k):
    if len(curComb) == k:
        # If size k stop recursion
        combs.append(curComb.copy())
        return
    if i > n:
        # If out of bounds stop
        return

    for j in range(i, n + 1):
        curComb.append(j) #Add element
        # Try adding starting from next element until contraints
        helper2(j + 1, curComb, combs, n, k)
        curComb.pop() #Pop to ensure we can back track

# example:
# n = 5 and k = 3
# So starts @1
# from 1 goes to 2
# So now @2 loop begins
# Was at 1 to 2 -> 3 -> Now K met, return
# Was at 1 to 2 -> 3 was added is popped
# Now from 1 to 2 -> 4 -> Now K met, return
# Was at 1 to 2 -> 4 was added is popped
# Now from 1 to 2 -> 5 -> Now K met, return
# Was at 1 to 2 -> 5 was added is popped
# For loop over as at n
# 2 is popped for 1 -> 2
# Now new is 3
# So 1 to 3 -> 4
# 1 to 3 -> 5
# Then 2 to 3 - 4
# 2 to 3 -> 5
# 3 to 4 -> 5
# Post 4 starts returning as End of Array, K not met so won't add to subsets
print(combinations2(5, 2))