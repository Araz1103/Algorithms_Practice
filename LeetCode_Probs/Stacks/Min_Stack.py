"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

# My approach
# Basically maintain an array of the minimums
# With push, add to it if there is a new minimum
# With pop, remove from it if the latest minimum is the one popped
# Since pop can only happen from the last inserted, the ones left will always be the last minimums
# If we maintain a counter, then we can check for those conditions
# And minimum can be returned in O(1) if we access the last minimum of this reference array
# Rest be careful about accessing lists, to handle empty list conditions

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.counter = 0
        self.current_minimum = None
        self.minimum_reference_index = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        print("-------- PUSH---------")
        print("Going for Push, Stack is", self.stack)
        if self.stack: #If not empty
            if val <= self.current_minimum:
                min_index = self.counter
                self.minimum_reference_index.append(min_index) 
                self.current_minimum = val
        else: #If Stack Empty
            self.current_minimum = val
            min_index = self.counter
            self.minimum_reference_index.append(min_index) 
        
        self.stack.append(val)
        self.counter += 1
        print("Push Done, Stack is", self.stack)
        print(f"Min is: {self.current_minimum}")
        print(f"Min Array is: {self.minimum_reference_index}")
        print(f"Counter is: {self.counter}")
        print("---------------------")
        print("-------- PUSH DONE ---------")
        
        

    def pop(self):
        """
        :rtype: None
        """
        print("-------- POP ---------")
        print(f"Min is: {self.current_minimum}")
        print(f"Min Array is: {self.minimum_reference_index}")
        print(f"Counter is: {self.counter}")
        print("Going for Pop, Stack is", self.stack)
        # Check if the counter at which popped had a current minimum
        if self.minimum_reference_index[-1] == (self.counter - 1):
            # Pop from min ref index as well
            self.minimum_reference_index.pop(-1)
            # New current minimum is the last entry from this
            if self.minimum_reference_index: 
                self.current_minimum = self.stack[self.minimum_reference_index[-1]]
            else:#If it becomes empty, then current minimum is None
                self.current_minimum = None

        self.stack.pop(-1)
        self.counter -= 1
        print(f"Min is: {self.current_minimum}")
        print(f"Min Array is: {self.minimum_reference_index}")
        print("Pop Done, Stack is", self.stack)
        print(f"Counter is: {self.counter}")
        print("-------- POP DONE ---------")
        

    def top(self):
        """
        :rtype: int
        """
        print("Fetching Top, Stack is", self.stack)
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        print("Fetching Min, Stack is", self.stack)
        return self.current_minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# min_is = obj.getMin()
# print(min_is)
# obj.pop()
# top_is = obj.top()
# print(top_is)
# min_is = obj.getMin()
# print(min_is)

obj = MinStack()
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483647)
top_is = obj.top()
print(top_is)
obj.pop()
min_is = obj.getMin()
print(min_is)
obj.pop()
min_is = obj.getMin()
print(min_is)
obj.pop()
obj.push(2147483647)
top_is = obj.top()
print(top_is)
min_is = obj.getMin()
print(min_is)
obj.push(-2147483648)
top_is = obj.top()
print(top_is)
min_is = obj.getMin()
print(min_is)
obj.pop()
min_is = obj.getMin()
print(min_is)