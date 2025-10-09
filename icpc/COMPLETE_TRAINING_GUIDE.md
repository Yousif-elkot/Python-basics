# 📚 COMPLETE ICPC TRAINING GUIDE
## 6 Weeks of Competitive Programming - Everything Covered

---

## 📖 TABLE OF CONTENTS

1. [Week 1: Data Types & Control Flow](#week-1-data-types--control-flow)
2. [Week 2: Loops, Arrays, Strings](#week-2-loops-arrays-strings)
3. [Week 3: More on Loops, Arrays, Strings](#week-3-more-on-loops-arrays-strings)
4. [Week 4: Math & Geometry](#week-4-math--geometry)
5. [Week 5: Recursion & Advanced Math](#week-5-recursion--advanced-math)
6. [Week 6: Mixed Problems](#week-6-mixed-problems)
7. [Key Learnings & Patterns](#key-learnings--patterns)
8. [Common Mistakes & How to Avoid](#common-mistakes--how-to-avoid)

---

## Week 1: Data Types & Control Flow

### Topics Covered
- **Input/Output**: Reading integers, floats, multiple values
- **Variables**: int, float, string
- **Basic Math**: +, -, *, /, //, %, **
- **Conditionals**: if-elif-else
- **Comparison**: ==, !=, <, >, <=, >=
- **Logical operators**: and, or, not

### Key Problems & Solutions

#### Problem Type 1: Simple I/O & Calculations
**Example**: Read two numbers, print their sum
```python
a, b = map(int, input().split())
print(a + b)
```

**Learning**: 
- Use `map()` to convert multiple inputs
- Use `split()` to separate space-separated values

#### Problem Type 2: Conditional Logic
**Example**: Check if number is even/odd
```python
n = int(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Learning**:
- Modulo operator `%` for divisibility
- Simple if-else structure

#### Problem Type 3: Multiple Conditions
**Example**: Grade calculator
```python
score = int(input())
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

**Learning**:
- elif chains for multiple ranges
- Order matters (check highest first)

#### Problem Type 4: Float Precision
**Example**: Calculate circle area with specific precision
```python
import math
r = float(input())
area = math.pi * r * r
print(f"{area:.2f}")  # 2 decimal places
```

**Learning**:
- `math.pi` for π constant
- f-string formatting for precision: `{value:.2f}`

### Week 1 Key Takeaways
✅ Master basic input/output patterns  
✅ Understand when to use int vs float  
✅ Practice if-elif-else logic  
✅ Learn float formatting  
✅ Use `math` module for constants and functions

---

## Week 2: Loops, Arrays, Strings

### Topics Covered
- **For loops**: range(), enumerate(), zip()
- **While loops**: condition-based iteration
- **Lists (Arrays)**: creation, indexing, slicing
- **String operations**: concatenation, slicing, methods
- **Nested loops**: 2D iterations

### Key Problems & Solutions

#### Problem Type 1: Basic Loops
**Example**: Print numbers 1 to n
```python
n = int(input())
for i in range(1, n+1):
    print(i)
```

**Learning**:
- `range(start, end)` excludes end
- `range(n)` starts at 0

#### Problem Type 2: List Operations
**Example**: Read array, find maximum
```python
n = int(input())
arr = list(map(int, input().split()))
print(max(arr))
```

**Learning**:
- `list(map())` pattern for reading arrays
- Built-in `max()`, `min()`, `sum()`

#### Problem Type 3: String Manipulation
**Example**: Count vowels in string
```python
s = input()
vowels = "aeiouAEIOU"
count = sum(1 for c in s if c in vowels)
print(count)
```

**Learning**:
- String membership with `in`
- List comprehensions for counting
- Sets for faster lookups

#### Problem Type 4: Nested Loops
**Example**: Print multiplication table
```python
n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i * j, end=" ")
    print()  # Newline after each row
```

**Learning**:
- Nested loops for 2D patterns
- `end=" "` to control print behavior

#### Problem Type 5: Array Sorting
**Example**: Sort and find median
```python
arr = list(map(int, input().split()))
arr.sort()
n = len(arr)
if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n//2 - 1] + arr[n//2]) / 2
print(median)
```

**Learning**:
- `.sort()` for in-place sorting
- `sorted()` for new sorted list
- Index arithmetic for middle element

### Week 2 Key Takeaways
✅ Master for/while loop patterns  
✅ Comfortable with list operations  
✅ Understand string indexing and slicing  
✅ Practice nested loops for 2D problems  
✅ Know when to sort data

---

## Week 3: More on Loops, Arrays, Strings

### Topics Covered
- **Advanced loops**: break, continue
- **String algorithms**: palindromes, anagrams
- **Array algorithms**: two pointers, sliding window
- **Frequency counting**: Counter, manual arrays
- **Pattern matching**: subsequences

### Key Problems & Solutions

#### Problem Type 1: Binary String Validation
**Example**: Check if both 0s and 1s appear with even counts
```python
s = input()
ones = s.count('1')
zeros = s.count('0')
if ones > 0 and zeros > 0 and ones % 2 == 0 and zeros % 2 == 0:
    print("YES")
else:
    print("NO")
```

**Learning**:
- `.count()` method for strings
- Multiple conditions with `and`

#### Problem Type 2: Anagram Detection (Sliding Window)
**Example**: Check if substring of m is anagram of s
```python
def has_anagram_substring(s, m):
    s_len, m_len = len(s), len(m)
    if s_len > m_len:
        return False
    
    # Frequency arrays (26 letters)
    s_freq = [0] * 26
    for c in s:
        s_freq[ord(c) - ord('a')] += 1
    
    # First window
    window_freq = [0] * 26
    for i in range(s_len):
        window_freq[ord(m[i]) - ord('a')] += 1
    
    if window_freq == s_freq:
        return True
    
    # Slide window
    for i in range(s_len, m_len):
        window_freq[ord(m[i]) - ord('a')] += 1
        window_freq[ord(m[i - s_len]) - ord('a')] -= 1
        if window_freq == s_freq:
            return True
    
    return False
```

**Learning**:
- **Sliding window**: Efficient O(n) substring checks
- **Frequency arrays**: [0]*26 for lowercase letters
- **Character indexing**: `ord(c) - ord('a')` maps 'a'→0, 'b'→1, etc.
- **Why it's fast**: Avoids recalculating entire window

#### Problem Type 3: Frequency Counting
**Example**: Find most frequent element
```python
from collections import Counter
arr = list(map(int, input().split()))
freq = Counter(arr)
most_common = freq.most_common(1)[0][0]
print(most_common)
```

**Learning**:
- `Counter` for automatic frequency counting
- `.most_common(k)` returns top k frequent

#### Problem Type 4: Prefix Sums
**Example**: Answer q range sum queries efficiently
```python
n = int(input())
arr = list(map(int, input().split()))

# Build prefix sums
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i-1] + arr[i-1]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    # Sum from index l to r (0-based)
    print(prefix[r+1] - prefix[l])
```

**Learning**:
- **Prefix sums**: Precompute for O(1) range queries
- Build once, query many times
- Pattern: `prefix[r+1] - prefix[l]` for range [l, r]

### Week 3 Key Takeaways
✅ Master sliding window technique  
✅ Use frequency arrays for character counting  
✅ Implement prefix sums for range queries  
✅ Understand anagram detection  
✅ Optimize substring problems

---

## Week 4: Math & Geometry

### Topics Covered
- **Number theory**: primes, GCD, LCM
- **Parity**: even/odd tricks
- **Geometry**: points, lines, collinearity
- **Cross product**: line intersection
- **Divisibility**: patterns and rules

### Key Problems & Solutions

#### Problem Type 1: Parity Problems
**Example**: Split n into k odd numbers
```python
n, k = map(int, input().split())

# Key insight: sum of k odd numbers is odd if k is odd, even if k is even
if n < k:
    print("NO")
elif n % 2 == k % 2:  # Same parity
    print("YES")
else:
    print("NO")
```

**Learning**:
- **Mathematical pattern**: k odd numbers → sum has same parity as k
- **Minimum check**: Need at least k (k ones)
- **Parity matching**: n and k must have same parity

#### Problem Type 2: Prime Checking
**Example**: Sieve of Eratosthenes for multiple primes
```python
def sieve(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    
    return is_prime

# Usage
primes = sieve(1000000)
if primes[n]:
    print("Prime")
```

**Learning**:
- **Sieve**: O(n log log n) - find all primes up to n
- **Optimization**: Only check up to √n
- **Memory**: Boolean array for fast lookup

#### Problem Type 3: Geometry - Collinearity
**Example**: Check if point is on line segment
```python
def is_on_segment(x1, y1, x2, y2, xi, yi):
    # Cross product for collinearity
    cross = (y2 - y1) * (xi - x1) - (yi - y1) * (x2 - x1)
    
    # If not collinear, return False
    if cross != 0:
        return False
    
    # Check if point is between endpoints
    if min(x1, x2) <= xi <= max(x1, x2) and \
       min(y1, y2) <= yi <= max(y1, y2):
        return True
    
    return False
```

**Learning**:
- **Cross product**: Tests collinearity (= 0 means on same line)
- **Bounding box**: Check if point is within segment bounds
- **Avoids division**: No slope calculation (avoids float errors)

#### Problem Type 4: Mathematical Formula Simplification
**Example**: Complex sum formula
```python
# Instead of computing: sum(2k² - k + 1/6) - sum(k - 1/6)
# Simplify algebraically first!

n = int(input())
# Direct formula after simplification
result = sum(2*k**2 - k + 1/6 for k in range(1, n+1)) - \
         sum(k - 1/6 for k in range(1, n+1))
print(int(result))
```

**Learning**:
- **Algebraic simplification**: Reduce operations before coding
- **Recognize patterns**: Many problems have closed-form formulas
- **Watch for fractions**: 16 might actually mean 1/6!

### Week 4 Key Takeaways
✅ Understand parity and divisibility  
✅ Use Sieve for multiple prime checks  
✅ Master cross product for geometry  
✅ Simplify mathematical formulas  
✅ Avoid floating point when possible

---

## Week 5: Recursion & Advanced Math

### Topics Covered
- **Recursion**: base cases, recursive relations
- **Dynamic Programming**: bottom-up, top-down
- **Memoization**: @lru_cache decorator
- **Combinatorics**: counting problems
- **Probability**: fractions and simplification

### Key Problems & Solutions

#### Problem Type 1: Basic Recursion
**Example**: Custom recursive function
```python
def R(n):
    # Base case - CRITICAL!
    if n < 1:
        return 1
    
    # Recursive case
    return R(n // 2) + R(Q(n) - 1) + R(Q(n) - 3)

def Q(n):
    return n % m
```

**Learning**:
- **ALWAYS have base case**: Prevents infinite recursion
- **Progress toward base**: Each call should reduce problem size
- **Stack depth**: Python limit ~1000 calls

#### Problem Type 2: Dynamic Programming - Sandwich Problem
**Example**: Count ways to make n kg with {1, 2, 3} kg sandwiches
```python
# Precompute DP table
MAX_N = 27
dp = [0] * (MAX_N + 1)
dp[0] = 1  # Base case

for i in range(1, MAX_N + 1):
    # Can end with 1kg, 2kg, or 3kg sandwich
    if i >= 1:
        dp[i] += dp[i-1]
    if i >= 2:
        dp[i] += dp[i-2]
    if i >= 3:
        dp[i] += dp[i-3]

# Answer queries in O(1)
n = int(input())
print(dp[n])
```

**Learning**:
- **DP pattern**: Current state depends on previous states
- **Precomputation**: Build table once, answer queries fast
- **Order matters**: 1+2 ≠ 2+1 (permutations not combinations)
- **Recurrence**: dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

#### Problem Type 3: Generating Sequences
**Example**: Generate all balanced parentheses (recursion)
```python
def generate(current, open_count, close_count, n):
    # Base case: used all brackets
    if open_count == n and close_count == n:
        print(current)
        return
    
    # Add opening bracket if possible
    if open_count < n:
        generate(current + '(', open_count + 1, close_count, n)
    
    # Add closing bracket if valid
    if close_count < open_count:
        generate(current + ')', open_count, close_count + 1, n)

# Start generation
n = int(input())
generate('', 0, 0, n)
```

**Learning**:
- **Backtracking**: Build solution incrementally
- **Validity constraints**: Only add ')' if more '(' exist
- **All solutions**: Explores all valid paths

#### Problem Type 4: Probability with Fractions
**Example**: Dice probability in simplified form
```python
import math

n, m = map(int, input().split())

# Count numbers divisible by m in range [1, n]
count_divisible = n // m

# Simplify fraction
numerator = count_divisible
denominator = n

gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd

print(f"{numerator}/{denominator}")
```

**Learning**:
- **GCD simplification**: Always reduce fractions
- **Avoid floats**: Keep as integer fractions
- **Floor division**: Count divisibles = n // m

### Week 5 Key Takeaways
✅ Master recursion with proper base cases  
✅ Understand DP bottom-up approach  
✅ Use memoization for optimization  
✅ Generate sequences with backtracking  
✅ Handle fractions with GCD

---

## Week 6: Mixed Problems

### Advanced Techniques

#### Large Number Optimization
**Problem**: Computing digits in huge products
```python
import math

# Instead of computing 15^88 directly (huge!)
# Use logarithms: log10(product) = sum of log10(values)

n = int(input())
q = int(input())
arr = list(map(int, input().split()))

# Prefix sums of logarithms
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i-1] + math.log10(arr[i-1])

for _ in range(q):
    l, r = map(int, input().split())
    left, right = min(l, r) - 1, max(l, r) - 1
    
    # Sum of logarithms = logarithm of product
    log_sum = prefix[right + 1] - prefix[left]
    
    # Number of digits = floor(log10(product)) + 1
    digits = math.floor(log_sum) + 1
    print(digits)
```

**Learning**:
- **Logarithm trick**: Convert multiplication to addition
- **Digit formula**: digits = floor(log10(n)) + 1
- **Prefix sums**: Works with logs too!
- **Avoids overflow**: Never compute the actual product

#### Modular Exponentiation
**Problem**: Last 2 digits of 15^n
```python
n = int(input())

# Compute 15^n mod 100 directly
# pow(base, exp, mod) is FAST
last_two_digits = pow(15, n, 100)

# Format with leading zero if needed
print(f"{last_two_digits:02d}")
```

**Learning**:
- **Three-argument pow()**: Computes (base^exp) % mod efficiently
- **Why it's fast**: Uses binary exponentiation O(log n)
- **Avoids huge numbers**: Never stores full 15^n

---

## Key Learnings & Patterns

### Pattern 1: Frequency Counting
**When to use**: Anagrams, character/element counting
```python
# For lowercase letters (fast)
freq = [0] * 26
for c in s:
    freq[ord(c) - ord('a')] += 1

# For any elements
from collections import Counter
freq = Counter(arr)
```

### Pattern 2: Sliding Window
**When to use**: Substring problems, consecutive elements
```python
# Fixed-size window
window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, n):
    window_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum, window_sum)
```

### Pattern 3: Prefix Sums
**When to use**: Multiple range queries
```python
# Build
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i-1] + arr[i-1]

# Query [l, r]
range_sum = prefix[r+1] - prefix[l]
```

### Pattern 4: Two Pointers
**When to use**: Sorted array problems, pair finding
```python
left, right = 0, len(arr) - 1
while left < right:
    if condition(arr[left], arr[right]):
        # Process
        left += 1
        right -= 1
    elif condition2:
        left += 1
    else:
        right -= 1
```

### Pattern 5: Dynamic Programming
**When to use**: Overlapping subproblems, optimization
```python
# Bottom-up
dp = [0] * (n + 1)
dp[0] = base_value

for i in range(1, n + 1):
    dp[i] = function(dp[i-1], dp[i-2], ...)
```

---

## Common Mistakes & How to Avoid

### Mistake 1: Wrong Input Reading
❌ **Wrong**:
```python
input = sys.stdin.readline  # Overrides input
data = input().split()  # Only reads one line!
```

✅ **Right**:
```python
data = sys.stdin.read().split()  # Reads all input
```

### Mistake 2: Off-by-One Errors
❌ **Wrong**:
```python
for i in range(n):  # 0 to n-1
    # But problem uses 1-indexed!
```

✅ **Right**:
```python
for i in range(1, n+1):  # 1 to n
    arr[i-1]  # Adjust for 0-indexed array
```

### Mistake 3: Missing Base Case in Recursion
❌ **Wrong**:
```python
def R(n):
    return R(n-1) + something  # Infinite recursion!
```

✅ **Right**:
```python
def R(n):
    if n <= 0:  # Base case
        return base_value
    return R(n-1) + something
```

### Mistake 4: Integer Division Confusion
❌ **Wrong**:
```python
avg = sum / count  # Float division
```

✅ **Right for floor**:
```python
avg = sum // count  # Integer division
```

### Mistake 5: Modifying List While Iterating
❌ **Wrong**:
```python
for item in arr:
    arr.remove(item)  # Skips elements!
```

✅ **Right**:
```python
arr = [item for item in arr if condition]  # New list
```

### Mistake 6: Comparing Floats Directly
❌ **Wrong**:
```python
if a == b:  # Precision issues!
```

✅ **Right**:
```python
epsilon = 1e-9
if abs(a - b) < epsilon:
```

---

## Practice Strategy

### Phase 1: Fundamentals (Weeks 1-2)
- ✅ Master I/O patterns
- ✅ Practice basic loops and conditionals
- ✅ Get comfortable with lists and strings

### Phase 2: Algorithms (Weeks 3-4)
- ✅ Learn sliding window
- ✅ Implement prefix sums
- ✅ Understand two pointers
- ✅ Practice sorting applications

### Phase 3: Advanced (Weeks 5-6)
- ✅ Master recursion and DP
- ✅ Learn mathematical optimizations
- ✅ Handle large numbers with logs/modulo
- ✅ Solve mixed problem types

### Next Steps
1. **STLs**: Learn advanced data structures (heaps, sets, deques)
2. **General III**: Practice more complex problems
3. **Speed**: Improve implementation speed
4. **Debugging**: Get faster at finding bugs

---

## 🏆 FINAL TIPS FOR SUCCESS

1. **Read problems twice**: Understand before coding
2. **Check constraints**: Determines algorithm choice
3. **Test edge cases**: n=0, n=1, max values
4. **Use fast I/O**: `sys.stdin.read()` for multiple test cases
5. **Simplify math**: Look for patterns and formulas
6. **Debug systematically**: Print intermediate values
7. **Practice regularly**: Speed comes with repetition
8. **Learn from mistakes**: Analyze why solutions failed

---

**You've completed 6 weeks of training! You now have:**
- ✅ Strong foundation in Python for CP
- ✅ Core algorithmic patterns
- ✅ Problem-solving strategies
- ✅ Debugging skills
- ✅ Optimization techniques

**Keep practicing and good luck in future contests!** 🚀
