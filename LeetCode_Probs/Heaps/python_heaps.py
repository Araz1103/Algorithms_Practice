import heapq
from typing import List


# To push in Heaps using heapq
# heapq.heappush(heap_you_use, value_to_push) Time: O(Log(N)) Space: O(N) for storing elements
# To get top priority element from heap, heap[0] # Python abstracts the 1st indexing #O(1)
# Default heapq makes a min heap

print("Pushing!")
def heap_push(heap: List[int], value: int) -> int:
    heapq.heappush(heap, value)
    return heap[0]


# do not modify below this line
print(heap_push([1, 2, 3], 4))
print(heap_push([1, 2, 3], 0))
print(heap_push([1, 2, 3], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 5))


print("Popping!")
# Default: Pops the smallest element from the heap
# Since Min Heap, so O(1) to access and O(Log(N)) to Pop (as needs to perculate down post popping)
def heap_pop(heap: List[int]) -> List[int]:
    # Must pass a heap to this
    return heapq.heappop(heap)

def heap_pop_all(heap: List[int]) -> List[int]:
    all_elements = []
    while heap:
        all_elements.append(heapq.heappop(heap))
    return all_elements #N*Log(N)

# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9]))
# If empty we get index error
#print(heap_pop([]))

print(heap_pop_all([1, 2, 3]))
print(heap_pop_all([1, 3, 2]))
print(heap_pop_all([6, 7, 8, 12, 9, 10, 11]))

import heapq

heap = []

heapq.heappush(heap, "zara")
heapq.heappush(heap, "banana")
heapq.heappush(heap, "apple")
heapq.heappush(heap, "kiwi")
print(heap)
# Min is apple -> banana -> kiwi
print(heapq.heappop(heap))  # apple
print(heap)
print(heapq.heappop(heap))  # banana
print(heapq.heappop(heap))  # kiwi

# heapify is O(N)

def heapify_strings(strings: List[str]) -> List[str]:
    heapq.heapify(strings) #Does in place, returns None
    return strings

print(heapify_strings(["b", "a", "e", "c", "d"]))


def heapify_integers(integers: List[int]) -> List[int]:
    heapq.heapify(integers)
    return integers

def heap_sort(nums: List[int]) -> List[int]:
    sorted_nums = []
    heapq.heapify(nums)
    while nums:
        sorted_nums.append(heapq.heappop(nums))

    return sorted_nums

print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
print(heap_sort(["b", "a", "e", "c", "d"]))

# Max Heap
# Since python does not have built in max heap
# For numbers we can negate the signs, and when fetching negate back
# So min becomes max

def get_reverse_sorted(nums: List[int]) -> List[int]:
    # If we cannot max heapify, will have to push one by one
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num) #negate for max heap
    
    reverse_nums = []
    while max_heap:
        # Negate back
        reverse_nums.append(-heapq.heappop(max_heap))

    return reverse_nums

print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))

"""
Unfortunately, Python does not have a custom key parameter for the heapq module. 
This means that we cannot directly create a heap with custom priorities. 
However, we can simulate a custom heap by using a tuple as the element in the heap.

With tuples, Python will use the first element of the tuple as the priority. 
If two tuples have the same first element, Python will compare the second element of the tuples, and so on.

If we wanted to create a heap of integers by using the absolute value of each integer as the priority, 
we could use the following code:
"""

nums = [4, -2, 3, -5]
heap = []

for num in nums:
    pair = (abs(num), num)
    heapq.heappush(heap, pair)

while heap:
    pair = heapq.heappop(heap)
    original_num = pair[1]
    print(original_num)

# Using this can simulate max heap

def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []
    for num in nums:
        heap_pair = (-num, num) # As will consider first element of tuple to compare
        heapq.heappush(max_heap, heap_pair)

    reverse_nums = []
    while max_heap:
        reverse_nums.append(heapq.heappop(max_heap)[1])

    return reverse_nums

print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))

# Get N Smallest Elements from Heap
"""
The time complexity of heapq.nsmallest() is O(mlog(n))
where n is the number of elements to return and m is the size of the input.
"""


def get_min_element(arr: List[int]) -> int:
    return heapq.nsmallest(1, arr)[0]


def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    return heapq.nsmallest(4, arr)


def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    min_arr =  heapq.nsmallest(2, arr)
    min_arr.reverse()
    return min_arr


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

def get_max_element(arr: List[int]) -> int:
    return heapq.nlargest(1, arr)[0]


def get_max_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    return heapq.nlargest(4, arr)


def get_max_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    new_arr = heapq.nlargest(2, arr)
    new_arr.reverse()
    return new_arr


print(get_max_element([1, 2, 3]))
print(get_max_element([3, 2, 1, 4, 6, 2]))
print(get_max_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_max_4_elements([4, 9, 7, 3, 2, 7, 4, 6, 2]))
print(get_max_4_elements([4, 9, 7, 2, 1, 3, 2, 3, 4, 6, 2, 3]))
print(get_max_4_elements([4, 7, 2, 3, 2, 4, 6, 2]))

print(get_max_2_elements([4, 5, 3, 7]))
print(get_max_2_elements([8, 8, 7, 9]))
print(get_max_2_elements([1, 2, 3, 9, 8, 7, 6]))





