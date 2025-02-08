from typing import Optional

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]
Example 3:

Input: list1 = [], list2 = []

Output: []
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach
        # Similar to merge function in merge sort
        # 1. Out of the 2 lists, at their current nodes, whichever is smaller, that is first
        # 2. Then you go one node ahead in the smaller one
        # 3. You again compare with this and the other one, and whichever is smaller one, previous points to that
        # 4. Keep repeating until 1 list reaches end, then directly add that to the remaining node of the other

        # Make a Dummy List Node and then keep adding to it
        # @end return dummy.next
        # Also tail pointer so you can keep on going
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            list1_current_val = list1.val
            list2_current_val = list2.val

            if list1_current_val <= list2_current_val:
                tail.next = list1
                list1 = list1.next #Basically iterate through that list itself, so no other pointers
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next # Update tail, as you have inserted @end

            
            
        if list1: # If list1 still exists
            tail.next = list1 #Add list1 to the end
        elif list2:
            tail.next = list2 #Add list2 to the end
        
        # Both can never be null, as one would always reach null first
        return dummy.next # This is the beginning of the sorted list

        