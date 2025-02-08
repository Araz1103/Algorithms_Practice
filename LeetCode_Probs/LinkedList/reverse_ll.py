from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def show_node(self):
        print(f"Node is: {self.val}")
        print(f"Next is: {self.next}")
        if self.next is not None:
            print(f"Next val is: {self.next.val}")

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertend(self, val):
        if self.head is None:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            insert_node = ListNode(val)
            self.tail.next = insert_node
            self.tail = insert_node

    def print_list(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

    def reverseList(self) -> Optional[ListNode]:
        # Basically
        # Reach till the end
        # Make that the head
        # While going till end, point the pointers to previous nodes
        current_node = self.head
        previous_node = None
        if current_node is not None:
            while current_node.next is not None:
                current_node.show_node()
                # Find the next node
                next_node = current_node.next
                
                # Now point current node, to previous node
                current_node.next = previous_node
                current_node.show_node()
                
                # Make the current node as previous node
                previous_node = current_node

                # Now make the next node as current node
                current_node = next_node

            # Now make the last current node point to the previous node
            current_node.next = previous_node
            
        
        # When we break out from here
        # We reach @end of the list
        # Now this is the new head
        new_head = current_node
        print("New Head!")
        new_head.show_node()
        self.head = new_head

        return new_head

example_ll = LinkedList()
example_ll.insertend(1)
example_ll.insertend(2)
example_ll.insertend(3)
example_ll.insertend(4)
example_ll.insertend(5)
example_ll.print_list()
example_ll.reverseList()
example_ll.print_list()

        