"""
🎓 Learning Recursion - Interactive Lessons

Master recursion through hands-on examples and exercises.
Run this file to learn recursion step by step!
"""

print("=" * 70)
print("🎓 Learning Recursion - Master the Art of Self-Calling Functions")
print("=" * 70)

# ============================================================================
# LESSON 1: What is Recursion?
# ============================================================================

print("\n" + "=" * 70)
print("LESSON 1: Understanding Recursion")
print("=" * 70)

print("""
Recursion is when a function calls itself to solve a smaller version
of the same problem.

Key Components:
1. BASE CASE: The stopping condition (prevents infinite recursion)
2. RECURSIVE CASE: The function calling itself with simpler input
3. PROGRESS: Each call must move toward the base case

Think of it like:
- Opening Russian nesting dolls (each one contains a smaller one)
- Looking in a mirror that reflects another mirror
- A directory containing subdirectories
""")

# Simple example: Countdown
def countdown(n):
    """Count down from n to 1."""
    # BASE CASE: Stop when we reach 0
    if n <= 0:
        print("Blast off! 🚀")
        return
    
    # Do some work
    print(f"Counting: {n}")
    
    # RECURSIVE CASE: Call ourselves with smaller number
    countdown(n - 1)

print("\nExample 1: Countdown")
print("Function: countdown(5)")
print("\nOutput:")
countdown(5)

# ============================================================================
# LESSON 2: Factorial (Classic Example)
# ============================================================================

print("\n" + "=" * 70)
print("LESSON 2: Factorial - The Hello World of Recursion")
print("=" * 70)

print("""
Factorial of n (written as n!) is:
n! = n × (n-1) × (n-2) × ... × 2 × 1

Examples:
5! = 5 × 4 × 3 × 2 × 1 = 120
3! = 3 × 2 × 1 = 6
1! = 1
0! = 1 (by definition)

Recursive thinking:
n! = n × (n-1)!
""")

def factorial(n):
    """Calculate factorial of n recursively."""
    # BASE CASE
    if n == 0 or n == 1:
        return 1
    
    # RECURSIVE CASE: n! = n × (n-1)!
    return n * factorial(n - 1)

print("\nExample: Calculating 5!")
print("\nHow it works:")
print("factorial(5)")
print("  = 5 × factorial(4)")
print("  = 5 × (4 × factorial(3))")
print("  = 5 × (4 × (3 × factorial(2)))")
print("  = 5 × (4 × (3 × (2 × factorial(1))))")
print("  = 5 × (4 × (3 × (2 × 1)))")
print("  = 5 × (4 × (3 × 2))")
print("  = 5 × (4 × 6)")
print("  = 5 × 24")
print("  = 120")

result = factorial(5)
print(f"\nResult: {result}")

# ============================================================================
# LESSON 3: Fibonacci Sequence
# ============================================================================

print("\n" + "=" * 70)
print("LESSON 3: Fibonacci - Multiple Recursive Calls")
print("=" * 70)

print("""
Fibonacci sequence: Each number is sum of previous two
0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

Formula:
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)

This demonstrates a function making TWO recursive calls!
""")

def fibonacci(n):
    """Calculate nth Fibonacci number."""
    # BASE CASES
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # RECURSIVE CASE: Two recursive calls!
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nExample: Fibonacci sequence (first 10 numbers)")
fib_sequence = [fibonacci(i) for i in range(10)]
print(f"Sequence: {fib_sequence}")

print("\nHow fibonacci(5) works:")
print("fib(5)")
print("  = fib(4) + fib(3)")
print("  = (fib(3) + fib(2)) + (fib(2) + fib(1))")
print("  = ((fib(2) + fib(1)) + (fib(1) + fib(0))) + ((fib(1) + fib(0)) + fib(1))")
print("  = ... eventually = 5")

# ============================================================================
# LESSON 4: Sum of List (Divide and Conquer)
# ============================================================================

print("\n" + "=" * 70)
print("LESSON 4: Sum of List - Working with Data Structures")
print("=" * 70)

