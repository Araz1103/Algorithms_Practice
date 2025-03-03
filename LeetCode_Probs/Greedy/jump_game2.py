"""
You are given a 0-indexed array of integers nums of length n. 
You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach nums[n - 1].

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, 
then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 
Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

# Intuition
# Start @end
# See what is the maximum (furthest) position we can reach from there to end
# Once we find that (we are bound to find something)
# We set that as our new goal, and then keep trying until we reach start node
# We will never have the case when we are furthest, and we can't reach that from previous node but we can reach something less further
# Example: 1, 1, 2, 3, 0, 1, 2
# From 2, we know furthest is 3
# Now there can be no case where we can't reach 3 but reach 1 before the 2
# So guaranteed to find min number of jumps

def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    goal_index = len(nums) - 1
    num_jumps = 0
    while goal_index!=0:
        # Search from all indexes possible from 0 till 1 less than the goal index
        # We can assign the first one we find, since that is the furthest
        for i in range(goal_index):
            if nums[i] >= (goal_index - i): #Can jump till the goal index from here
                goal_index = i #New goal
                num_jumps+=1
                break #No need to check more, as this is the furthest

    # while loop guaranteed to exit!
    # If only 1 element in nums, then num jumps is 0, which is technically correct
    return num_jumps

        