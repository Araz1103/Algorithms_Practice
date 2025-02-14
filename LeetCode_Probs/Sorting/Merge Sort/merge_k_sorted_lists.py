"""
Merge K Sorted Linked Lists
You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.

Example 1:

Input: lists = [[1,2,4],[1,3,5],[3,6]]

Output: [1,1,2,3,3,4,5,6]
Example 2:

Input: lists = []

Output: []
Example 3:

Input: lists = [[]]

Output: []
Constraints:

0 <= lists.length <= 1000
0 <= lists[i].length <= 100
-1000 <= lists[i][j] <= 1000
"""

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergesorted(self, list1, list2):
        # Can merge in place
        # Basically point starting from a dummy node
        # Return from one post dummy node
        # Starting node
        start_node = ListNode()
        starting_node = start_node
        list1_pointer = list1
        list2_pointer = list2

        while list1_pointer!=None and list2_pointer!=None:
            # Check which one is lower, starting node to be added to that
            if list1_pointer.val <= list2_pointer.val:
                starting_node.next = list1_pointer
                list1_pointer = list1_pointer.next

            else:
                starting_node.next = list2_pointer
                list2_pointer = list2_pointer.next

            starting_node = starting_node.next
            starting_node.next = None #Cut away ties of that node

        # Now whichever is left, starting node points to that
        if list1_pointer is None:
            starting_node.next = list2_pointer
        else:
            starting_node.next = list1_pointer

        return start_node.next #This is the head of the newly sorted list
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Using Merge Sort Approach
        # Divide and Conquer
        # Merge the two
        # Smallest unit is a list here
        # Combine to return a list too
        len_list = len(lists)
        if not len_list:
            return None

        start_index = 0
        end_index = len_list - 1
        if start_index >= end_index:
            return lists[start_index]

        mid_point = int((start_index + end_index)/2)

        sorted_list1_head = self.mergeKLists(lists[start_index:mid_point+1])
        sorted_list2_head = self.mergeKLists(lists[mid_point+1:])
        sorted_list_head = self.mergesorted(sorted_list1_head, sorted_list2_head)
        return sorted_list_head
        