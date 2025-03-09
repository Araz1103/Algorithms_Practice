"""
You are given two integer arrays, nums1 and nums2, both of length n, along with a positive integer k.

For each index i from 0 to n - 1, perform the following:

Find all indices j where nums1[j] is less than nums1[i].
Choose at most k values of nums2[j] at these indices to maximize the total sum.
Return an array answer of size n, where answer[i] represents the result for the corresponding index i.

 
Example 1:
Input: nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2

Output: [80,30,0,80,50]

Explanation:
For i = 0: Select the 2 largest values from nums2 at indices [1, 2, 4] where nums1[j] < nums1[0], resulting in 50 + 30 = 80.
For i = 1: Select the 2 largest values from nums2 at index [2] where nums1[j] < nums1[1], resulting in 30.
For i = 2: No indices satisfy nums1[j] < nums1[2], resulting in 0.
For i = 3: Select the 2 largest values from nums2 at indices [0, 1, 2, 4] where nums1[j] < nums1[3], resulting in 50 + 30 = 80.
For i = 4: Select the 2 largest values from nums2 at indices [1, 2] where nums1[j] < nums1[4], resulting in 30 + 20 = 50.

Example 2:
Input: nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1

Output: [0,0,0,0]

Explanation:
Since all elements in nums1 are equal, no indices satisfy the condition nums1[j] < nums1[i] for any i, resulting in 0 for all positions.

Constraints:

n == nums1.length == nums2.length
1 <= n <= 105
1 <= nums1[i], nums2[i] <= 106
1 <= k <= n
"""

# Find all indices j where nums1[j] is less than nums1[i].
# For this if we sort the array first and pre-compute for all indices
# So rather than O(n^2) can have this in O(n.log(n))

def find_all_min(nums):
    if len(nums)==1:
        return {nums[0]: []} #no such indices exist
    
    sorted_nums = sorted([(num, idx) for idx, num in enumerate(nums)]) #O(N*Log(N))
    #print(sorted_nums)
    all_less_dict = {sorted_nums[0][0]: []} #least element in nums will have nothing less than
    running_index = [sorted_nums[0][1]] #keeps storing indices in ascending order, so can accordingly add for strictly <
    for idx in range(1, len(sorted_nums)):
        # Check if new element or not
        if sorted_nums[idx][0]!=sorted_nums[idx-1][0]:
            # New element, must be gt prev element
            # create new entry in dict with all indices till now, as they are lt this
            all_less_dict[sorted_nums[idx][0]] = running_index[:] #Remember to add a copy, as mutable!
        # Add in running index too
        running_index.append(sorted_nums[idx][1])
        # print(all_less_dict)
        # print(running_index)

    return all_less_dict

#print(find_all_min([14, 2, 1, 5, 3]))
#print(find_all_min([4, 2, 1, 1, 5, 3, 0]))

# Now for nums 2, we want the indices corresponding, to lt, and then choose 2 to maximise sum
# For that, we can take all elements at those indices, using heaps, get largest k? 
# Then get the sum of that?
import heapq

