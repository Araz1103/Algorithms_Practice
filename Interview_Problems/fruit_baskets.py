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
import bisect
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        """
        Determines the number of unplaced fruits given their sizes and available baskets.

        The goal is to place as many fruits as possible into baskets while following these rules:
        - A fruit can only be placed in a basket if the basket's capacity is **greater than or equal to** the fruit's size.
        - Each basket can hold at most **one** fruit.
        - Baskets are used in sorted order (smallest available basket first).
        
        ### Approach:
        - **Step 1:** Create an ordered list (`ordered`) of available baskets sorted by their capacity.
        - **Step 2:** Iterate through each fruit, trying to find the smallest available basket that can hold it.
        - **Step 3:** If a valid basket is found, remove it from the list (mark it as used).
        - **Step 4:** If no valid basket is found for a fruit, the fruit remains unplaced.
        
        ### Binary Search Optimization:
        - Instead of searching through all baskets linearly, we use **binary search (`bisect_left`)** to efficiently find the first basket that can hold a given fruit in **O(log n)** time.

        ### Parameters:
        - `fruits` (List[int]): A list of integers representing the sizes of fruits to be placed.
        - `baskets` (List[int]): A list of integers representing the capacities of available baskets.

        ### Returns:
        - `int`: The number of fruits that could not be placed into baskets.

        ### Complexity:
        - Sorting baskets initially: **O(n log n)**
        - Searching for baskets using binary search per fruit: **O(m log n)**
        - Overall time complexity: **O((n + m) log n)** where `n` is the number of baskets and `m` is the number of fruits.

        ### Example:
        ```python
        fruits = [2, 3, 5]
        baskets = [1, 4, 3, 6]
        sol = Solution()
        print(sol.numOfUnplacedFruits(fruits, baskets))  # Output: 1
        ```
        **Explanation:**
        - Fruit `2` is placed in basket `3`
        - Fruit `3` is placed in basket `4`
        - Fruit `5` is placed in basket `6`
        - **1 fruit remains unplaced.**
        """
        n = len(fruits)

        ordered = [(0, 0)]  # Start with a dummy basket (0, 0)

        # Function to update `ordered` with valid baskets
        def fill_ordered(arr, start, end):
            for i in range(start, end):
                if baskets[i] >= arr[-1][0]:  # Ensure increasing order
                    arr.append((baskets[i], i))
                    baskets[i] = 0  # Mark as used

        fill_ordered(ordered, 0, n)

        res = n  # Assume all fruits are unplaced initially

        for f in fruits:
            # Find the first valid basket using binary search
            i = bisect.bisect_left(ordered, (f, 0))

            if i == len(ordered):  # No available basket
                continue

            # Determine range to re-evaluate baskets
            start = ordered[i][1] + 1  # Next index
            if i == len(ordered) - 1:  # Last basket case
                end = n
            else:
                end = ordered[i + 1][1]

            # Create a new ordered list excluding used baskets
            new = [ordered[i - 1]]
            fill_ordered(new, start, end)

            # Update `ordered`
            ordered[i: i + 1] = new[1:]

            res -= 1  # Fruit placed

        return res
