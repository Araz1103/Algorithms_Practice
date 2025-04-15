import copy

list_of_lists = [[1, 2], [3, 4]]
shallow = list_of_lists.copy()
deep = copy.deepcopy(list_of_lists)

# Modify the original inner list
list_of_lists[0][0] = 99

print(shallow)  # [[99, 2], [3, 4]]  <- Affected by change!
print(deep)     # [[1, 2], [3, 4]]   <- Fully independent

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

