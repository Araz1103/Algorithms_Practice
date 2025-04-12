"""
The median is the middle value in a sorted list of integers. For lists of even length, 
there is no middle value, so the median is the mean of the two middle values.

For example:

For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.
Example 1:

Input:
["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]

Output:
[null, null, 1.0, null, 2.0, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.findMedian(); // return 1.0
medianFinder.addNum(3);    // arr = [1, 3]
medianFinder.findMedian(); // return 2.0
medianFinder.addNum(2);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
Constraints:

-100,000 <= num <= 100,000
findMedian will only be called after adding at least one integer to the data structure.
"""


import heapq

class MedianFinder:

    def __init__(self):
        self.smaller_elements = [] #Max Heap
        self.larger_elements = [] #Min Heap
        
    def addNum(self, num: int) -> None:
        # default add to smaller elements first
        # Since we want max heap, we need to make negative
        heapq.heappush(self.smaller_elements, -1*num)

        # Now check if post adding, 
        # if max of smaller elements is less than min of larger elements
        
        # Check if they are not empty, before checking max and min
        if (self.smaller_elements and self.larger_elements):
            if not (-1*self.smaller_elements[0] < self.larger_elements[0]):
                # If not, we take the max of smaller elements and push in larger elements
                max_smaller_elements = -1*heapq.heappop(self.smaller_elements)
                heapq.heappush(self.larger_elements, max_smaller_elements)

        # Now check that the different in length of the 2 Heaps should not be more than 1
        # If it is, we take the min/max and add to the other heap

        # First check for Smaller Elements
        if (len(self.smaller_elements) - len(self.larger_elements)) > 1:
            # Take from smaller elements and push to larger elements
            max_smaller_elements = -1*heapq.heappop(self.smaller_elements)
            heapq.heappush(self.larger_elements, max_smaller_elements)
        # Now check for Larger Elements
        elif (len(self.larger_elements) - len(self.smaller_elements)) > 1:
            # Take from larger elements and push to smaller elements
            min_larger_elements = heapq.heappop(self.larger_elements)
            heapq.heappush(self.smaller_elements, -1*min_larger_elements)

    def findMedian(self) -> float:
        # Whichever Heap has more elements, we take from that
        if (len(self.smaller_elements) > len(self.larger_elements)):
            return -1*self.smaller_elements[0]

        elif (len(self.smaller_elements) < len(self.larger_elements)):
            return self.larger_elements[0]

        # If both have equal length
        return (-1*self.smaller_elements[0] + self.larger_elements[0])/2

        
        