"""
Edit and compare long strings
Design and implement a data structure that handles edit operations on long strings and comparisons between them.
Formally, the DS manages a string S of length N, where N is very large (say, 10^9 characters). 
At initialization, the string is a repetition of N copies of the 0 ASCII character.

The DS has to handle an operation edit(i, c), which means that the i-th character of S is replaced with character c. 
Moreover, you have to implement a comparison function/operator, 
which takes two of these data structures and returns whether the corresponding strings are equal or not.

Assumptions:
- N -> size of string can be large say 10^9 characters
- we expect a small number of edit operations and comparisons (total number of operations = M)

Test Case:  
Initial State:
S1 = 000, S2 = 000
Operations:
S1.Edit(1, a)
S2.Edit(1, a)
Compare(S1, S2); → true
S1.Edit(2, b)
Compare(S1, S2); → false
S1.Edit(2, c)
S2.Edit(2, c)
Compare(S1, S2); → true
"""

class string_datastructure:

    def __init__(self, N=100):
        self.length = N
        self.edits = {} #Keep track of edits
        # Do not need to store the string itself, as too large for array
        # See hints from 10^9 and large
        # Default string is all 0s
        # So we track edits

    def edit_string(self, i, c):
        # Edits the string
        # Updates at ith index to c character
        
        # If character is '0', we know it technically reverts the string ith index back to 0
        # So we remove from edit dict
        if c=='0':
            self.edits.pop(i, None) #If no edits yet, handling pop to not raise an error
        else:
            # We can edit the string
            # Add to the edit dict
            self.edits[i] = c

        # We see edits are done in O(1)

def compare_strings(s1, s2):
    # Takes 2 string data structure objects and compares them
    
    if s1.length!=s2.length: #O(1)
        return False
    
    # Now if both of these have edits at different places, we know cannot be equal
    # So can check if keys of both edit dicts are same or not
    # if s1.edits.keys()!=s2.edits.keys():
    #     return False
    
    # Now we can check if all edits equal or not
    # Dict operation is O(len of dict)
    # In our case for M edits, worst case will be O(M)
    return s1.edits==s2.edits

s1 = string_datastructure(100)
s2 = string_datastructure(100)

# First test @equal at initialisation or not
print("1", compare_strings(s1, s2))

# Let's make an edit to s1 and then see
s1.edit_string(10, "a")
print("2", compare_strings(s1, s2))

# Reverting edit back
s1.edit_string(10, "0")
print("3", compare_strings(s1, s2))

# now edits to both
s1.edit_string(11, "11")
s2.edit_string(11, "11")
print("4", compare_strings(s1, s2))

# 0 edit
s2.edit_string(10, "0")
print("5", compare_strings(s1, s2))

# different edits
s2.edit_string(1, "!!")
print("6", compare_strings(s1, s2))

# Reverting back
s2.edit_string(1, "0")
print("7", compare_strings(s1, s2))

# Same edits to both
s1.edit_string(100, "!!")
s2.edit_string(100, "!!")
print("8", compare_strings(s1, s2))

# Same edit index but different chars to both
s1.edit_string(100, "!")
s2.edit_string(100, "!!")
print("9", compare_strings(s1, s2))

# reverts
s1.edit_string(100, "!!")
print("10", compare_strings(s1, s2))

# Different edit index and different chars to both
s1.edit_string(1, "!")
s2.edit_string(2, "!!")
print("11", compare_strings(s1, s2))


s1 = string_datastructure(10)
s2 = string_datastructure(10)
s1.edit_string(1, '1')
s1.edit_string(1, '0')
print(compare_strings(s1, s2))

"""
Identify and test boundary conditions that might challenge your code. These include:

Boundary Values: Testing inputs at the minimum and maximum limits.
Empty or Null Inputs: Ensuring your code handles cases with no data.
Large Inputs: Assessing performance and correctness with substantial data sizes.
Invalid Inputs: Checking how your code responds to unexpected or erroneous data types.
"""


    

