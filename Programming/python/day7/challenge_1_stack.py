"""
V - Visualize & Verify (The "What")

P - Pseudocode (The "How")

C - Code (The "Do")

R - Refine & Reflect (The "Check")
"""
def is_valid_parentheses(s: str) -> bool:
    """
    Given a string containing just the characters 
    '(', ')', '{', '}', '[' and ']', determine if valid.
    
    Examples:
    >>> is_valid_parentheses("()")
    True
    >>> is_valid_parentheses("()[]{}")
    True
    >>> is_valid_parentheses("(]")
    False
    >>> is_valid_parentheses("([)]")
    False
    """
    # TODO: Implement using stack
    
    # pseudocode: what if empty string? return true
    if not s:
        return True

    # pseudocode: def stack = []
    stack = []
    # pseudocode: map = { '(': ')', '{': '}', '[': ']' } 
    mapping = { '(': ')', '{': '}', '[': ']' }
    #pseudocode: loop for every char in s
    for char in s:
        # pseudocode: if char in map -> stack.push(char)
        if char in mapping:
            stack.append(char)
        
        # pseudocode: else if stack is empty -> return false
        # pseudocode: else if map[stack.pop()] != char -> return false
        else:
            if not stack:
                return False
            if mapping[stack.pop()] != char:
                return False
    # pseudocode: return true if stack is empty else false
    return len(stack) == 0
        

        