print("""
Problem: Calculate sum of numbers in a list

Recursive approach:
- BASE CASE: Empty list has sum 0
- RECURSIVE CASE: sum = first_element + sum_of_rest

This demonstrates processing data structures recursively!
""")

def recursive_sum(numbers):
    """Calculate sum of list recursively."""
    # BASE CASE: Empty list
    if len(numbers) == 0:
        return 0
    
    # RECURSIVE CASE: first element + sum of rest
    return numbers[0] + recursive_sum(numbers[1:])

test_list = [1, 2, 3, 4, 5]
print(f"\nList: {test_list}")
print("\nHow it works:")
print("sum([1, 2, 3, 4, 5])")
print("  = 1 + sum([2, 3, 4, 5])")
print("  = 1 + (2 + sum([3, 4, 5]))")
print("  = 1 + (2 + (3 + sum([4, 5])))")
print("  = 1 + (2 + (3 + (4 + sum([5]))))")
print("  = 1 + (2 + (3 + (4 + (5 + sum([])))))")
print("  = 1 + (2 + (3 + (4 + (5 + 0))))")
print("  = 15")

result = recursive_sum(test_list)
print(f"\nResult: {result}")

# ============================================================================
# LESSON 5: Power Function (Optimization with Recursion)
# ============================================================================

print("\n" + "=" * 70)
print("LESSON 5: Power Function - Efficient Recursion")
print("=" * 70)

print("""
Problem: Calculate x^n (x to the power of n)

Naive approach: x^n = x × x^(n-1)
Efficient approach: x^n = (x^(n/2))^2  [when n is even]

This demonstrates how recursion can be optimized!
""")

def power_naive(x, n):
    """Calculate x^n naively (O(n) time)."""
    if n == 0:
        return 1
    return x * power_naive(x, n - 1)

