"""
Jump Game
You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

Return true if you can reach the last index starting from index 0, or false otherwise.

Example 1:

Input: nums = [1,2,0,1,0]

Output: true
Explanation: First jump from index 0 to 1, then from index 1 to 3, and lastly from index 3 to 4.

Example 2:

Input: nums = [1,2,1,0,1]

Output: false
Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""
from typing import List

def canJump(nums: List[int]) -> bool:

    if len(nums)==1:
        return True #Obvious
    
    print(nums)

    # Let's start @end
    goal_index = len(nums)-1

    # We want to keep checking if we can reach the goal from some node
    # Once we get to that node, keep checking if you can get to that
    # Basically we keep checking until we reach start node (so we know we can reach to end from start)
    # Or we see that node cannot be reached by any other previous node 
    for i in range(len(nums)-1, -1, -1):
        print(f"At index: {i}, element: {nums[i]}")
        print(f"Goal Index is: {goal_index}, element is: {nums[goal_index]}")
        print(f"i - goal index distance: {goal_index - i}")
        print(f"Condition is: {nums[i] >= (goal_index - i)}")
        if nums[i] >= (goal_index - i): #this means that can reach
            # We shift the goal to this position
            goal_index = i
            print(f"New Goal Index is: {goal_index}, element: {nums[goal_index]}")

    # Basically if we were able to reach from start to end
    # The goal index should be at 0 now
    # If it is, we can return True else False
    return goal_index==0

print(canJump([1, 2, 2, 0, 1]))

nums=[1,2,1,0,1]
print(canJump(nums))
            
        