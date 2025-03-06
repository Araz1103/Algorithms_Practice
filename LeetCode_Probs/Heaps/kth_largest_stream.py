from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        # We start by taking nums, and only keeping top k elements
        # We store them in a min heap
        # So the top of the heap is kth largest element
        # Everytime we add, we check if val is >= min from heap
        # If it is not, then we can ignore it, as it doesn't affect kth largest element
        # If it is, then we pop the minimum element (OlogN)
        # Then we add this new element (OlogN)
        # @end we return the min element (O(1))

        # to take top k elements, need to sort them in reverse and keep first k
        nums.sort(reverse=True)
        heap_elements = nums[:k] #Since k>=1, this works

        # storing them in a min heap
        # If we store in sorted order, satisfies constraints
        self.heap = [None] #0th index is None
        for i in range(len(heap_elements)-1, -1, -1):
            self.heap.append(heap_elements[i])

        # Now our min heap is ready

        # In case nums is empty @beginning or K is 1 more than nums
        # When adding, we first check size
        # If size is < k, we know post adding it will be k
        # So we don't pop the minimum, we just add @heap
        

    def add(self, val: int) -> int:
        # First check if k is <= size of heap or not
        # If not, then we just add to the heap first
        # Then return minimum
        if self.k > (len(self.heap) - 1):
            self.push_element_heap(val)
            return self.heap[1] # New min, which is kth largest

        # Check if val is >= min of heap
        min_element = self.heap[1]
        if val < min_element:
            # Do nothing to the heap and return min element
            return min_element
        
        # Now we need to update the heap
        # We pop the min element
        # Push the new element
        # Then return the new min from heap
        self.pop_from_heap()
        self.push_element_heap(val)
        return self.heap[1] # New min, which is kth largest

    def push_element_heap(self, val): #O(Log(N)), as perculating up, we can go till height of tree, for balanced tree is O(Log(N))
        # We can directly append to Heap
        # Then check while current element is not root
        # That it is > it's parent
        # If not, we swap with the parent
        # We don't need to check any others, as they are already satisfied from order property
        self.heap.append(val)
        # Get current index
        i = len(self.heap) - 1

        while i > 1 and (self.heap[i] < self.heap[i//2]):
            # Swap with parent
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2 # New index


    def pop_from_heap(self): #O(Log(N)), as perculating down, we can go till height of tree, for balanced tree is O(Log(N))

        # First check Heap exists
        if len(self.heap)==1:
            return None#Means Heap is empty

        # Check if just 1 element, so can directly pop
        if len(self.heap)==2:
            return self.heap.pop() #Pop the last element, which is first and only element

        # Now if we have more than 2 elements
        # We take the last element, and make it the first one
        # Then we perculate down
        last_element = self.heap.pop()

        # Store current min for returning later
        current_min = self.heap[1]
        # Make it the first element
        self.heap[1] = last_element

        # Now perculating down (Min Heap)
        # We keep checking if there is a left child
        # If not, we know there are no children (structure property complete binary tree)
        # So then we can stop, as can't perculate down and order satisfied
        # Otherwise we check if right child exists, and if it does, then we check if right child
        # is less than left child, if it is we check right child is < current element
        # If it is, we can swap with right child (as min overall)
        # Otherwise we check if left child < current element, if it is, swap with left child (so then min overall)
        # Otherwise we know current element is < LC and RC, so at current position, so break out
        i = 1 #Root Node
        while 2*i < len(self.heap): #2*i is left child, if it exists, index must be in heap, so checking < len(heap)

            if (((2*i + 1) < len(self.heap)) and (self.heap[2*i + 1] < self.heap[2*i]) and \
                (self.heap[i] > self.heap[2*i + 1])):
                # Swap with Right Child
                self.heap[i], self.heap[2*i + 1] = self.heap[2*i + 1], self.heap[i]
                i = (2*i + 1) #Now new index

            elif (self.heap[2*i] < self.heap[i]):
                # Swap with Left Child
                self.heap[i], self.heap[2*i] = self.heap[2*i], self.heap[i]
                i = 2*i #New Index

            else:
                break #@correct position

        return current_min # Returning popped element!!
            
            
            
kthLargest = KthLargest(3, [1, 2, 3, 3])
print(kthLargest.add(3)) #// return 3
print(kthLargest.add(5)) #// return 3
print(kthLargest.add(6)) #// return 3
print(kthLargest.add(7)) #// return 5
print(kthLargest.add(8)) #// return 6
print(kthLargest.heap)
print("----------------")
print(kthLargest.add(13))
print(kthLargest.heap)
print(kthLargest.add(12))
print(kthLargest.heap)
print(kthLargest.add(17))
print(kthLargest.heap)
print(kthLargest.add(11))
print(kthLargest.heap)
print(kthLargest.add(19))
print(kthLargest.heap)