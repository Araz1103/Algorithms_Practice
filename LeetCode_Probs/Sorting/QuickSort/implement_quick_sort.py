

def quick_sort(arr, l, r):
    pivot_element = arr[r] #Picking @last element
    check_swap = l #Pointer telling which element to swap, initialised left most
    # Whenever we encounter < pivot, swap
    # Stop until we reach pivot
    # Check Swap's position has all before lt pivot
    # So swap with pivot
    # Then we can continue left and right halves recursively
    # Base Case if when there's only 1 element
    if l>=r:
        #print(f"Recursion stopped! L: {l} R: {r} arr: {arr[l:r+1]}")
        return #Return, stop recursion
    
    # Iterate from l to r
    for idx in range(l, r+1):
        if idx==r: #reached pivot, stop and swap pivot
            arr[r], arr[check_swap] = arr[check_swap], arr[r]
            #break
        elif arr[idx] <= pivot_element:
            # Swap since less than equal to pivot
            arr[check_swap], arr[idx] = arr[idx], arr[check_swap]
            check_swap +=1
        else: #if gt pivot, we continue
            continue

    # print(f"Arr is now: {arr}")
    # print(f"Check Swap IDX: {check_swap}, Element: {arr[check_swap]}")

    # Now we know elements to left of check swap are lte pivot
    # Pivot is at sorted place
    # Elements to right of check swap are gt pivot
    # So we recursively pass them to sort
    quick_sort(arr, l, check_swap-1)
    quick_sort(arr, check_swap+1, r)
    return #Since sorts in place, don't need to return arr

arr = [1, 3, 2, 4, 6, 5, 6, 7, 8, 2]
print(arr)
quick_sort(arr, 0, len(arr)-1)
print(arr)

arr = [-1, 3, -2, 4, -6, 0, 5, 6, 7, 8, 2]
print(arr)
quick_sort(arr, 0, len(arr)-1)
print(arr)

from typing import List

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        if not pairs:
            return pairs

        def quick_sort(arr, l, r):
            pivot_element = arr[r].key #Picking @last element
            check_swap = l #Pointer telling which element to swap, initialised left most
            # Whenever we encounter < pivot, swap
            # Stop until we reach pivot
            # Check Swap's position has all before lt pivot
            # So swap with pivot
            # Then we can continue left and right halves recursively
            # Base Case if when there's only 1 element
            if l>=r:
                #print(f"Recursion stopped! L: {l} R: {r} arr: {arr[l:r+1]}")
                return #Return, stop recursion
            
            # Iterate from l to r
            for idx in range(l, r+1):
                if idx==r: #reached pivot, stop and swap pivot
                    arr[r], arr[check_swap] = arr[check_swap], arr[r]
                    #break
                elif arr[idx].key < pivot_element:
                    # Swap since less than equal to pivot
                    arr[check_swap], arr[idx] = arr[idx], arr[check_swap]
                    check_swap +=1
                else: #if gt pivot, we continue
                    continue

            # print(f"Arr is now: {arr}")
            # print(f"Check Swap IDX: {check_swap}, Element: {arr[check_swap]}")

            # Now we know elements to left of check swap are lte pivot
            # Pivot is at sorted place
            # Elements to right of check swap are gt pivot
            # So we recursively pass them to sort
            quick_sort(arr, l, check_swap-1)
            quick_sort(arr, check_swap+1, r)
            return #Since sorts in place, don't need to return arr

        quick_sort(pairs, 0, len(pairs)-1)
        return pairs

        