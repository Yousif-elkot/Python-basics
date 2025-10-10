def check_brackets(expression: str) -> bool:
    """Check if the brackets in the expression are balanced."""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'} # Dictionary lookup approach
    opening = '({['
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in pairs:
            if len(stack) == 0:
                return False # No matching opening bracket
            popped = stack.pop()
            if popped != pairs[char]:
                return False # Wrong bracket type
    
    return len(stack) == 0 # True if all brackets matched

def main():
    "Test the checker"
    test_cases = [
        ("()", True),
        ("(())", True),
        ("(()())", True),
        ("(()", False),
        (")(", False),
        ("())", False),
        ("()[]{}", True),
        ("([{}])", True),
        ("([)]", False),
        ("{[()]}", True),
        ("{[(])}", False),
    ]

    print("Testing balanced brackets checker:")
    print("-" * 50)

    for expression, expected in test_cases:
        result = check_brackets(expression)
        status = "PASS" if result == expected else "FAIL"
        print(f"Expression: {expression:10} | Expected: {expected} | Got: {result} | {status}")

if __name__ == "__main__":
    main()