"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if n > len(flowerbed):
        return False

    num_flowers = 0
    if len(flowerbed)==1:
        if flowerbed[0]==0:
            num_flowers+=1

        return num_flowers >= n #Can n flowers be planted or not

    
    for i in range(len(flowerbed)):
        
        # For last position check if empty and before is 1 or not
        if i==len(flowerbed)-1:
            if flowerbed[i]==0 and flowerbed[i-1]!=1:
                num_flowers+=1
                flowerbed[i]=1
        # For first position just check if empty and next is 1 or not
        elif i==0:
            if flowerbed[i]==0 and flowerbed[i+1]!=1:
                num_flowers+=1
                flowerbed[i]=1
        # For all others
        # 1. Check spot is empty (0)
        # 2. Check that before is 1 or after is 1
        else:
            if flowerbed[i]==0 and flowerbed[i-1]!=1 and flowerbed[i+1]!=1:
                num_flowers+=1
                flowerbed[i]=1
    print(num_flowers, flowerbed)
    return num_flowers >= n #Can n flowers be planted or not

# Slightly more organized :P GPT
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            # Stop early if we have already planted enough flowers
            if count >= n:
                return True
            
            # Check if current spot is empty and both neighbors (if exist) are empty
            if flowerbed[i] == 0:
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)  # Either first plot or left neighbor is empty
                next_empty = (i == length - 1 or flowerbed[i + 1] == 0)  # Either last plot or right neighbor is empty
                
                if prev_empty and next_empty:
                    # Plant flower
                    flowerbed[i] = 1
                    count += 1
        
        return count >= n
