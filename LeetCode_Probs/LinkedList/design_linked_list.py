"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""
class LinkedListNode():
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.previous = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        # If index is negative, return -1
        # If LL is empty, return -1
        if index < 0 or (not self.head):
            return -1
        
        # Now basically iterate until reach the index
        # If during iteration, exceeds tail, return -1

        current_node = self.head

        while index > 0 and current_node != self.tail: # The minute index reaches 0 or we reach tail
            current_node = current_node.next
            index -=1

        # If we broke out, we're at the current node required
        if index !=0: #This means that an invalid index was returned
            return -1
        else: #Index reached 0, therefore we are at the required node
            return current_node.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        # If LL is currently empty, handle
        if not self.head:
            new_node = LinkedListNode(val)
            self.head = new_node
            self.tail = new_node
            return None
        
        # To add @head, get current head
        # Make a node with value
        # Point this node at the current head
        # Set next and previous accordingly
        # Make this the new head
        new_node = LinkedListNode(val)
        new_node.next = self.head
        # Previous points to None only @starting
        self.head.previous = new_node
        self.head = new_node
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        # If LL is currently empty, handle
        if not self.head:
            new_node = LinkedListNode(val)
            self.head = new_node
            self.tail = new_node
            return None
            
        # To add at the tail, create a new node
        # Fetch the current tail
        # Point the tail's next to this new node
        # Point the new node's previous to the tail
        # Now assign the tail to this new node
        new_node = LinkedListNode(val)
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # If index is negative, return -1
        if index < 0:
            return None
        
        # If LL is currently empty, handle
        if not self.head:
            if index in [0,1]: #If we want to handle adding @0 and 1 both
                new_node = LinkedListNode(val)
                self.head = new_node
                self.tail = new_node
                return None
            else:
                return None # Cannot add for any other indexes
        
        #print("IN Appending @Index")
        # Now basically iterate until reach the index
        # If during iteration, exceeds tail, return None (no addition)
        # Once at required place, we add a new node

        current_node = self.head

        while index > 0 and current_node != self.tail: # The minute index reaches 0 or we reach tail
            current_node = current_node.next
            index -=1

        #print("Broke out!", index)
        # If we broke out, we're at the current node required
        if index !=0:
            # If index is 1, therefore it is appending @end
            if index == 1:
                new_node = LinkedListNode(val)
                current_node.next = new_node
                new_node.previous = current_node
                self.tail = new_node
            else:
                # If > 1, then not valid
                return None
        else: #Index reached 0, therefore we are at the required node
            #print("Adding now!")
            new_node = LinkedListNode(val)
            if current_node == self.head:
                new_node.next = current_node
                current_node.previous = new_node
                #print("Current Node is head, so reassigning head!")
                # Since current node was head, make this the new head
                # As we have added before head
                self.head = new_node

            else:
                previous_node = current_node.previous
                previous_node.next = new_node
                new_node.next = current_node
                new_node.previous = previous_node
                current_node.previous = new_node
            
            #print("Added!")
            
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        # If index is negative, return None
        # Or LL is Empty
        if index < 0 or (not self.head):
            return None
        
        # Now basically iterate until reach the index
        # If during iteration, exceeds tail, return None (no deletion)
        # Once at required place, we delete the node

        current_node = self.head

        while index > 0 and current_node != self.tail: # The minute index reaches 0 or we reach tail
            current_node = current_node.next
            index -=1

        # If we broke out, we're at the current node required to remove
        if index !=0: #This means that an invalid index was returned
            return None
        else: #Index reached 0, therefore we are at the required node
            # Delete this node
            if current_node == self.head:
                next_node = current_node.next
                if next_node:
                    # If next node exists, remove previous of it
                    # Pointing to the current node
                    next_node.previous = None
                else: #If no next node, this means there was only 1 node @LL
                    self.tail = None # No tail as well now
                self.head = next_node #New Head
                current_node.next = None

            elif current_node == self.tail:
                previous_node = current_node.previous
                if previous_node:
                    # If previous node exists
                    # Remove it's next
                    previous_node.next = None
                else: #If no previous node, means there was only 1 node @LL
                    self.head = None
                
                self.tail = previous_node
                current_node.previous = None

            else:
                # If it is neither head nor tail
                # Is a node @middle
                # Remove it directly
                previous_node = current_node.previous
                next_node = current_node.next
                previous_node.next = next_node
                next_node.previous = previous_node
                current_node.next = None
                current_node.previous = None

    def print_ll(self):
        if not self.head:
            # Empty LL
            print("Empty LL")
            return

        current_node = self.head
        print("Begin!")

        while current_node!=self.tail:
            print(f"-> {current_node.val} ->")
            current_node = current_node.next

        print(f"-> {current_node.val} -> END")

        
    
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# obj = MyLinkedList()
# #obj.print_ll()
# obj.addAtHead(5)
# #obj.print_ll()
# obj.addAtTail(6)
# obj.addAtHead(15)
# #obj.print_ll()
# obj.addAtIndex(0,7)
# obj.addAtIndex(2,17)
# obj.print_ll()
# print(obj.get(1))
# print(obj.get(2))
# obj.deleteAtIndex(2)
# obj.print_ll()

obj = MyLinkedList()
# #obj.print_ll()
# obj.addAtHead(5)
# #obj.print_ll()
# obj.addAtTail(6)
# obj.addAtHead(15)
# #obj.print_ll()
obj.addAtIndex(1,0)
# obj.addAtIndex(2,17)
# obj.print_ll()
print(obj.get(0))
# print(obj.get(2))
# obj.deleteAtIndex(2)
obj.print_ll()