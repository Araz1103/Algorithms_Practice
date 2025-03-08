"""
Given 2 sorted arrays, return the intersection of both the arrays. The intersection of 2 arrays means all the elements which are present in both.

Example
Array 1: [1, 3, 4, 5, 5, 6, 6, 7]
Array 2: [2, 5, 6, 6, 7, 8]
Intersection: [5, 6, 6, 7]
Note: The resultant array should also be sorted.
"""
from typing import List
def intersection(A: List[int], B: List[int]) -> List[int]:
		# add your logic here
        # Basically maintain 2 pointers, in each list
        # We check if the elements are equal
        # If they are, we can add to result intersection list
        # If not, whichever is smaller, we increment that
        # Keep checking while either of them goes out of bounds
        i = 0
        j = 0
        intersection_list = []
        while i < len(A) and j < len(B):
            if A[i]==B[j]:
                intersection_list.append(A[i])
                i+=1
                j+=1
            elif A[i] < B[j]:
                #increment i
                i+=1
            else:
                #increment j
                j+=1
        return intersection_list

print(intersection([1, 1, 2, 3], [4, 5, 6]))
print(intersection([1, 1, 2, 3, 4], [4, 5, 6]))
print(intersection([1, 1, 2, 3, 4, 5, 5, 6, 8, 9], [1, 1, 4, 5, 5, 6, 7, 8]))
