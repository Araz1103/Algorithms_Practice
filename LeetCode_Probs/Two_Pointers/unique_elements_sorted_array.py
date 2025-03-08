"""
Given a sorted array A, find the size of array A after removing the duplicate elements.

Examples:
A: [1 2 3 3 3 4 5 5]

Size of A after removing duplicate elements: 5
"""

from typing import List

# Intuition
# Since is sorted, we can just keep checking if next element is same as curr
# Maintain 2 pointers

def removeDuplicates(A: List[int]) -> int:
    if len(A)==1:
        return 1
    
    unique_element_pointer = 0
    num_elements = 1
    for idx in range(1, len(A)):
        if A[idx]==A[unique_element_pointer]: #duplicate element, skip
            continue
        else:
            # Unique element
            num_elements+=1
            unique_element_pointer = idx #New unique element

    return num_elements

print(removeDuplicates([1,1,2,2,3,4,5]))