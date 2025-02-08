"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    check_stack = []
    for char in s:
        #print(f"Stack: {check_stack}")
        #print(f"Char in s: {char}")
        if check_stack:
            #print("Stack Not Empty")
            last_element = check_stack[-1]
            #print(f"Last Element in Stack: {last_element}")
            # Char is an opening bracket string
            # We append in the stack
            # As it can't close the last element
            if char in ["(", "[", "{"]:
                check_stack.append(char)
            elif char == ')':
                if last_element == "(": #Found Match Pop Last Element
                    check_stack = check_stack[:-1]
                else:
                    return False
                    #check_stack.append(char)
            elif char == ']':
                if last_element == "[": #Found Match Pop Last Element
                    check_stack = check_stack[:-1]
                else:
                    return False
                    #check_stack.append(char)
            elif char == '}':
                if last_element == "{": #Found Match Pop Last Element
                    check_stack = check_stack[:-1]
                else:
                    return False
                    #check_stack.append(char)
                    
        else:
            #print("Stack Empty, Appending")
            check_stack.append(char)

    #print(f"Final Check Stack: {check_stack}")
    if check_stack:
        return False # If it's a valid string, stack should be empty
    else:
        return True

print(isValid("()"))
print(isValid("{}(){}["))
print(isValid("{}([]){}"))
print(isValid("{{}(){}{[]}}"))
print(isValid("{}({}){}[[]"))
        