"""
This script demonstrates the usage of the `bisect` module in Python, 
which provides efficient binary search-based operations on sorted lists.

The `bisect` module includes:

1. **Finding the correct insertion index** using `bisect_left()` and `bisect_right()` to locate where an element should be inserted.
2. **Inserting elements efficiently** using `insort_left()` and `insort_right()` to maintain sorted order.
3. **Finding the closest number** to a target in a sorted list using binary search.
4. **Maintaining a sorted leaderboard** by efficiently inserting scores while keeping the list ordered.

### Key Advantages of `bisect`:
- Provides O(log n) time complexity for searching and inserting into sorted lists.
- Useful for handling ordered datasets without repeatedly sorting them.
- Helps optimize problems requiring sorted order maintenance, such as leaderboards and ranking systems.
"""

import bisect

def demo_bisect_left_right():
    """
    Demonstrates `bisect_left()` and `bisect_right()` usage.
    
    - `bisect_left(lst, x)`: Finds the leftmost index to insert `x` while maintaining order.
    - `bisect_right(lst, x)`: Finds the rightmost index to insert `x` while maintaining order.
    
    Example:
    Given a sorted list [10, 20, 30, 30, 30, 40, 50], `bisect_left(30)` returns 2, while `bisect_right(30)` returns 5.
    """
    lst = [10, 20, 30, 30, 30, 40, 50]
    print("List:", lst)
    print("bisect_left(30):", bisect.bisect_left(lst, 30))  # Finds first occurrence of 30
    print("bisect_right(30):", bisect.bisect_right(lst, 30))  # Finds last occurrence of 30

def demo_insort_left_right():
    """
    Demonstrates `insort_left()` and `insort_right()` usage.
    
    - `insort_left(lst, x)`: Inserts `x` at the leftmost valid position while maintaining order.
    - `insort_right(lst, x)`: Inserts `x` at the rightmost valid position while maintaining order.
    
    Example:
    Given [10, 20, 30, 40, 50], inserting 30 using `insort_left()` results in [10, 20, 30, 30, 40, 50].
    """
    lst = [10, 20, 30, 40, 50]
    print("\nOriginal List:", lst)
    bisect.insort_left(lst, 30)  # Insert at leftmost valid position
    print("After insort_left(30):", lst)
    bisect.insort_right(lst, 30)  # Insert at rightmost valid position
    print("After insort_right(30):", lst)

def find_closest(lst, target):
    """
    Finds the closest number to the target in a sorted list using `bisect_left()`.
    
    - If `target` is smaller than all elements, return the first element.
    - If `target` is larger than all elements, return the last element.
    - Otherwise, compare the nearest left and right values and return the closest.
    
    Example:
    Given [1, 3, 5, 7, 9, 11], the closest number to 6 is 5, and to 10 is 9.
    """
    pos = bisect.bisect_left(lst, target)
    
    if pos == 0:
        return lst[0]
    if pos == len(lst):
        return lst[-1]
    
    before = lst[pos - 1]
    after = lst[pos]
    return before if target - before <= after - target else after

def demo_find_closest():
    """
    Demonstrates finding the closest number using `bisect`.
    
    Uses `find_closest()` to return the nearest value to a given target in a sorted list.
    """
    lst = [1, 3, 5, 7, 8, 11]
    print("\nSorted List:", lst)
    print("Closest to 6:", find_closest(lst, 6))
    print("Closest to 10:", find_closest(lst, 10))

def maintain_leaderboard():
    """
    Demonstrates maintaining a sorted leaderboard efficiently using `bisect`.
    
    - `insort()` helps insert new scores while keeping the list sorted.
    - This ensures that rankings can be managed in O(log n) time instead of O(n).
    
    Example:
    Given [10, 20, 30, 40, 50], inserting 35 keeps it sorted as [10, 20, 30, 35, 40, 50].
    """
    scores = [10, 20, 30, 40, 50]
    print("\nInitial Scores:", scores)
    bisect.insort(scores, 35)  # Insert while maintaining order
    print("After inserting 35:", scores)
    bisect.insort(scores, 45)
    print("After inserting 45:", scores)

def main():
    """
    Runs all demonstrations for the `bisect` module.
    """
    demo_bisect_left_right()
    demo_insort_left_right()
    demo_find_closest()
    maintain_leaderboard()

if __name__ == "__main__":
    main()
