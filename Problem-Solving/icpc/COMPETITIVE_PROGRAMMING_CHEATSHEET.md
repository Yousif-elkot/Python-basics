# 🚀 COMPETITIVE PROGRAMMING CHEAT SHEET
## Quick Reference for ICPC Contests

---

## 📥 INPUT/OUTPUT OPTIMIZATION

### Fast Input (Use for large inputs)
```python
import sys
input = sys.stdin.readline

# Read single integer
n = int(input())

# Read multiple integers on one line
a, b, c = map(int, input().split())

# Read array
arr = list(map(int, input().split()))

# Read ALL input at once (best for multiple test cases)
data = sys.stdin.read().split()
index = 0
t = int(data[index])
index += 1
```

### Common Input Patterns
```python
# Single test case
n = int(input())

# Multiple test cases
t = int(input())
for _ in range(t):
    # solve each test case
    pass

# Reading n lines
n = int(input())
for _ in range(n):
    line = input().strip()
```

---

## 📊 DATA TYPES & OPERATIONS

### Important Limits
```python
# Python integers: unlimited size! No overflow
# But be careful with time limits

# Maximum list size: ~10^8 elements (memory limit)
# Typical constraints: 10^5 to 10^6
```

### Common Operations
```python
# Integer division (floor)
a // b  # 7 // 2 = 3

# Modulo
a % b   # 7 % 2 = 1

# Power
pow(a, b)        # a^b
pow(a, b, m)     # (a^b) % m - FAST modular exponentiation

# Absolute value
abs(x)

# Min/Max
min(a, b, c)
max(a, b, c)

# GCD and LCM
import math
gcd = math.gcd(a, b)
lcm = a * b // gcd
```

---

## 🔢 MATHEMATICAL FORMULAS

### Sum Formulas
```python
# Sum of 1 to n
sum_n = n * (n + 1) // 2

# Sum of squares: 1² + 2² + ... + n²
sum_squares = n * (n + 1) * (2*n + 1) // 6

# Sum of cubes: 1³ + 2³ + ... + n³
sum_cubes = (n * (n + 1) // 2) ** 2
```

### Number Theory
```python
import math

# Check if prime (simple)
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Sieve of Eratosthenes (for multiple primes)
def sieve(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    return is_prime

# Number of digits in number
digits = len(str(n))

# Or using logarithms
import math
digits = math.floor(math.log10(n)) + 1 if n > 0 else 1
```

### Combinatorics
```python
import math

# Factorial
fact = math.factorial(n)

# Combinations: C(n, k) = n! / (k! * (n-k)!)
comb = math.comb(n, k)

# Permutations: P(n, k) = n! / (n-k)!
perm = math.perm(n, k)
```

---

## 📝 ARRAYS (LISTS)

### Creation
```python
# Empty list
arr = []

# List with n zeros
arr = [0] * n

# 2D array (n x m)
matrix = [[0] * m for _ in range(n)]

# List comprehension
squares = [i**2 for i in range(n)]

# From input
arr = list(map(int, input().split()))
```

### Common Operations
```python
# Append (end)
arr.append(x)      # O(1)

# Insert at position
arr.insert(i, x)   # O(n)

# Remove by value
arr.remove(x)      # O(n)

# Remove by index
arr.pop(i)         # O(n), arr.pop() for last element O(1)

# Length
len(arr)

# Sum
sum(arr)

# Min/Max
min(arr)
max(arr)

# Sort (in-place)
arr.sort()         # Ascending
arr.sort(reverse=True)  # Descending

# Sorted (returns new list)
sorted_arr = sorted(arr)

# Reverse
arr.reverse()      # In-place
reversed_arr = arr[::-1]  # New list

# Count occurrences
count = arr.count(x)

# Find index
index = arr.index(x)  # Raises error if not found
```

### Slicing
```python
# arr[start:end:step]
arr[2:5]      # Elements at index 2, 3, 4
arr[:3]       # First 3 elements
arr[3:]       # From index 3 to end
arr[-3:]      # Last 3 elements
arr[::2]      # Every 2nd element
arr[::-1]     # Reverse
```

### Prefix Sums (Range Queries)
```python
# Build prefix sum
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i-1] + arr[i-1]

# Query sum from index l to r (0-based)
range_sum = prefix[r+1] - prefix[l]
```

### Two Pointers Pattern
```python
# Example: Find pair with sum = target
left, right = 0, len(arr) - 1
while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        # Found!
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1
```

---

## 📜 STRINGS

