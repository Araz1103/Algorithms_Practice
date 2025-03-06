"""
Design a Minimum Heap (aka a Priority Queue) class.

Your MinHeap class should support the following operations:

MinHeap() will initialize an empty minimum heap.
void push(int val) will add val to the heap.
int pop() will remove and return the smallest element in the heap. If the heap is empty, return -1.
int top() will return the smallest element in the heap without removing it. If the heap is empty, return -1.
void heapify(int[] nums) will build a minimum heap from nums.
Note: push and pop should be implemented in O(logn) time complexity, 
while top should be implemented in O(1),
and heapify should be implemented in O(n) time complexity.
"""

from typing import List

class MinHeap:
    
    def __init__(self):
        self.heap = [None]
        
    def push(self, val: int) -> None:
        # First append to the heap
        # Then keep comparing with the parent, swap, if < parent or until @root
        self.heap.append(val)
        i = len(self.heap) - 1
        # O(Log(N))
        while i > 1 and self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def perculate_down(self, position):
        # Check while left child exists
        # If it doesn't, this means no children exist, can stop
        while 2*position < len(self.heap): #Len of Heap can tell us last index

            # Check if Right Child Exists
            # If it does, is it less than left child
            # If it is, then is the right child < current element
            # If it is, we swap with right child, as it is the minimum
            if (2*position + 1) < len(self.heap) and \
               (self.heap[2*position + 1] < self.heap[2*position]) and \
               (self.heap[2*position + 1] < self.heap[position]):
                # Swap with Right Child
                self.heap[position], self.heap[2*position + 1] = self.heap[2*position + 1], self.heap[position]
                # New position is @right child
                position = 2*position + 1

            # If above not matching, then we can check if current element > left child
            elif (self.heap[position] > self.heap[2*position]):
                # Swap with Left Child
                self.heap[position], self.heap[2*position] = self.heap[2*position], self.heap[position]
                # New position is @left child
                position = 2*position

            else: # This means current element is min, so correct position can break
                break


    def pop(self) -> int:

        if len(self.heap)==1: #Empty heap
            return -1
        
        if len(self.heap)==2: # Only 1 element
            return self.heap.pop()
        
        # Otherwise we swap root with the last element
        # Perculate down from root until satisfied
        current_min = self.heap[1]
        last_element = self.heap.pop()
        self.heap[1] = last_element #Make it new root

        # Call perculating down from root, i = 1
        self.perculate_down(position=1) # O(Log(N))
        return current_min
        

    def top(self) -> int:
        if len(self.heap)==1: #Empty heap
            return -1
        return self.heap[1] #O(1)
        

    def heapify(self, nums: List[int]) -> None:
        # If nums is empty, we do nothing
        if not nums:
            return 
        
        # First we take nums, and append the first element @end
        # Then can assign it to our heap
        nums.append(nums[0])
        self.heap = nums # Initialised
        # Now we need to check from @end
        # Can skip half, as they won't have children
        # Check for each position, if we need to perculate it down
        # Last index of heap is len(self.heap) - 1
        current_position = (len(self.heap) - 1)//2 # Will give index of half from end
        # O(N) overall
        while current_position > 0: #We want to check till index 1, start of heap
            self.perculate_down(current_position)
            current_position-=1 #Decrement to check the next node (we go in reverse)
        