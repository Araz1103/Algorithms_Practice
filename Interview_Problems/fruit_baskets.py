def numOfUnplacedFruits(fruits, baskets):
    """
    :type fruits: List[int]
    :type baskets: List[int]
    :rtype: int
    """
    # For the baskets, we need a way to keep track which are available from L to R
    # Then we basically iterate through fruits, and choose the available one from L to R
    # if a fruit cannot be placed then, increase count of unplaced
    # keep the track of current max, so can directly skip, if none of them have that capacity
    # sort and keep baskets available
    # @each iteration, get value and remove the smallest index
    # so the one left is the next left most available one
    basket_available = {i: 1 for i in range(len(baskets))} #1 indicates available, i is basket index
    basket_count = {}
    for basket in baskets:
        if basket not in basket_count:
            basket_count[basket] = 1
        else:
            basket_count[basket]+=1
    basket_count = dict(sorted(basket_count.items(), reverse=True)) # O(Log(N))
    not_placed = 0
    for fruit in fruits:
        #print(fruit)
        max_basket_available = next(iter(basket_count))
        print(max_basket_available)
        if max_basket_available >= fruit: #Checking only when we know it can be placed
            for basket_index, available in basket_available.items():
                #print(basket_index, available)
                if available and baskets[basket_index] >= fruit:
                    basket_available[basket_index] = 0 #fill it in
                    # We pop this from the dict so faster search next time
                    basket_available.pop(basket_index)
                    # Update basket count dict, so we can always know current max basket available
                    basket_count[baskets[basket_index]]-=1
                    if not basket_count[baskets[basket_index]]:
                        basket_count.pop(baskets[basket_index])
                    break
                
        else:
            not_placed +=1
        print(basket_available)
        print(not_placed)
    return not_placed


fruits = [4,2,5]
baskets = [3,5,4]
# fruits =[3,6,1]
# baskets = [6,4,7]
print(numOfUnplacedFruits(fruits, baskets))

# Maintain a dict of baskets
# keys are the basket values
# values are the basked indices
# We basically check for all baskets >= capacity, what is the minimum index, we pop that
# since for us we don't need index, just need to determine to search or not
# so if we have the max available capacity @every iteration, that should speed things up

"""
4, 2, 5

3, 5, 4

max:
5, 4, 3
@4: max is 5, so search

max: 4, 3
@2: max is 4, so search

max: 4
@5 max is 4, so skip

"""