### Common Operations
```python
# Length
len(s)

# Concatenation
s = s1 + s2

# Repeat
s = "ab" * 3  # "ababab"

# Access character
c = s[i]

# Substring
sub = s[start:end]

# Convert to list (for modifications)
chars = list(s)
# ... modify chars ...
s = ''.join(chars)

# Case conversion
s.lower()
s.upper()

# Check methods
s.isalpha()    # All alphabetic
s.isdigit()    # All digits
s.isalnum()    # Alphanumeric
s.islower()
s.isupper()

# String methods
s.strip()      # Remove whitespace
s.split()      # Split by whitespace
s.split(',')   # Split by delimiter
s.replace(old, new)
s.count(sub)   # Count occurrences
s.find(sub)    # Find index (-1 if not found)
s.startswith(prefix)
s.endswith(suffix)
```

### String Formatting
```python
# f-strings (Python 3.6+)
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")

# Format with padding
print(f"{num:02d}")  # 5 -> "05"
print(f"{num:5d}")   # 5 -> "    5"
```

### Character Operations
```python
# ASCII value
ord('a')  # 97
ord('A')  # 65

# Character from ASCII
chr(97)   # 'a'

# Lowercase letter to index (0-25)
index = ord(c) - ord('a')

# Index to lowercase letter
c = chr(index + ord('a'))
```

### Frequency Counting (for anagrams, etc.)
```python
from collections import Counter

# Count characters
freq = Counter(s)
print(freq['a'])  # Frequency of 'a'

# Or manually with array (faster for lowercase letters)
freq = [0] * 26
for c in s:
    freq[ord(c) - ord('a')] += 1
```

---

## 🔄 LOOPS

### For Loops
```python
# Range: 0 to n-1
for i in range(n):
    print(i)

# Range: start to end-1
for i in range(start, end):
    print(i)

# Range with step
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# Reverse range
for i in range(n-1, -1, -1):
    print(i)

# Iterate over list
for item in arr:
    print(item)

# Enumerate (index + item)
for i, item in enumerate(arr):
    print(f"Index {i}: {item}")

# Multiple lists (zip)
for a, b in zip(list1, list2):
    print(a, b)
```

### While Loops
```python
# Basic while
while condition:
    # do something
    pass

# Common pattern
i = 0
while i < n:
    # do something
    i += 1

# Break early
while True:
    # do something
    if condition:
        break

# Continue to next iteration
while condition:
    if skip_condition:
        continue
    # do something
```

### Nested Loops (2D iterations)
```python
# Iterate through matrix
for i in range(n):
    for j in range(m):
        print(matrix[i][j])

# Iterate pairs
for i in range(n):
    for j in range(i+1, n):
        # Process pair (i, j)
        pass
```

---

## 🎯 CONTROL FLOW

### If-Else
```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code

# Ternary operator
result = value_if_true if condition else value_if_false

# Multiple conditions
if x > 0 and x < 10:
    pass

if x == 1 or x == 2:
    pass

if x not in [1, 2, 3]:
    pass
```

### Boolean Logic
```python
# and, or, not
a and b
a or b
not a

# Comparison
==, !=, <, >, <=, >=

# Chaining
if 0 < x < 10:  # Same as: x > 0 and x < 10
    pass
```

---

## 🔁 RECURSION

### Basic Template
```python
def recursive_function(n):
    # Base case (CRITICAL!)
    if n <= 0:
        return base_value
    
    # Recursive case
    result = recursive_function(n - 1) + something
    return result
```

### Common Patterns

#### Factorial
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

#### Fibonacci
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# With memoization (faster!)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

#### Power
```python
def power(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    
    half = power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    else:
        return half * half * base
```

### Recursion Tips
- **ALWAYS have a base case!**
- Make sure recursive calls progress toward base case
- Watch out for stack overflow (Python limit ~1000)
- Consider iterative/DP approach for deep recursion

---

## 🧮 DYNAMIC PROGRAMMING (DP)

### Bottom-Up (Tabulation)
```python
# Example: Climbing stairs (1 or 2 steps)
def climb_stairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

### Top-Down (Memoization)
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def climb_stairs(n):
    if n <= 2:
        return n
    return climb_stairs(n-1) + climb_stairs(n-2)
```

---

## 📚 DATA STRUCTURES

### Dictionary (Hash Map)
```python
# Create
d = {}
d = dict()

# Add/Update
d[key] = value

# Get value
value = d[key]           # KeyError if not found
value = d.get(key, default)  # Returns default if not found

# Check existence
if key in d:
    pass

# Delete
del d[key]
d.pop(key, default)

# Iterate
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)

# Default dict (auto-initialize)
from collections import defaultdict
d = defaultdict(int)     # Defaults to 0
d = defaultdict(list)    # Defaults to []
```

### Set
```python
# Create
s = set()
s = {1, 2, 3}

# Add
s.add(x)

# Remove
s.remove(x)      # KeyError if not found
s.discard(x)     # No error if not found

# Check membership
if x in s:
    pass

# Set operations
a | b   # Union
a & b   # Intersection
a - b   # Difference
a ^ b   # Symmetric difference
```

### Counter
```python
from collections import Counter

# Count elements
freq = Counter(arr)
freq = Counter("hello")

# Most common
freq.most_common(3)  # Top 3 most frequent

# Operations
freq[x]  # Count of x (0 if not present)
```