def power_optimized(x, n):
    """Calculate x^n efficiently (O(log n) time)."""
    if n == 0:
        return 1
    
    # If n is even: x^n = (x^(n/2))^2
    if n % 2 == 0:
        half = power_optimized(x, n // 2)
        return half * half
    
    # If n is odd: x^n = x × x^(n-1)
    else:
        return x * power_optimized(x, n - 1)

print("\nExample: 2^10")
print(f"Naive approach (10 multiplications): {power_naive(2, 10)}")
print(f"Optimized approach (4 multiplications): {power_optimized(2, 10)}")

print("\nHow optimized works:")
print("power(2, 10)")
print("  = power(2, 5)^2")
print("  = (2 × power(2, 4))^2")
print("  = (2 × power(2, 2)^2)^2")
print("  = (2 × (power(2, 1)^2)^2)^2")
print("  = (2 × ((2 × power(2, 0))^2)^2)^2")
print("  = (2 × ((2 × 1)^2)^2)^2")
print("  = 1024")

# ============================================================================
# LESSON 6: Tree Traversal Preview
# ============================================================================

print("\n" + "=" * 70)
print("LESSON 6: Tree Traversal - Recursion's True Power")
print("=" * 70)

print("""
Trees are naturally recursive structures!
Each subtree is itself a tree.

Simple Tree Node:
    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None    # Left subtree
            self.right = None   # Right subtree

Traversal Pattern:
    def traverse(node):
        if node is None:    # BASE CASE
            return
        
        # Process current node
        print(node.value)
        
        # RECURSIVE CASES
        traverse(node.left)   # Traverse left subtree
        traverse(node.right)  # Traverse right subtree

This is the foundation for your BST project today!
""")

# Simple demo
class SimpleTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree(node, depth=0):
    """Print tree structure."""
    if node is None:
        return
    
    print("  " * depth + str(node.value))
    print_tree(node.left, depth + 1)
    print_tree(node.right, depth + 1)

# Build a small tree
root = SimpleTreeNode(50)
root.left = SimpleTreeNode(30)
root.right = SimpleTreeNode(70)
root.left.left = SimpleTreeNode(20)
root.left.right = SimpleTreeNode(40)

print("\nExample tree:")
print("      50")
print("     /  \\")
print("   30    70")
print("  /  \\")
print(" 20  40")

print("\nRecursive traversal output:")
print_tree(root)

# ============================================================================
# EXERCISES
# ============================================================================

print("\n" + "=" * 70)
print("🎯 YOUR EXERCISES")
print("=" * 70)

print("""
Complete these exercises to practice recursion:
Edit this file and implement the functions below!
""")

# Exercise 1: Reverse a string
def reverse_string(s):
    """
    Reverse a string using recursion.
    
    Examples:
        reverse_string("hello") → "olleh"
        reverse_string("python") → "nohtyp"
    
    Hint:
        - BASE CASE: Empty string or single character
        - RECURSIVE CASE: last_char + reverse(rest_of_string)
    """
    # TODO: Implement this!
    # Your code here
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

# Exercise 2: Count occurrences in list
def count_occurrences(lst, target):
    """
    Count how many times target appears in lst.
    
    Examples:
        count_occurrences([1, 2, 3, 2, 2], 2) → 3
        count_occurrences([1, 2, 3], 5) → 0
    
    Hint:
        - BASE CASE: Empty list has 0 occurrences
        - RECURSIVE CASE: Check first element, add 1 if match
    """
    # TODO: Implement this!
    # Your code here
    if len(lst) == 0:
        return 0
    count = 1 if lst[0] == target else 0
    return count + count_occurrences(lst[1:], target)

# Exercise 3: Palindrome checker
def is_palindrome(s):
    """
    Check if string is a palindrome using recursion.
    
    Examples:
        is_palindrome("racecar") → True
        is_palindrome("hello") → False
    
    Hint:
        - BASE CASE: Empty string or single character is palindrome
        - RECURSIVE CASE: Check first and last chars match,
                         then check middle part
    """
    # TODO: Implement this!
    # Your code here
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Test exercises
print("\n" + "=" * 70)
print("EXERCISE 1: Reverse String")
print("=" * 70)
test_str = "recursion"
print(f"reverse_string('{test_str}') = {reverse_string(test_str)}")

print("\n" + "=" * 70)
print("EXERCISE 2: Count Occurrences")
print("=" * 70)
test_list = [1, 2, 3, 2, 4, 2, 5]
print(f"count_occurrences({test_list}, 2) = {count_occurrences(test_list, 2)}")

print("\n" + "=" * 70)
print("EXERCISE 3: Palindrome Checker")
print("=" * 70)
test_words = ["racecar", "hello", "level", "python"]
for word in test_words:
    result = is_palindrome(word)
    print(f"is_palindrome('{word}') = {result}")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("\n" + "=" * 70)
print("🎓 KEY TAKEAWAYS")
print("=" * 70)

print("""
1. Every recursive function MUST have:
   ✓ BASE CASE (stopping condition)
   ✓ RECURSIVE CASE (calling itself)
   ✓ PROGRESS (moving toward base case)

2. Recursion is great for:
   ✓ Tree and graph traversal
   ✓ Divide and conquer algorithms
   ✓ Problems with recursive structure
   ✓ Backtracking algorithms

3. Recursion vs Iteration:
   ✓ Recursion: Often cleaner, more intuitive for trees
   ✓ Iteration: Usually more efficient, no stack overflow risk
   
4. Common pitfalls:
   ✗ Forgetting base case → Infinite recursion
   ✗ Not making progress → Stack overflow
   ✗ Too many recursive calls → Poor performance

5. Debugging tips:
   ✓ Add print statements to trace calls
   ✓ Draw the call stack on paper
   ✓ Test with small inputs first
   ✓ Check that you're moving toward base case

Remember: Recursion is a tool, not always the best tool!
Sometimes iteration is simpler and more efficient.
""")

print("\n" + "=" * 70)
print("✅ Lessons Complete! Ready to build Binary Search Trees!")
print("=" * 70)