# Optimised Soln
from bisect import bisect_left
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        """
        Determines the number of fruit types that remain unplaced after allocating fruits to baskets.

        In this problem:
          - We have two arrays of equal length:
              • `fruits`: each element represents the quantity required for a particular fruit type.
              • `baskets`: each element represents the capacity of a basket.
          - The rules for placing fruits are:
              1. Each fruit type must be placed into the leftmost available basket that has a capacity 
                 greater than or equal to the fruit’s quantity.
              2. Each basket can hold only one type of fruit.
              3. If no basket can accommodate a fruit type, it remains unplaced.
          - The function returns the number of fruit types that remain unplaced.

        ### Overall Approach:
        
        The algorithm maintains an "ordered" list of available baskets, stored as tuples (basket_capacity, basket_index).
        It uses binary search (via `bisect_left`) to quickly locate the leftmost basket with sufficient capacity.
        A helper function, `fill_ordered`, is used to update the ordered list with new available baskets from a given range.
        
        The main steps are:
          1. **Initialize an ordered list (`ordered`):**
             - Start with a dummy tuple (0, 0) so that subsequent baskets are compared against 0.
             - Call `fill_ordered` to populate `ordered` with baskets from the entire range [0, n).
          2. **Iterate over each fruit:**
             - For each fruit, use `bisect_left` to find the first basket (in `ordered`) that has capacity ≥ the fruit's quantity.
             - If no such basket exists (i.e. binary search returns an index equal to the length of `ordered`), the fruit remains unplaced.
             - Otherwise, determine a subrange of baskets that may now become available after using the chosen basket.
             - Call `fill_ordered` on this subrange to update the ordered list, effectively removing the used basket.
             - Decrement the count of unplaced fruits (initially set to n, the total number of fruits) for every fruit placed.
          3. **Return the count of unplaced fruits.**
        
        ### Detailed Explanation of Key Components:

        #### A. The `fill_ordered` Function:
        - **Purpose:**  
          To scan the baskets in a specified range [start, end) and append those baskets to an array `arr`
          if the basket's capacity is at least as large as the last element in `arr` (ensuring a non-decreasing order of capacities).
        - **Mechanism:**  
          For each index `i` from `start` to `end - 1`:
            - If `baskets[i] >= arr[-1][0]` (i.e. the basket's capacity is greater than or equal to the capacity of 
              the last basket in `arr`), append the tuple `(baskets[i], i)` to `arr`.
            - Immediately mark `baskets[i]` as used by setting it to 0, so it will not be considered in future calls.
        - **Data Flow Example:**  
          Suppose `arr` is `[(0, 0)]` (after initialization) and the baskets array is `[3, 5, 4, 8, 9]`.  
          - For `i=0`: `baskets[0]` is 3. Since 3 ≥ 0, append `(3, 0)` to `arr` → `arr` becomes `[(0, 0), (3, 0)]`, and set `baskets[0]=0`.
          - For `i=1`: Now `baskets[1]` is 5. Compare 5 with `arr[-1][0]` which is 3; since 5 ≥ 3, append `(5, 1)` → `arr` becomes `[(0, 0), (3, 0), (5, 1)]`, and set `baskets[1]=0`.
          - For `i=2`: `baskets[2]` is 4. Now, 4 is NOT ≥ 5 (the last element's capacity), so it is skipped.
          - And so on...
        - **Time Complexity:**  
          This function scans a segment of the baskets array once, so it runs in O(k) time where k is the number of elements in that segment.

        #### B. Using `bisect_left`:
        - **Purpose:**  
          To efficiently find the leftmost basket in `ordered` whose capacity is at least as large as the current fruit's quantity.
        - **Mechanism:**  
          `bisect_left(ordered, (f, 0))` treats the tuples in `ordered` in lexicographical order.
          Since the first element of each tuple is the basket's capacity, this call returns the index of the first tuple 
          where the capacity is ≥ `f` (the fruit's quantity).
        - **Data Flow Example:**  
          With an ordered list `[(0, 0), (3, 0), (5, 1)]` and fruit `f = 4`:
          - `bisect_left(ordered, (4, 0))` returns index 2 (since `(5, 1)` is the first tuple with capacity 5, which is ≥ 4).

        #### C. Updating `ordered` After Placement:
        - After a basket is used to place a fruit, we determine a new range [start, end) of baskets in the original array that might now be available.
        - A new temporary list, `new`, is initialized with the basket immediately preceding the chosen one (i.e. `ordered[i-1]`).
        - The function `fill_ordered` is called on this subrange to append new baskets that satisfy the capacity condition.
        - Then, the section `ordered[i : i + 1]` (which represents the used basket) is replaced with `new[1:]` (the newly found baskets).
        - This dynamic update ensures that `ordered` always maintains a correct, monotonic list of available baskets.

        #### D. Overall Time Complexity Analysis:
        - The initial call to `fill_ordered` scans all baskets once: O(n).
        - For each fruit, a binary search is performed on the `ordered` list: O(log n) per fruit.
        - The dynamic updates via `fill_ordered` in the worst case can scan a portion of the baskets array multiple times, but each basket is marked as used once.
        - Overall, the worst-case time complexity is approximately O(n log n) (assuming that each basket is processed only once due to marking).

        ### Detailed Step-by-Step Examples:

        #### Example 1:
        Input: 
            fruits  = [4, 2, 5, 7, 6]
            baskets = [3, 5, 4, 8, 9]
        
        **Step 1: Initialization & First `fill_ordered` Call**
            - `ordered` starts as [(0, 0)].
            - Call fill_ordered(ordered, 0, 5):
              * i=0: baskets[0]=3 (3 ≥ 0) → append (3,0), set baskets[0]=0. ordered becomes [(0,0), (3,0)].
              * i=1: baskets[1]=5 (5 ≥ 3) → append (5,1), set baskets[1]=0. ordered becomes [(0,0), (3,0), (5,1)].
              * i=2: baskets[2]=4 (4 < 5) → skipped.
              * i=3: baskets[3]=8 (8 ≥ 5) → append (8,3), set baskets[3]=0. ordered becomes [(0,0), (3,0), (5,1), (8,3)].
              * i=4: baskets[4]=9 (9 ≥ 8) → append (9,4), set baskets[4]=0. ordered becomes [(0,0), (3,0), (5,1), (8,3), (9,4)].
        
        **Step 2: Processing Each Fruit**
            - res is initialized to 5 (number of fruits).
            
            For fruit 4:
              - bisect_left(ordered, (4,0)) finds index 2 because (5,1) is the first tuple with capacity ≥ 4.
              - Determine start = ordered[2][1] + 1 = 1 + 1 = 2.
              - Determine end: since index 2 is not the last element, end = ordered[3][1] = 3.
              - Initialize new = [ordered[1]] (which is (3,0)).
              - Call fill_ordered(new, 2, 3):
                  * i=2: baskets[2]=4 (4 ≥ 3) → append (4,2), set baskets[2]=0.
                  * new becomes [(3,0), (4,2)].
              - Replace ordered[2:3] with new[1:] → ordered becomes [(0,0), (3,0), (4,2), (8,3), (9,4)].
              - Decrement res to 4.
            
            Similar detailed steps occur for each subsequent fruit, dynamically updating `ordered` using the new ranges.

        #### Example 2:
        Input:
            fruits  = [5, 6, 2, 9, 3]
            baskets = [4, 7, 3, 10, 5]
        
        **Initial fill_ordered:**
            - ordered starts as [(0, 0)].
            - Process baskets in order:
              * i=0: baskets[0]=4 → (4,0) appended, baskets[0]=0.
              * i=1: baskets[1]=7 → (7,1) appended, baskets[1]=0.
              * i=2: baskets[2]=3 (3 < 7) → skipped.
              * i=3: baskets[3]=10 → (10,3) appended, baskets[3]=0.
              * i=4: baskets[4]=5 (5 < 10) → skipped.
            - ordered becomes [(0,0), (4,0), (7,1), (10,3)].
        
        **Processing Fruits with bisect_left:**
            - For fruit 5:
              * bisect_left returns index 2 (since (7,1) is the first with capacity ≥ 5).
              * Update range and call fill_ordered accordingly.
            - Detailed updates continue for each fruit, ensuring that the correct baskets are removed and new ones inserted.
        
        #### Example 3:
        Input:
            fruits  = [3, 8, 5, 10, 6]
            baskets = [5, 9, 4, 11, 7]
        
        **Initial fill_ordered:**
            - ordered begins as [(0, 0)].
            - Process baskets:
              * i=0: 5 → append (5,0).
              * i=1: 9 (9 ≥ 5) → append (9,1).
              * i=2: 4 (4 < 9) → skipped.
              * i=3: 11 (11 ≥ 9) → append (11,3).
              * i=4: 7 (7 < 11) → skipped.
            - ordered becomes [(0,0), (5,0), (9,1), (11,3)].
        
        **Processing Fruits:**
            - For fruit 3:
              * bisect_left returns index 1 (first basket with capacity ≥ 3 is (5,0)).
              * Update new ranges and call fill_ordered.
            - The algorithm continues similarly for the remaining fruits, updating the ordered list dynamically.
        
        #### Example 4:
        Input:
            fruits  = [6, 2, 7, 4, 5]
            baskets = [3, 8, 5, 10, 6]
        
        **Initial fill_ordered:**
            - ordered starts as [(0,0)].
            - Process baskets:
              * i=0: 3 → append (3,0).
              * i=1: 8 (8 ≥ 3) → append (8,1).
              * i=2: 5 (5 < 8) → skipped.
              * i=3: 10 (10 ≥ 8) → append (10,3).
              * i=4: 6 (6 < 10) → skipped.
            - ordered becomes [(0,0), (3,0), (8,1), (10,3)].
        
        **Processing Fruits:**
            - For fruit 6:
              * bisect_left returns index 2 (first basket with capacity ≥ 6 is (8,1)).
              * The algorithm then updates the ordered list by scanning the range following basket index 1.
            - Subsequent fruits are processed similarly, with dynamic updates to `ordered` using the `fill_ordered` function.
        
        ### Summary of the Process:
        - **Initialization:**  
          Build a monotonic (non-decreasing) list `ordered` of available baskets using `fill_ordered`.  
        - **For Each Fruit:**  
          Use binary search to quickly find the leftmost basket that can accommodate the fruit.  
          Update the range of available baskets by invoking `fill_ordered` on a subrange, thereby removing the used basket.
        - **Result Calculation:**  
          Decrement the result counter for every successful fruit placement, and return the final count of unplaced fruits.
        
        ### Time Complexity:
        - **Initial fill_ordered:** O(n) (each basket is processed once)
        - **Each Fruit Processing:**
            - Binary search via `bisect_left`: O(log n)
            - Updating available baskets via `fill_ordered`: O(k) for the segment, but each basket is marked used once.
        - **Overall Complexity:** Approximately O(n log n) in the worst case.
        
        This detailed explanation covers every step of the algorithm, how the helper function `fill_ordered` works with concrete data examples, and how binary search (via bisect_left) is used to maintain and update the list of available baskets.
        """
        n = len(fruits)

        ordered = [(0, 0)]

        def fill_ordered(arr, start, end):
            # Iterate over baskets from index 'start' to 'end' (non-inclusive)
            for i in range(start, end):
                # Check if the current basket's capacity is greater than or equal to the last element in arr.
                # This ensures we only add baskets that maintain a non-decreasing order in capacity.
                if baskets[i] >= arr[-1][0]:
                    arr.append((baskets[i], i))
                    baskets[i] = 0  # Mark the basket as used so it won't be considered again

        # Initially, fill the 'ordered' list with baskets from the entire range [0, n)
        fill_ordered(ordered, 0, n)

        res = n  # Start with the assumption that none of the fruits have been placed
        for f in fruits:
            # Use binary search to find the leftmost basket in 'ordered' with capacity >= fruit f
            i = bisect_left(ordered, (f, 0))

            if i == len(ordered):  # If no valid basket is found, move on (fruit remains unplaced)
                continue

            # Determine the subrange in baskets that might now have new available baskets
            start = ordered[i][1] + 1
            if i == len(ordered) - 1:  # If the chosen basket is the last in 'ordered'
                end = n
            else:
                end = ordered[i + 1][1]

            new = [ordered[i - 1]]
            # Update 'new' with available baskets in the range [start, end)
            fill_ordered(new, start, end)

            # Replace the used basket in 'ordered' with the newly found baskets in this segment
            ordered[i: i + 1] = new[1:]

            res -= 1  # Decrement the count as this fruit was successfully placed

        return res
