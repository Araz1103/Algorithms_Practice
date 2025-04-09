from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Detects if a cycle exists in a linked list and returns the starting node of the cycle.
        If no cycle is present, returns None.

        Uses Floyd’s Tortoise and Hare algorithm:
        Step 1: Detect cycle using slow and fast pointers.
        Step 2: Once they meet, use a new pointer from head and move both one step at a time
                until they meet again — this meeting point is the start of the cycle.
        """
        slow = fast = head

        # Step 1: Cycle Detection
        while fast and fast.next:
            slow = slow.next          # Move slow by 1
            fast = fast.next.next     # Move fast by 2

            if slow == fast:
                # ✅ Cycle detected
                break
        else:
            # ❌ No cycle detected
            return None

        # Step 2: Find the start of the cycle
        entry = head

        # At this point:
        # Let’s say the distance from head to start of cycle = x
        # Distance from start of cycle to meeting point = y
        # Remaining distance to complete cycle = z
        # Then:
        # Slow traveled x + y
        # Fast traveled x + y + n*(y + z) (n ≥ 1)

        # Since fast moves twice as fast:
        # 2(x + y) = x + y + n(y + z)
        # => x = n(y + z) - y
        # => x = (n-1)(y + z) + z
        # This means if one pointer starts from head (x away),
        # and another starts from meeting point (z away from cycle start),
        # they’ll meet at the cycle start!

        while entry != slow:
            entry = entry.next  # Move from head
            slow = slow.next    # Move from meeting point

        return entry  # Start of the cycle
