from typing import List

def perculate_max_down(position, heap):
    # Check while left child exists
    while 2*position < len(heap):
        # Check if Right Child Exists
        # And if RC > Left Child
        # If current element < RC
        if (2*position + 1 < len(heap)) and \
            (heap[2*position + 1] > heap[2*position]) and \
            (heap[position] < heap[2*position + 1]):
            # Swap with Right Child
            heap[position], heap[2*position + 1] = heap[2*position + 1], heap[position]
            position = 2*position + 1 #New position

        # Check if Current Element < Left Child
        elif heap[position] < heap[2*position]:
            # Swap with LC
            heap[position], heap[2*position] = heap[2*position], heap[position]
            position = 2*position #New position
        else: #Max of both child, @correct position
            break

    return heap #since we change in place, don't really need to return

def pop_max(heap):
    # If empty array, return None
    if len(heap)==1:
        return None
    if len(heap)==2: #pop & return 1 element in heap
        return heap.pop()
    
    # Pop root and put last element there
    max_element = heap[1]
    last_element = heap.pop()

    # Make root last element
    heap[1] = last_element
    # Now perculate root down
    perculate_max_down(1, heap)
    return max_element

def max_heapify(arr):
    heap = arr + [arr[0]] #first element ignored

    curr_position = (len(heap)-1)//2

    while curr_position > 0:
        perculate_max_down(curr_position, heap)
        curr_position -=1

    return heap

def push(heap, val):
    # Add #end
    # Then keep checking with parent, if < parent or not, until reach root
    heap.append(val)

    curr_position = len(heap)-1
    # Since max heap, parent must be bigger
    # If not we swap
    # Until we reach root
    while curr_position > 1 and heap[curr_position] > heap[curr_position//2]:
        heap[curr_position], heap[curr_position//2] = heap[curr_position//2], heap[curr_position]
        curr_position = curr_position//2

def lastStoneWeight(stones: List[int]) -> int:
    # Check length of stones array
    # If 1, return the element
    # If > 1:
    #   Max Heapify the stones array: O(N)

    if len(stones) == 1:
        return stones[0]
    
    heap = max_heapify(stones)

    # Then from our heap, we keep popping 2 elements
    # Before popping 1st, check if Heap empty
    # If it is, return 0
    # After 1st pop, check if Heap is empty or not
    # If Heap is empty -> Return the popped element
    # Else after 2nd pop
    # Get difference of 2 elements:
    # If difference is 0, continue, do nothing
    # If difference > 0, push this to the heap
    # Since pops and pushes are Log(N)
    # And max we will do n or 2*n times
    # Complexity is N + 2*N(Log(N)) -> N*Log(N)
    while (len(heap) > 1): #Heap is not empty
        print(f"heap is: {heap[1:]}")
        # Pop First Element
        heaviest_stone = pop_max(heap)
        print(f"Heaviest Stone is: {heaviest_stone}")
        # If heap is empty, return this
        if len(heap)==1:
            return heaviest_stone
        
        # If not empty, then pop 2nd
        second_heaviest_stone = pop_max(heap)
        print(f"2nd Heaviest Stone is: {second_heaviest_stone}")

        difference_stone = heaviest_stone - second_heaviest_stone
        if difference_stone > 0: #Some weight remains
            push(heap, difference_stone)

    return 0

print(lastStoneWeight([1, 1, 2, 2]))
print(lastStoneWeight([7,5,8]))

print("Using heapq")
import heapq

def lastStoneWeight(stones: List[int]) -> int:
    # We heapify to get a max heap
    # Until heap is empty
    # We do 2 pops
    # If post first pop, if heap is empty, we return that
    # Else we get the difference 
    # If difference is > 0, we push it in the heap
    # If heap is empty we return 0
    max_stones = [-stone for stone in stones] #Since we want max heap
    heapq.heapify(max_stones) #O(N)

    while len(max_stones):
        print(f"Heap is: {max_stones}")
        # Do first pop
        heaviest_stone = -heapq.heappop(max_stones) #O(LogN)
        print(f"Heaviest Stone: {heaviest_stone}")
        if len(max_stones):
            # Do second pop
            second_heaviest_stone = -heapq.heappop(max_stones) #O(LogN)
            print(f"2nd Heaviest Stone: {second_heaviest_stone}")
            weight_difference = heaviest_stone - second_heaviest_stone
            print(f"Weight Difference: {weight_difference}")
            if weight_difference > 0:
                # we push this to the heap
                heapq.heappush(max_stones, -weight_difference) #O(LogN)
        else:
            return heaviest_stone
    return 0

print(lastStoneWeight([1, 1, 2, 2]))
print(lastStoneWeight([7,5,8]))

        

        