### Deque (Double-ended queue)
```python
from collections import deque

# Create
q = deque()

# Add
q.append(x)       # Add to right
q.appendleft(x)   # Add to left

# Remove
q.pop()           # Remove from right
q.popleft()       # Remove from left

# Used for BFS, sliding window
```

---

## 🎲 COMMON ALGORITHMS

### Binary Search
```python
# Find target in sorted array
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

# Using bisect module
import bisect
index = bisect.bisect_left(arr, target)
```

### Sliding Window
```python
# Example: Max sum of subarray of size k
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1
    
    # First window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window
    for i in range(k, n):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Frequency Array for Anagrams
```python
# Check if substring is anagram
def is_anagram_substring(s, m):
    s_len = len(s)
    m_len = len(m)
    
    if s_len > m_len:
        return False
    
    # Frequency arrays
    s_freq = [0] * 26
    for c in s:
        s_freq[ord(c) - ord('a')] += 1
    
    window_freq = [0] * 26
    for i in range(s_len):
        window_freq[ord(m[i]) - ord('a')] += 1
    
    if window_freq == s_freq:
        return True
    
    # Sliding window
    for i in range(s_len, m_len):
        window_freq[ord(m[i]) - ord('a')] += 1
        window_freq[ord(m[i - s_len]) - ord('a')] -= 1
        
        if window_freq == s_freq:
            return True
    
    return False
```

---

## 🔧 COMMON TRICKS & TIPS

### Avoid TLE (Time Limit Exceeded)
```python
# 1. Use fast input
import sys
input = sys.stdin.readline

# 2. Avoid repeated calculations
# BAD: for i in range(len(arr))  # Calls len() every iteration
# GOOD: n = len(arr); for i in range(n)

# 3. Use sets for membership checks (O(1) vs O(n) for lists)

# 4. Precompute when possible (prefix sums, etc.)

# 5. Choose right data structure
# - Dictionary for counting/mapping: O(1)
# - Set for unique elements: O(1)
# - List for indexed access: O(1)

# 6. Avoid string concatenation in loops
# BAD: s = ""; for x in arr: s += str(x)
# GOOD: s = ''.join(str(x) for x in arr)
```

### Handle Large Numbers
```python
# Modular arithmetic
MOD = 10**9 + 7

# For multiplication
result = (a * b) % MOD

# For addition
result = (a + b) % MOD

# For power
result = pow(a, b, MOD)
```

### Avoid Float Precision Issues
```python
# Use integers when possible
# For probabilities, use fractions
from fractions import Fraction
prob = Fraction(numerator, denominator)

# For comparison with tolerance
epsilon = 1e-9
if abs(a - b) < epsilon:
    # a and b are equal
    pass
```

### Common Edge Cases to Check
- Empty input (n=0, empty string)
- Single element (n=1)
- All same elements
- Sorted/reverse sorted
- Maximum constraints (n=10^5, values=10^9)
- Negative numbers
- Zero

---

## 📋 TEMPLATE FOR CONTESTS

```python
#!/usr/bin/env python3
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

# Fast input
input = sys.stdin.readline

def solve():
    # Your solution here
    pass

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()
```

---

## ⚡ TIME COMPLEXITY GUIDE

| Operation | Complexity | Max n (1 sec) |
|-----------|-----------|---------------|
| O(1) | Constant | ∞ |
| O(log n) | Logarithmic | ∞ |
| O(n) | Linear | 10^8 |
| O(n log n) | Sorting | 10^6 |
| O(n²) | Nested loops | 10^4 |
| O(n³) | Triple nested | 500 |
| O(2^n) | Exponential | 20 |
| O(n!) | Factorial | 11 |

---

## 🎯 PROBLEM-SOLVING STRATEGY

1. **Read Carefully**: Understand input/output format
2. **Identify Pattern**: What type of problem? (Math, DP, Greedy, etc.)
3. **Think of Constraints**: What's the max n? What complexity is needed?
4. **Edge Cases**: What breaks my solution?
5. **Code**: Write clean, modular code
6. **Test**: Try examples, edge cases
7. **Debug**: If WA, check edge cases, overflow, off-by-one errors
8. **Optimize**: If TLE, improve algorithm or I/O

---

## 📌 QUICK WINS

```python
# Read all input at once for multiple test cases
data = sys.stdin.read().split()

# GCD
import math
gcd = math.gcd(a, b)

# LCM
lcm = a * b // math.gcd(a, b)

# Digit count
digits = len(str(n))

# Check parity
if n % 2 == 0:  # Even
if n % 2 == 1:  # Odd

# Swap
a, b = b, a

# Min/max of multiple values
min_val = min(a, b, c, d)
max_val = max(a, b, c, d)

# Clamp value
x = max(min_val, min(x, max_val))
```

---

**Good luck in your contests! 🚀**
