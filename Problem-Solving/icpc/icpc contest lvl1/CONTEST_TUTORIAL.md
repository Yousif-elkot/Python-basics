# ICPC Contest Level 1 - Complete Tutorial Guide

This guide explains all problems from the contest with detailed explanations, techniques, and step-by-step solutions for beginners.

---

## Table of Contents
1. [Problem A: Book Stack Manager](#problem-a-book-stack-manager)
2. [Problem B: Task String Validator](#problem-b-task-string-validator)
3. [Problem C: Mathematical Series](#problem-c-mathematical-series)
4. [Problem D: Good Array Counter](#problem-d-good-array-counter)
5. [Problem E: Even-Odd Index Sum](#problem-e-even-odd-index-sum)
6. [Problem F: Palindrome Builder](#problem-f-palindrome-builder)

---

## Problem A: Book Stack Manager

### 📋 Problem Summary
You manage 3 types of books in stacks (LIFO - Last In First Out). You receive queries to either:
- Add a book: `+ type` - add a book at the current minute
- Take a book: `- type` - take the most recently added book of that type

### 🎯 Key Concepts
- **Data Structure**: Stack (LIFO - Last In First Out)
- **Python Implementation**: `deque` from collections (can use as stack)
- **Time Complexity**: O(1) per operation

### 💡 Solution Approach

**Step 1: Choose the right data structure**
- Stack is perfect because "most recent" = "last added" = LIFO
- Need 3 separate stacks, one for each book type

**Step 2: Track minutes**
- Each book added gets a timestamp (minute number)
- When taking a book, pop from stack and print its timestamp

**Step 3: Handle edge case**
- If stack is empty when taking, print `-1`

### 📝 Step-by-Step Implementation

```python
from collections import deque

def solve():
    n = int(input().strip())
    
    # Create 3 stacks (one for each book type)
    stacks = {
        1: deque(),  # Book type 1
        2: deque(),  # Book type 2
        3: deque()   # Book type 3
    }
    
    for minute in range(1, n + 1):
        query = input().strip().split()
        action = query[0]        # '+' or '-'
        book_type = int(query[1]) # 1, 2, or 3
        
        if action == '+':
            # Add book: store the minute number
            stacks[book_type].append(minute)
        else:  # action == '-'
            # Take book: get most recent (last added)
            if stacks[book_type]:
                book_id = stacks[book_type].pop()
                print(book_id)
            else:
                print(-1)  # Stack empty
```

### 🧪 Test Case Walkthrough
```
Input:
5
+ 1    → Add type 1 at minute 1
+ 1    → Add type 1 at minute 2
+ 2    → Add type 2 at minute 3
- 1    → Take type 1 (most recent = minute 2)
- 3    → Take type 3 (empty stack)

Output:
2
-1
```

**Visualization:**
```
Minute 1: Stack[1] = [1]
Minute 2: Stack[1] = [1, 2]
Minute 3: Stack[1] = [1, 2], Stack[2] = [3]
Minute 4: Stack[1] = [1] (popped 2, printed 2)
Minute 5: Stack[3] = [] (empty, print -1)
```

### 📚 Learning Points
- Stack = LIFO (Last In, First Out)
- `deque.append()` = push to stack
- `deque.pop()` = pop from stack (returns last element)
- Always check if stack is empty before popping

---

## Problem B: Task String Validator

### 📋 Problem Summary
Check if a binary string is a "Task string":
1. Get prime factors of string length (with repetition)
2. Split string into chunks based on prime factors
3. Convert each chunk from binary to decimal
4. Each decimal must be ≤ its chunk length

### 🎯 Key Concepts
- **Number Theory**: Prime factorization
- **String Manipulation**: Slicing
- **Base Conversion**: Binary to decimal
- **Time Complexity**: O(√n + k) where k = number of factors

### 💡 Solution Approach

**Step 1: Prime factorization**
- Find all prime factors of n (with repetition)
- Example: 6 → [2, 3], 12 → [2, 2, 3]

**Step 2: Split string into chunks**
- First chunk = length of first prime
- Second chunk = length of second prime, etc.

**Step 3: Validate each chunk**
- Convert binary chunk to decimal
- Check if decimal ≤ chunk length

### 📝 Step-by-Step Implementation

```python
def get_prime_factors(n):
    """
    Returns list of prime factors with repetition.
    Example: 12 → [2, 2, 3]
    """
    if n == 1:
        return []  # 1 has no prime factors
    
    factors = []
    d = 2  # Start with smallest prime
    
    # Try all divisors up to √n
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    # If n > 1, it's a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors

def solve():
    s = input().strip()
    n = len(s)
    
    # Get prime factors
    prime_factors = get_prime_factors(n)
    
    # Edge case: n=1 has no prime factors
    if not prime_factors:
        print("NO")
        return
    
    # Process each chunk
    pos = 0
    for prime in prime_factors:
        # Check if we have enough characters
        if pos + prime > n:
            break  # Ignore remaining
        
        # Extract chunk
        chunk = s[pos:pos + prime]
        
        # Convert binary to decimal
        decimal_value = int(chunk, 2)
        
        # Validate
        if decimal_value > prime:
            print("NO")
            return
        
        pos += prime
    
    print("YES")
```

### 🧪 Test Case Walkthrough

**Example 1:** `"100110"` (length 6)
```
Step 1: Prime factors of 6 = [2, 3]
Step 2: Split string:
  - Chunk 1 (length 2): "10"
  - Chunk 2 (length 3): "011"
Step 3: Convert and check:
  - "10" → 2, check 2 ≤ 2 ✓
  - "011" → 3, check 3 ≤ 3 ✓
Result: YES
```

**Example 2:** `"101100"` (length 6)
```
Step 1: Prime factors of 6 = [2, 3]
Step 2: Split string:
  - Chunk 1 (length 2): "10"
  - Chunk 2 (length 3): "110"
Step 3: Convert and check:
  - "10" → 2, check 2 ≤ 2 ✓
  - "110" → 6, check 6 ≤ 3 ✗
Result: NO
```

### 📚 Learning Points
- Prime factorization: try divisors from 2 to √n
- Include multiplicities: 12 = 2 × 2 × 3 → [2, 2, 3]
- Binary to decimal: `int("101", 2)` → 5
- String slicing: `s[start:end]` (end is exclusive)

---

## Problem C: Mathematical Series

### 📋 Problem Summary
Calculate a mathematical formula involving sum of squares and sum of integers.
Given n, compute: `(2 × Σi² × (Σi)²) / (2 × Σi² × Σi)`

Where Σi² = 1² + 2² + ... + n² and Σi = 1 + 2 + ... + n

### 🎯 Key Concepts
- **Math Formulas**: Sum of integers, sum of squares
- **Simplification**: Algebraic reduction
- **Time Complexity**: O(1)

### 💡 Solution Approach

**Step 1: Know the formulas**
```
Sum of integers: Σi = n(n+1)/2
Sum of squares: Σi² = n(n+1)(2n+1)/6
```

**Step 2: Simplify the expression**
```
Original: (2 × Σi² × (Σi)²) / (2 × Σi² × Σi)
Cancel 2 × Σi²: (Σi)² / Σi
Simplify: Σi
Result: n(n+1)/2
```

**Key insight**: The complex formula simplifies to just the sum of integers!

### 📝 Step-by-Step Implementation

```python
def solve():
    n = int(input())
    
    # Formula for sum of integers: n(n+1)/2
    def sum_of_integers(n):
        return (n * (n + 1)) // 2
    
    # Formula for sum of squares: n(n+1)(2n+1)/6
    def sum_of_squares(n):
        return (n * (n + 1) * (2 * n + 1)) // 6
    
    # Calculate the full formula (before simplification)
    def calculate_formula(n):
        sum_i = sum_of_integers(n)
        sum_i2 = sum_of_squares(n)
        
        numerator = 2 * sum_i2 * (sum_i ** 2)
        denominator = 2 * sum_i2 * sum_i
        
        return numerator // denominator
    
    # But we know it simplifies to just sum_of_integers!
    result = sum_of_integers(n)
    print(result)
```

### 🧪 Test Case Walkthrough

**Example:** n = 6
```
Sum of integers: 6(6+1)/2 = 6×7/2 = 21
Sum of squares: 6(6+1)(12+1)/6 = 6×7×13/6 = 91

Full formula:
  Numerator: 2 × 91 × 21² = 2 × 91 × 441 = 80,262
  Denominator: 2 × 91 × 21 = 3,822
  Result: 80,262 / 3,822 = 21

Simplified: n(n+1)/2 = 21 ✓
```

### 📚 Learning Points
- Mathematical formulas can often be simplified before coding
- Sum of 1 to n: `n(n+1)/2`
- Sum of squares: `n(n+1)(2n+1)/6`
- Use integer division `//` to avoid floating point errors

---

## Problem D: Good Array Counter

### 📋 Problem Summary
Count arrays of length n where:
- Each element is between 1 and 6
- Sum of all elements equals 8

### 🎯 Key Concepts
- **Dynamic Programming**: Count ways to reach target sum
- **Memoization**: Cache results to avoid recomputation
- **Combinatorics**: Counting problem
- **Time Complexity**: O(n × 8 × 6) = O(n)

### 💡 Solution Approach

**Step 1: Define the recursive function**
- `count_ways(positions_left, sum_remaining)` = number of ways
- Base case: 0 positions left, 0 sum → 1 way
- Base case: 0 positions left, non-zero sum → 0 ways

**Step 2: Try all possible values**
- For current position, try values 1-6
- Recursively count for remaining positions and sum

**Step 3: Use memoization**
- Cache results for (positions, sum) pairs
- Avoid recalculating the same state

### 📝 Step-by-Step Implementation

```python
def solve(n):
    # Dictionary to store computed results
    memo = {}
    
    def count_ways(pos, remaining_sum):
        """
        Count ways to fill 'pos' positions with sum 'remaining_sum'
        where each value is 1-6
        """
        # Base cases
        if pos == 0:
            return 1 if remaining_sum == 0 else 0
        
        if remaining_sum <= 0:
            return 0
        
        # Check if already computed
        if (pos, remaining_sum) in memo:
            return memo[(pos, remaining_sum)]
        
        # Try all values 1-6
        result = 0
        for val in range(1, 7):
            if remaining_sum - val >= 0:
                result += count_ways(pos - 1, remaining_sum - val)
        
        # Cache the result
        memo[(pos, remaining_sum)] = result
        return result
    
    return count_ways(n, 8)
```

### 🧪 Test Case Walkthrough

**Example 1:** n = 2
```
Need: sum = 8, length = 2

Possible arrays:
[6,2] ✓
[5,3] ✓
[4,4] ✓
[3,5] ✓
[2,6] ✓

Total: 5 ways
```

**Example 2:** n = 8
```
Need: sum = 8, length = 8
Each element must be ≤ 6
To reach sum 8 with 8 elements:
Minimum sum = 8 × 1 = 8

Only way: [1,1,1,1,1,1,1,1]
Total: 1 way
```

**Recursion tree for n=2:**
```
count_ways(2, 8)
├─ val=1: count_ways(1, 7) → 1 way [1,7] but 7>6 so 0
├─ val=2: count_ways(1, 6) → 1 way [2,6] ✓
├─ val=3: count_ways(1, 5) → 1 way [3,5] ✓
├─ val=4: count_ways(1, 4) → 1 way [4,4] ✓
├─ val=5: count_ways(1, 3) → 1 way [5,3] ✓
└─ val=6: count_ways(1, 2) → 1 way [6,2] ✓
Total: 5 ways
```

### 📚 Learning Points
- **Memoization** = caching recursive results
- Use dictionary with tuple keys: `memo[(pos, sum)]`
- Try all possibilities and sum them up
- Base cases are crucial for recursion

---

## Problem E: Even-Odd Index Sum

### 📋 Problem Summary
Given an array, answer queries: for range [l, r], calculate:
`(sum of elements at EVEN indices) - (sum of elements at ODD indices)`

**Important**: Indices are based on ORIGINAL array position, not subarray!

### 🎯 Key Concepts
- **Prefix Sum**: Precompute cumulative sums for O(1) queries
- **Array Indexing**: 0-indexed (even: 0,2,4,... odd: 1,3,5,...)
- **Time Complexity**: O(n) preprocessing, O(1) per query

### 💡 Solution Approach

**Step 1: Build two prefix sum arrays**
- `prefix_even[i]` = sum of all even-indexed elements from 0 to i
- `prefix_odd[i]` = sum of all odd-indexed elements from 0 to i

**Step 2: Answer queries in O(1)**
- For range [l, r]:
  - `even_sum = prefix_even[r] - prefix_even[l-1]`
  - `odd_sum = prefix_odd[r] - prefix_odd[l-1]`
  - Result = `even_sum - odd_sum`

**Common mistake**: Checking if VALUE is even/odd instead of INDEX!

### 📝 Step-by-Step Implementation

```python
def solve():
    n = int(input().strip())
    A = list(map(int, input().strip().split()))
    
    # Build prefix sum arrays
    prefix_even = [0] * n
    prefix_odd = [0] * n
    
    for i in range(n):
        if i == 0:
            # First element
            if i % 2 == 0:  # Check INDEX, not value!
                prefix_even[i] = A[i]
                prefix_odd[i] = 0
            else:
                prefix_even[i] = 0
                prefix_odd[i] = A[i]
        else:
            # Copy previous values
            prefix_even[i] = prefix_even[i - 1]
            prefix_odd[i] = prefix_odd[i - 1]
            
            # Add current element to appropriate sum
            if i % 2 == 0:  # Even INDEX
                prefix_even[i] += A[i]
            else:  # Odd INDEX
                prefix_odd[i] += A[i]
    
    # Answer queries
    q = int(input().strip())
    for _ in range(q):
        l, r = map(int, input().strip().split())
        
        # Calculate sums for range [l, r]
        even_sum = prefix_even[r]
        if l > 0:
            even_sum -= prefix_even[l - 1]
        
        odd_sum = prefix_odd[r]
        if l > 0:
            odd_sum -= prefix_odd[l - 1]
        
        result = even_sum - odd_sum
        print(result)
```

### 🧪 Test Case Walkthrough

**Array:** `[-2, 0, 4, -1]` (indices: 0, 1, 2, 3)

**Build prefix sums:**
```
i=0 (even): A[0]=-2
  prefix_even = [-2, ?, ?, ?]
  prefix_odd  = [0, ?, ?, ?]

i=1 (odd): A[1]=0
  prefix_even = [-2, -2, ?, ?]
  prefix_odd  = [0, 0, ?, ?]

i=2 (even): A[2]=4
  prefix_even = [-2, -2, 2, ?]
  prefix_odd  = [0, 0, 0, ?]

i=3 (odd): A[3]=-1
  prefix_even = [-2, -2, 2, 2]
  prefix_odd  = [0, 0, 0, -1]
```

**Query 1: l=0, r=3**
```
even_sum = prefix_even[3] = 2
odd_sum = prefix_odd[3] = -1
result = 2 - (-1) = 3 ✓
```

**Query 2: l=1, r=2**
```
even_sum = prefix_even[2] - prefix_even[0] = 2 - (-2) = 4
odd_sum = prefix_odd[2] - prefix_odd[0] = 0 - 0 = 0
result = 4 - 0 = 4 ✓
```

### 📚 Learning Points
- **Prefix sum formula**: `sum[l..r] = prefix[r] - prefix[l-1]`
- Check if **INDEX** is even/odd, not the value!
- Build separate prefix arrays for different criteria
- Handle boundary: when l=0, don't subtract anything

---

## Problem F: Palindrome Builder

### 📋 Problem Summary
Given a string with `?` characters, replace them to form:
1. A valid palindrome
2. The lexicographically smallest palindrome
3. Return `-1` if impossible

### 🎯 Key Concepts
- **Two Pointers**: Compare mirror positions
- **Palindrome Property**: s[i] must equal s[n-1-i]
- **Greedy**: Choose 'a' when possible (smallest letter)
- **Time Complexity**: O(n)

### 💡 Solution Approach

**Step 1: Use two pointers**
- Left pointer at start, right pointer at end
- These are mirror positions in a palindrome

**Step 2: Handle 4 cases for each pair**
1. Both `?` → set both to 'a' (greedy)
2. Left `?` → copy right character
3. Right `?` → copy left character
4. Both letters → must match, else impossible

**Step 3: Handle middle (odd length)**
- If string has odd length and middle is `?`, set to 'a'

### 📝 Step-by-Step Implementation

```python
def solve():
    s = list(input().strip())  # Convert to list for modification
    n = len(s)
    
    left = 0
    right = n - 1
    
    # Process pairs from both ends
    while left < right:
        if s[left] == '?' and s[right] == '?':
            # Both are ?, choose smallest letter
            s[left] = 'a'
            s[right] = 'a'
        
        elif s[left] == '?':
            # Left is ?, copy from right
            s[left] = s[right]
        
        elif s[right] == '?':
            # Right is ?, copy from left
            s[right] = s[left]
        
        else:
            # Both are letters, must match
            if s[left] != s[right]:
                print(-1)
                return
        
        left += 1
        right -= 1
    
    # Handle middle character (if odd length)
    if n % 2 == 1 and s[n // 2] == '?':
        s[n // 2] = 'a'
    
    result = ''.join(s)
    print(result)
```

### 🧪 Test Case Walkthrough

**Example 1:** `"a?z?"`
```
Initial: a ? z ?
         ↑     ↑
       left  right

Step 1: Compare positions 0 and 3
  s[0]='a', s[3]='?' → copy 'a' to position 3
  Result: "a?za"

Step 2: Compare positions 1 and 2
  s[1]='?', s[2]='z' → copy 'z' to position 1
  Result: "azza"

Final: "azza" ✓
```

**Example 2:** `"aba"`
```
Initial: a b a
         ↑   ↑
       left right

Step 1: Compare positions 0 and 2
  s[0]='a', s[2]='a' → match! ✓
  
Step 2: left=1, right=1 → stop (left < right is false)

Middle: position 1 is 'b', not '?' → leave it

Final: "aba" ✓
```

**Example 3 (impossible):** `"ab?cd"`
```
Initial: a b ? c d
         ↑       ↑
       left    right

Step 1: Compare positions 0 and 4
  s[0]='a', s[4]='d' → 'a' ≠ 'd' → IMPOSSIBLE
  
Return: -1 ✗
```

### 📚 Learning Points
- **Two pointers technique**: Start from both ends, move inward
- **Strings are immutable**: Convert to list to modify
- **Greedy choice**: Always pick 'a' when you have freedom
- **Mirror positions**: In palindrome, `s[i] = s[n-1-i]`
- **Edge case**: Handle middle character for odd-length strings

---

## 🎓 General Tips for Competitive Programming

### Problem-Solving Strategy
1. **Read carefully**: Understand exactly what's being asked
2. **Identify pattern**: What algorithm/data structure fits?
3. **Think of edge cases**: Empty input, size 1, maximum size
4. **Start simple**: Write brute force first, then optimize
5. **Test with examples**: Trace through given test cases

### Common Techniques Used
- **Stack/Queue**: When order matters (LIFO/FIFO)
- **Prefix Sum**: When you have multiple range queries
- **Two Pointers**: When comparing pairs or finding patterns
- **Dynamic Programming**: Counting or optimization problems
- **Greedy**: When local optimal choice leads to global optimal

### Debugging Tips
- Print intermediate values to trace execution
- Test edge cases: n=1, n=0, maximum n
- Check array bounds: don't access out of range
- Verify base cases in recursion
- Make sure data types match (int vs float)

### Python-Specific Tips
- Use `sys.stdin.readline` for faster input
- Convert strings to lists to modify them
- Use `//` for integer division, not `/`
- `deque` is better than list for stack/queue operations
- Dictionary with tuple keys for memoization

---

## 📊 Complexity Cheat Sheet

| Problem | Time Complexity | Space Complexity | Key Technique |
|---------|----------------|------------------|---------------|
| A | O(n) | O(n) | Stack |
| B | O(√n + k) | O(k) | Prime Factorization |
| C | O(1) | O(1) | Math Formula |
| D | O(n × target) | O(n × target) | DP + Memoization |
| E | O(n + q) | O(n) | Prefix Sum |
| F | O(n) | O(n) | Two Pointers |

Where:
- n = input size
- k = number of prime factors
- q = number of queries
- target = 8 (fixed in problem D)

---

## 🚀 Practice Recommendations

After understanding these problems:
1. **Recode from scratch** without looking at solutions
2. **Modify the problems**: Change constraints, add features
3. **Practice similar problems** on Codeforces/LeetCode
4. **Time yourself**: Try to solve within contest time limits
5. **Learn from mistakes**: Keep a log of bugs and how you fixed them

---

Good luck with your competitive programming journey! 🎯
