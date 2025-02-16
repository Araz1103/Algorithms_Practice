from typing import List
from math import ceil

def check_satisfy_banana(piles, k, h):
    # Basically go in each pile
    # Keep subtracting k, and count for h taken
    # Until pile is <= 0
    # Final count if <= h, it satisfies
    count_h = 0
    for pile in piles: # Time complexity O(N)
        # Avoid while loop, increases operations
        # pile_count = pile
        # while pile_count > 0:
        #     pile_count -= k
        #     count_h +=1
        # Single Operation for count
        count_h += ceil(pile/k)
    
    return count_h <= h

def minEatingSpeed(piles: List[int], h: int) -> int:
    left_idx = 1
    max_k = max(piles) #Time complexity O(N)

    right_idx = max_k # This is the max K, which will definetly eat all bananas
    # We do a binary search, where we check until which K will it satisfy eating all banans
    # We keep the min k found with us
    min_k_found = max_k

    while left_idx <= right_idx: # Binary Search Time Complexity is O(Log(max_k)) but for each step it is O(N)

        mp_idx = int(left_idx + (right_idx - left_idx)/2)

        if check_satisfy_banana(piles, mp_idx, h): # O(N)
            min_k_found = mp_idx
            # Check if any more can be found on left
            right_idx = mp_idx - 1
        else: # If doesn't satisfy, we need to check higher values of k on right
            left_idx = mp_idx + 1

    return min_k_found # Total is O(N*Log(max_k))


piles=[1,4,3]
h=3

piles=[1,4,3,1]
h=6

piles=[1,4,3,2]
h=9

print(minEatingSpeed(piles, h))
    