def findMaxSum(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[int]
    """
    res = []
    all_min_indices = find_all_min(nums1) #O(N*Log(N))

    for num in nums1:
        min_indices = all_min_indices[num] #Will return all min indices in O(1)
        # Get all elements from nums2 @these indices
        nums2_idx_elements = [nums2[idx] for idx in min_indices]
        # Now we want the sum of the top k elements here!
        if k >= len(nums2_idx_elements): #No need to choose, return sum of all
            res.append(sum(nums2_idx_elements))
        else:
            # We can use a heap to get nlargest elements
            # Time complexity is O(n*log(k)), where n is num selected indices, and k is selecting them
            # For each of the n elements, adding or popping from min heap is log(k)
            res.append(sum(heapq.nlargest(k, nums2_idx_elements)))

    return res #Total Time Complexity is O(N*Log(N) + )

# nums1 = [4,2,1,5,3]
# nums2 = [10,20,30,40,50]
# k = 2
# print(findMaxSum(nums1, nums2, k))

# nums1 = [2,2,2,2]
# nums2 = [3,1,2,3]
# k = 1
# print(findMaxSum(nums1, nums2, k))

from typing import List
from heapq import heappop, heappush
# More Optmized Approach
def findMaxSum(nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        result = [0] * n

        # Create a sorted list of tuples (nums1_value, original_index)
        # Sorting ensures we process elements in increasing order of nums1.
        sorted_nums1 = sorted((nums1[i], i) for i in range(n))
        print(sorted_nums1)
        
        # min_heap will store the nums2 values of elements that satisfy nums1[j] < current nums1[i].
        min_heap = []
        current_heap_sum = 0  # Sum of values currently in the heap.
        left_pointer = 0      # Points to the smallest unprocessed element in sorted_nums1.
        max_sum_for_index = {}  # Maps each original index to the computed sum of top k nums2 values.

        # Process each element in sorted order of nums1.
        for right_pointer in range(n):
            print(left_pointer, right_pointer)
            print(sorted_nums1[left_pointer], sorted_nums1[right_pointer])
            current_original_index = sorted_nums1[right_pointer][1]
            current_value = sorted_nums1[right_pointer][0]

            # Add all elements from the left (with strictly smaller nums1 values)
            # into the min_heap.
            while left_pointer < right_pointer:
                candidate_value, candidate_index = sorted_nums1[left_pointer]
                # Because sorted_nums1 is in increasing order,
                # once we hit a candidate that is not less than current_value, we stop.
                if candidate_value >= current_value:
                    break

                # Push the corresponding nums2 value for candidate_index.
                heapq.heappush(min_heap, nums2[candidate_index])
                current_heap_sum += nums2[candidate_index]
                print(current_heap_sum)

                # If the heap size exceeds k, remove the smallest element.
                if len(min_heap) > k:
                    current_heap_sum -= heapq.heappop(min_heap)
                left_pointer += 1
                print(current_heap_sum)

            # Record the current sum for this original index.
            max_sum_for_index[current_original_index] = current_heap_sum
            print(max_sum_for_index)
            print("----------------------")

        # Build the result array by retrieving computed sums for each original index.
        for i in range(n):
            result[i] = max_sum_for_index.get(i, 0)

        return result

nums1 = [4,2,1,5,3,1]
nums2 = [10,20,30,40,50,80]
k = 2
print(findMaxSum(nums1, nums2, k))

# nums1 = [2,2,2,2]
# nums2 = [3,1,2,3]
# k = 1
# print(findMaxSum(nums1, nums2, k))

"""
### Algorithm Comparison: Optimized Two-Pointer + Heap vs. Naive Dictionary-Based Approach

#### **Naive Approach (Dictionary-Based Filtering + Sorting)**
1. **Preprocessing (`find_all_min`)**
   - Sort `nums1` along with indices: **O(n log n)**
   - Build a dictionary of indices where `nums1[j] < nums1[i]`: **O(n)**
   - **Total preprocessing time:** **O(n log n)**

2. **Processing Each Element in `nums1`**
   - For each `nums1[i]`, lookup indices in O(1).
   - Extract corresponding `nums2` values (can be O(n) worst case).
   - Use `heapq.nlargest(k, ...)` to get the largest `k` elements: **O(n log k)**.
   - **Total per element:** **O(n log k)** worst case.
   - **Total complexity:** **O(n² log k)** worst case.

#### **Optimized Approach (Two-Pointer + Heap)**
1. **Sorting Step:**
   - Sort `nums1` along with indices: **O(n log n)**

2. **Processing with Two Pointers & Heap**
   - Iterate over sorted `nums1`, using a two-pointer approach to maintain valid candidates.
   - Push candidates to a min-heap of size `k` (each push/pop is **O(log k)**).
   - Each element in `nums1` is processed **once**, and the pointer only moves forward.
   - **Overall complexity:** **O(n log n) + O(n log k) ≈ O(n log n)**.

#### **Comparison**
| Approach         | Sorting | Per Element Work | Total Complexity |
|-----------------|---------|------------------|------------------|
| Dictionary-Based | O(n log n) | O(n log k) worst case | O(n² log k) |
| Two-Pointer + Heap | O(n log n) | O(log k) per element | O(n log n) |

#### **Conclusion**
- The naive approach performs redundant filtering for each element, leading to **O(n² log k)** worst-case complexity.
- The optimized approach ensures each element is processed only **once** using a **two-pointer + heap** technique, reducing complexity to **O(n log n)**.
- The optimized method is significantly faster for large `n`, as **O(n log n) is much better than O(n² log k)**.
"""