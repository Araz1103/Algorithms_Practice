# First understand deque concepts

from collections import deque

queue = deque()

queue.append(1) # [1]
queue.append(2) # [1, 2]
queue.append(3) # [1, 2, 3]
queue.pop() # [1, 2]

print(queue)
print(type(queue))

print(queue.popleft()) # [2]
queue.appendleft(3) # [3, 2]
queue.append(7) # [3, 2, 7]

print(queue)

# Append, Popleft, Pop, Appendleft are all O(1)


# Since deques are implemented as Linked Lists, Getting an element at index i is O(n)
# so queue[3] is O(N)
print(queue[1])

# Getting first and last element is O(1)
print(deque[0])
print(deque[-1])

# Extends are O(K) for how many elements are extended with
# Like appending K times

# Extend deque with multiple elements at the right
queue.extend([0, 7, 9])
print("After extend:", queue)  # deque([3, 2, 7, 0, 7, 9])

# Extend deque with multiple elements at the left
queue.extendleft([5, 6, 7]) # deque([7, 6, 5, 3, 2, 7, 0, 7, 9])
print("After extendleft:", queue)  
# Note: extendleft adds elements in reverse order so that 7 becomes the new leftmost element.

# Summary
"""
Operation	        Time Complexity (Average)
-----------------------------------------------
append(x)	                    O(1)
appendleft(x)	                O(1)
pop()	                        O(1)
popleft()	                    O(1)
extend(iterable)	            O(k) for k elements
Indexing	                    O(n) (worst-case)
Insertion/Deletion in Middle	O(n)
------------------------------------------------
"""

# Sample Problem
"""
rotate_list(arr: List[int], k: int) -> Deque[int] 
Takes a list of integers arr and an integer k. 
It should convert the list into a deque, then rotate the values in the list to the left by k steps and return the resulting deque.
Example: rotate_list([1, 2, 3, 4, 5], 2) should return deque([3, 4, 5, 1, 2]).
"""

from typing import List, Deque

def rotate_list(arr: List[int], k: int) -> Deque[int]:
    arr_deque = deque(arr) #O(N) to convert in deque

    # For each rotate, we pop from left and append that to the right
    for i in range(k%len(arr)): # O(k%N)
        leftmost = arr_deque.popleft() #O(1)
        arr_deque.append(leftmost) #O(1)

    return arr_deque # Total Time complexity is O(N + k) and Space is O(N) since new deque is created


print("Left Rotation")
print(rotate_list([1, 2, 3, 0, 6, 7], 4))
print(rotate_list([1, 2, 3, 0, 6, 7], 0))
print(rotate_list([1, 2, 3, 0, 6, 7], 20))

"""
Implement the following function using the queue operations described above:

rotate_list(arr: List[int], k: int) -> Deque[int] that takes a list of integers arr and an integer k. It should convert the list into a deque. And next, rotate the values in the list to the right by k steps and return the resulting deque.
Example: rotate_list([1, 2, 3, 4, 5], 2) should return deque([4, 5, 1, 2, 3]).
"""

def rotate_list(arr: List[int], k: int) -> Deque[int]:
    arr_deque = deque(arr) #O(N) to convert in deque

    # For each rotate, we pop from left and append that to the right
    for i in range(k%len(arr)): # O(k%N)
        righmost = arr_deque.pop() #O(1)
        arr_deque.appendleft(righmost) #O(1)

    return arr_deque # Total Time complexity is O(N + k) and Space is O(N) since new deque is created

print("Right Rotation")
print(rotate_list([1, 2, 3, 0, 6, 7], 4))
print(rotate_list([1, 2, 3, 0, 6, 7], 0))
print(rotate_list([1, 2, 3, 0, 6, 7], 20))



