def is_balanced(expression):
    # Define a dictionary to map closing brackets to their corresponding opening brackets
    brackets_map = {')': '(', '}': '{', ']': '['}
    
    # Initialize an empty stack to store opening brackets
    stack = []

    # Iterate through each character in the expression
    for char in expression:
        # If the character is an opening bracket, push it onto the stack
        if char in "({[":
            stack.append(char)
        # If the character is a closing bracket
        elif char in ")}]":
            # Check if the stack is empty (no matching opening bracket)
            if not stack:
                return False
            # Pop the top element from the stack and check if it matches the current closing bracket
            top = stack.pop()
            if top != brackets_map[char]:
                return False
    
    # After processing all characters, if the stack is empty, the expression is balanced
    return True


expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  
print(is_balanced(expression2))  