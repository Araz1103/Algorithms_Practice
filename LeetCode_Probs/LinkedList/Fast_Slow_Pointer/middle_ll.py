# To get the middle of the Linked List
# Can start 2 pointers @start
# Fast Pointer: Moves 2 steps
# Slow Pointer: Moves 1 step

# When FP @end, SP @half, which is middle

def get_middle_ll(head):
    slow_pointer = head
    fast_pointer = head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return slow_pointer # Will have reached the middle

# Middle only works on a LL without any cycles