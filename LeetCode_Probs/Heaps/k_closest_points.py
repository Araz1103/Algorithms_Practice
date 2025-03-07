import heapq
from typing import List

"""
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. 
You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.

Input: points = [[0,2],[2,2]], k = 1

Output: [[0,2]]
Explanation : The distance between (0, 2) and the origin (0, 0) is 2. 
The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

Input: points = [[0,2],[2,0],[2,2]], k = 2

Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted.
"""
class Solution:
    def get_distance(self, x1, x2, y1, y2):
        x_val = (x1-x2)**2
        y_val = (y1-y2)**2
        return (x_val + y_val)**0.5

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Do 1 pass to convert points into distances: O(N)
        # Use heapq.nsmallest() to get
        distances = [((x,y), self.get_distance(x, 0, y, 0)) for (x,y) in points]

        # Basically since we want min distances, let's keep a max heap of k elements
        # Then for every next element, let's push the new element and then pop the max
        # This way will maintain k smallest elements always
        max_heap = []

        for coords, distance in distances:
            # Max heap, so keep negative distance as python heaps are min heaps
            heapq.heappush(max_heap, (-distance, coords))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # @end all elements left in max heap are k smallest
        # So we used O(K) space here BUT we used O(N) Space for precomputed distances!!
        # Time complexity is N*Log(K)
        # For each of the N elements we push and pop so N*(2*Log(K)) = N*Log(K)
        smallest_coords = []
        for distance, coords in max_heap: #O(K)
            smallest_coords.append(coords)

        # Final Time Complexity: O(N + N*Log(K) + k) = O(N*Log(K)) (Dominant Term)

        return smallest_coords
    
    # We optimise space complexity by not pre-computing distances but streaming and calculating on fly
    def kClosestOptimal(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Basically since we want min distances, let's keep a max heap of k elements
        # Then for every next element, let's push the new element and then pop the max
        # This way will maintain k smallest elements always
        max_heap = []

        for x,y in points:
            distance = self.get_distance(x, 0, y, 0)
            # Max heap, so keep negative distance as python heaps are min heaps
            heapq.heappush(max_heap, (-distance, (x,y)))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # @end all elements left in max heap are k smallest
        # So we used O(K) space and time complexity is N*Log(K)
        # For each of the N elements we push and pop so N*(2*Log(K)) = N*Log(K)
        smallest_coords = []
        for distance, coords in max_heap: #O(K)
            smallest_coords.append(coords)

        # Final Time Complexity: O(N + N*Log(K) + k) = O(N*Log(K)) (Dominant Term)

        return smallest_coords

        