"""
Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?

Example 1:

Input: nums = [2,3,1,5,4], k = 2

Output: 4
Example 2:

Input: nums = [2,3,1,1,5,5,4], k = 3

Output: 4
Constraints:

1 <= k <= nums.length <= 10000
-1000 <= nums[i] <= 1000

"""
from typing import List
import heapq

def findKthLargest(nums: List[int], k: int) -> int:
    # Basically we need the Kth Largest Element from this Array
    # If we create a min heap of size k
    # We can keep pushing to this
    # If the size becomes greater than k
    # We pop the min from it
    # So @end, the min left will be the kth largest, as all others are greater than it
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # @end we just need to return the minimum
    return min_heap[0]

# One Liner, Internally does the same thing
def findKthLargest(nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1] #Since is in decreasing order, so we want last, kth
    
print(findKthLargest([2, 1, 3, 4, 6, 5, 4, 1], 5))
print(findKthLargest([2, 1, 3, 4, 6, 5, 4, 1], 1))