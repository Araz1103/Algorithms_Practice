"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Slow @beginning and Fast @next
        # Start a slow and fast pointer and traverse FP till @end
        # Now Slow is at middle left element
        # Till then we are keeping a stack and adding elements to it
        # Now we can keep adding to top of stack element, pop it, check with curr max

        slow_pointer = head
        fast_pointer = head.next
        
        stack = [slow_pointer.val]
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            stack.append(slow_pointer.val)
            fast_pointer = fast_pointer.next.next
        
        # Now slow pointer @middle left
        # Now keep incrementing slow until it reaches @end, and add and pop from stack
        curr_max = 0
        #print(stack)
        while slow_pointer.next:
            #print(stack)
            slow_pointer = slow_pointer.next
            top_element = stack.pop()
            #print(top_element, slow_pointer.val)
            twin_sum = top_element + slow_pointer.val
            curr_max = max(curr_max, twin_sum)

        return curr_max

# We can also do 1 pass and store all values in an array
# And then on that array, use one pointer @start and @end
        