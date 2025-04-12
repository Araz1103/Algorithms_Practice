# Detect a cycle in a LL
# Start a Slow and Fast Pointer @LL Start
# If the LL has a cycle, they will meet
# Otherwise the FP will reach @end

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_cycle_ll(head):
    slow_pointer = head
    fast_pointer = head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        # if slow and fast pointer met, cycle
        if slow_pointer==fast_pointer:
            return True
        
    return False # If inner condition not satisfied, must exit 

# Now we want to return the head of the cycle in LL, if it exists
# We also want the cycle length

def detect_ll_cycle_head(head):
    slow_pointer = head
    fast_pointer = head
    cycle_exists = False #default value false
    distance_p_x = 0

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        distance_p_x +=1

        # If slow and fast pointer meet, cycle exists
        if slow_pointer==fast_pointer:
            # we break to find out the cycle head
            cycle_exists = True
            break

    if not cycle_exists:
        return None #No cycle, so no head of cycle
    else:
        # Let's assume length till the intersection point, from cycle head = X
        # Length from intersection point till cycle head: C - X where C is length of cycle
        # Assuming P distance till cycle head from start of LL
        # We know slow pointer travels half of fast pointer
        # Distance Travelled by Fast Pointer till now:
        # P (to reach cycle start) + C (needs to complete C, and reach Cycle Head before it can catch up with slow pointer) + X (distance from Cycle Head till intersection)
        # Distance Travelled till Slow Pointer till now:
        # P (to reach cycle start) + X (distance from Cycle head till intersection)
        # We know 2* Slow Pointer Distance = Fast Pointer Distance
        # Therefore:
        # 2*(P + X) = P + C + X
        # 2P + 2X = P + C + X
        # P = C - X
        # Therefore to find distance till head of Cycle, we need to traverse till head of the cycle
        # So currently our slow and fast are together, if we start moving slow again +1
        # and start a new pointer @start of LL, and move it +1
        # They both will travel P = C - X and meet each other, @cycle head
        new_start_pointer = head
        while new_start_pointer!=slow_pointer:
            new_start_pointer = new_start_pointer.next
            slow_pointer = slow_pointer.next
        
        # Now they're both at head of Cycle
        # For Cycle Length
        # We know P = C - X
        # C = P + X
        # We tracked it above with p_x
        return slow_pointer #or the new start pointer
