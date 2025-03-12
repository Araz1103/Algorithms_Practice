"""
Rotate an array to the right by k steps.Example: Input: [1,2,3,4,5,6,7], k = 3, Output: [5,6,7,1,2,3,4
"""
from collections import deque

def rotate(arr, k):
    k = k%len(arr)

    if k==0:
        print(arr)
        return arr

    rotated_arr = deque()
    idx = len(arr)-1
    for i in range(k):
        rotated_arr.appendleft(arr[idx])
        idx=idx-1
    
    rotated_arr = list(rotated_arr) + arr[:-k]
    print(rotated_arr)

rotate([1, 2, 3, 4, 5, 6, 7], 16)

# Simpler

def rotate(arr, k):
    k = k%len(arr)
    arr = list(reversed(arr))

    arr1 = list(reversed(arr[:k]))
    arr2 = list(reversed(arr[k:]))

    return arr1 + arr2

print(rotate([1, 2, 3, 4, 5, 6, 7], 16))

def rotate(arr, k):
    k = k%len(arr)
    arr.reverse()
    arr1 = arr[:k]
    #print(arr1)
    arr2 = arr[k:]
    #print(arr2)
    arr1.reverse()
    arr2.reverse()

    return arr1 + arr2

print(rotate([1, 2, 3, 4, 5, 6, 7], 16))