from typing import List

# Time complexity: O(N*2^N)
# Memory is: O(N)

"""
Generates all possible subsets (the power set) of a given list using backtracking.

Time Complexity:
- O(N × 2^N), where:
    - 2^N is the number of subsets.
    - Each subset takes up to O(N) time to copy and append.

Space Complexity:
- Output storage (sub_sets): O(N × 2^N)
    - We store 2^N subsets.
    - Each subset can be up to size N.
- Call stack: O(N), due to recursion depth.
- curr_set (temporary list used in recursion): O(N)
    - This is reused and does not add to total output space.

Key Notes:
- curr_set is dynamically modified (append/pop) in the recursion.
- curr_set is explicitly copied (`curr_set.copy()`) before adding to output to avoid referencing the same list object.
"""

"""
Difference between `copy()` and `deepcopy()`:

1. **`copy()`**:
   - **Shallow copy**: Creates a new object, but does not recursively copy nested objects (only copies the reference).
   - Any mutable objects (like lists, dictionaries) inside the original object will **remain shared** between the copy and the original.
   - Use `copy()` when:
     - You want to create a new object but don't need to copy nested objects (i.e., just need to copy the top-level object).
     - Changes to nested objects in the copy should reflect in the original object (or vice versa).

   Example:
       ```python
       import copy
       a = [1, [2, 3], 4]
       b = copy.copy(a)
       b[1][0] = 9
       print(a)  # Output: [1, [9, 3], 4] --> Both a and b share the same inner list [2, 3].
       ```

2. **`deepcopy()`**:
   - **Deep copy**: Creates a new object and **recursively** copies all nested objects.
   - This means changes to nested objects in the copied object **do not affect the original object** and vice versa.
   - Use `deepcopy()` when:
     - You want to copy all nested objects, so they are completely independent of the original.
     - You need full independence between the copy and the original object, especially in cases with mutable objects inside mutable objects.

   Example:
       ```python
       import copy
       a = [1, [2, 3], 4]
       b = copy.deepcopy(a)
       b[1][0] = 9
       print(a)  # Output: [1, [2, 3], 4] --> a and b are completely independent.
       ```

### When to use `copy()` vs `deepcopy()`:

- **Use `copy()`**:
  - When you are dealing with **immutable** types (e.g., tuples, strings, integers, etc.), shallow copy is fine because they can't be modified in-place.
  - When you are only interested in copying the **top-level object** and don't mind that nested mutable objects are shared.
  
- **Use `deepcopy()`**:
  - When you are dealing with **mutable objects** (like lists or dictionaries) and want to ensure that the copy is **independent** of the original object, including nested objects.
  - When you need to modify a copy and want to ensure that the original object remains unchanged, even in deeply nested structures.
  
Key Considerations:
- **Performance**: `deepcopy()` is more expensive than `copy()` because it needs to recursively copy every nested object. If you don't need a deep copy, avoid the overhead of copying everything recursively.
- **Memory**: `deepcopy()` creates independent copies of all objects, which consumes more memory compared to `copy()`.

"""



def add_subsets_helper(arr, i, curr_set, sub_sets):
    if i == len(arr): #Last element crossed, fill sub sets
        sub_sets.append(curr_set.copy()) #Fill with a copy, otherwise with reference, can get modified
        return #Stop recursion
    
    # Choose current element
    curr_set.append(arr[i])
    add_subsets_helper(arr, i+1, curr_set, sub_sets)
    curr_set.pop() #Since we also want w/o current element
    # The pop is important to backtrack!
    # Do not choose current element
    add_subsets_helper(arr, i+1, curr_set, sub_sets)

def add_subsets_helper(arr, i, curr_set, sub_sets):
    if i == len(arr): #Last element crossed, fill sub sets
        sub_sets.append(curr_set.copy()) #Fill with a copy, otherwise with reference, can get modified
        return #Stop recursion
    
    # Do not choose current element
    add_subsets_helper(arr, i+1, curr_set, sub_sets)
    # Choose current element
    curr_set.append(arr[i]) #Since we also want with current element
    add_subsets_helper(arr, i+1, curr_set, sub_sets)
    curr_set.pop() #Need this to backtrack!

def subsets(nums: List[int]) -> List[List[int]]:

    sub_sets = []
    curr_set = []

    add_subsets_helper(nums, 0, curr_set, sub_sets)
    return sub_sets

print(subsets([1, 2, 3]))
print(subsets([1, 2, 3, 5]))

        