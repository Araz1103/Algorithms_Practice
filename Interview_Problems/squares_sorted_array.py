"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    sorted_squares = []

    start_pointer = 0
    end_pointer = len(nums)-1

    # Basically since it is sorted, and can have negatives
    # Let's compare the squares for each start and end pointer
    # Whichever is larger, let's add that and shift pointer
    # If all positive, end pointer will keep decrimenting
    # Do until start_pointer <= end_pointer

    while start_pointer <= end_pointer:
        start_square = nums[start_pointer]**2
        end_square = nums[end_pointer]**2

        if start_square >= end_square:
            sorted_squares.append(start_square)
            start_pointer +=1
        else:
            sorted_squares.append(end_square)
            end_pointer -=1

    return sorted_squares[::-1]

print(sortedSquares([]))
print(sortedSquares([-1, 0, 2, 5]))
print(sortedSquares([-5, 1, 4, 5]))
print(sortedSquares([-6, -3, 2, 4, 5]))
print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))