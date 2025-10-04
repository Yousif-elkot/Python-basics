#!/usr/bin/env python3
"""
Interactive Hash Table Tutorial - Day 5
Learn hash tables through hands-on examples and experiments

Run this file to go through 6 interactive lessons:
1. Introduction to Hash Tables
2. Hash Functions
3. Collision Handling
4. Python Dictionary Deep Dive
5. Common Patterns
6. Performance Analysis
"""

import sys
from collections import defaultdict, Counter
from typing import List, Dict, Any


def clear_screen():
    """Clear the screen (works on most terminals)"""
    print("\n" * 2)


def wait_for_enter():
    """Wait for user to press Enter"""
    input("\n➤ Press Enter to continue...")


def print_header(title: str):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60 + "\n")


def print_section(title: str):
    """Print a section header"""
    print(f"\n{'─' * 60}")
    print(f"📚 {title}")
    print('─' * 60)


# ============================================================================
# LESSON 1: Introduction to Hash Tables
# ============================================================================

def lesson_1_intro():
    """Introduction to Hash Tables - The O(1) Superpower"""
    print_header("LESSON 1: Introduction to Hash Tables")
    
    print("Welcome to Hash Tables! 🗂️")
    print("\nHash tables are one of the most important data structures in programming.")
    print("They give us O(1) average case lookup, insert, and delete operations!")
    
    wait_for_enter()
    
    print_section("The Problem: Slow Lookups in Lists")
    
    print("\n🐢 LINEAR SEARCH - O(n) time:")
    print("Let's search for a name in a list...")
    
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry"]
    search_name = "Henry"
    
    print(f"\nList: {names}")
    print(f"Searching for: '{search_name}'")
    
    # Demonstrate linear search
    comparisons = 0
    for i, name in enumerate(names):
        comparisons += 1
        print(f"  Step {comparisons}: Checking '{name}'...", end="")
        if name == search_name:
            print(f" ✅ FOUND at index {i}!")
            break
        else:
            print(" ❌")
    
    print(f"\n📊 Total comparisons: {comparisons}")
    print(f"Time complexity: O(n) - might check every element!")
    
    wait_for_enter()
    
    print_section("The Solution: Hash Tables - O(1) time")
    
    print("\n⚡ HASH TABLE LOOKUP - O(1) average time:")
    print("Let's use a hash table (Python dict) instead...")
    
    # Create hash table
    names_dict = {name: True for name in names}
    
    print(f"\nHash Table: {list(names_dict.keys())}")
    print(f"Searching for: '{search_name}'")
    
    print(f"\n  Step 1: Hash '{search_name}' to get index")
    print(f"  Step 2: Check that index directly ✅ FOUND!")
    
    print(f"\n📊 Total comparisons: ~1")
    print(f"Time complexity: O(1) average - direct access!")
    
    wait_for_enter()
    
    print_section("Key Insight")
    
    print("""
The Magic of Hash Tables:
┌─────────────────────────────────────────────────────────┐
│  Instead of searching through items one by one...       │
│  We COMPUTE where to look directly!                     │
│                                                          │
│  key → hash_function(key) → array_index → value         │
└─────────────────────────────────────────────────────────┘

Example:
  "Henry" → hash("Henry") → 7 → Look at index 7 directly!
  
No searching needed! 🎯
    """)
    
    wait_for_enter()
    
    print_section("Real-World Applications")
    
    applications = [
        ("🔍 Database Indexing", "Find records by ID instantly"),
        ("🌐 DNS Lookup", "Domain name → IP address"),
        ("💾 Caching", "Store computed results for quick retrieval"),
        ("📊 Frequency Counting", "Count occurrences (word counter)"),
        ("🔄 Deduplication", "Remove duplicates efficiently"),
        ("👥 User Sessions", "Track logged-in users"),
    ]
    
    print("\nHash tables power many everyday technologies:\n")
    for use_case, description in applications:
        print(f"  {use_case}")
        print(f"    └─ {description}\n")
    
    wait_for_enter()
    
    print("\n✅ Lesson 1 Complete!")
    print("\nKey Takeaways:")
    print("  • Hash tables provide O(1) average case operations")
    print("  • They compute array indices from keys using hash functions")
    print("  • Used everywhere in real-world applications")


# ============================================================================
# LESSON 2: Hash Functions
# ============================================================================

def lesson_2_hash_functions():
    """Understanding Hash Functions"""
    print_header("LESSON 2: Hash Functions")
    
    print("A hash function converts a key into an array index.")
    print("It's the secret sauce that makes hash tables fast! 🧪")
    
    wait_for_enter()
    
    print_section("Simple Hash Function Example")
    
    def simple_hash(key: str, table_size: int) -> int:
        """Convert string to index by summing character codes"""
        total = sum(ord(char) for char in key)
        return total % table_size
    
    print("\nOur simple hash function:")
    print("  1. Sum up ASCII values of all characters")
    print("  2. Modulo by table size (to fit in array)")
    print("\nFormula: hash(key) = sum(ord(char) for char in key) % table_size")
    
    wait_for_enter()
    
    # Demonstrate hashing
    table_size = 10
    words = ["cat", "dog", "bird", "fish", "lion"]
    
    print(f"\n📝 Let's hash some words (table size = {table_size}):\n")
    
    for word in words:
        char_values = [ord(c) for c in word]
        total = sum(char_values)
        index = simple_hash(word, table_size)
        
        print(f"'{word}':")
        print(f"  ASCII values: {char_values}")
        print(f"  Sum: {total}")
        print(f"  Index: {total} % {table_size} = {index}")
        print()
    
    wait_for_enter()
    
    print_section("Properties of Good Hash Functions")
    
    print("""
A good hash function should be:

1. ✅ DETERMINISTIC
   └─ Same input always produces same output
   └─ hash("cat") always gives same index

2. ✅ UNIFORM DISTRIBUTION
   └─ Spreads keys evenly across array
   └─ Avoids clustering in one area

3. ✅ FAST TO COMPUTE
   └─ Should be O(1) operation
   └─ Complex math defeats the purpose!

4. ✅ MINIMIZES COLLISIONS
   └─ Different keys should hash to different indices
   └─ (Collisions are inevitable, but should be rare)
    """)
    
    wait_for_enter()
    
    print_section("Collision Example")
    
    print("\n⚠️ COLLISION: When two keys hash to same index\n")
    
    # Find a collision
    word1, word2 = "listen", "silent"  # These are anagrams!
    hash1 = simple_hash(word1, table_size)
    hash2 = simple_hash(word2, table_size)
    
    print(f"'{word1}' → hash = {hash1}")
    print(f"'{word2}' → hash = {hash2}")
    
    if hash1 == hash2:
        print("\n💥 COLLISION! Both hash to same index!")
        print("We need a strategy to handle this...")
    else:
        print("\n✅ No collision in this case.")
    
    wait_for_enter()
    
    print("\n✅ Lesson 2 Complete!")
    print("\nKey Takeaways:")
    print("  • Hash functions convert keys to array indices")
    print("  • Good hash functions are deterministic and uniform")
    print("  • Collisions happen when different keys hash to same index")
    print("  • We need strategies to handle collisions (next lesson!)")


# ============================================================================
# LESSON 3: Collision Handling
# ============================================================================

def lesson_3_collisions():
    """Handling Collisions with Chaining"""
    print_header("LESSON 3: Collision Handling")
    
    print("When two keys hash to the same index, we have a COLLISION.")
    print("Let's learn how to handle them! 🔧")
    
    wait_for_enter()
    
    print_section("Strategy 1: Chaining (Python's Approach)")
    
    print("""
CHAINING: Store multiple items at the same index using a list.

Array Structure:
┌─────────┬────────────────────────────┐
│ Index 0 │ → ["apple", 3]             │
│ Index 1 │ → ["banana", 5] → ["berry", 2] │  ← Collision!
│ Index 2 │ → ["cherry", 7]            │
│ Index 3 │ (empty)                    │
└─────────┴────────────────────────────┘

Each array slot holds a LIST of key-value pairs.
When collision occurs, just append to the list!
    """)
    
    wait_for_enter()
    
    print_section("Chaining in Action")
    
    # Demonstrate chaining
    table_size = 5
    hash_table = [[] for _ in range(table_size)]
    
    items = [("apple", 10), ("banana", 20), ("cherry", 30), ("berry", 40)]
    
    def simple_hash_demo(key: str) -> int:
        return sum(ord(c) for c in key) % table_size
    
    print(f"\nInserting items into hash table (size {table_size}):\n")
    
    for key, value in items:
        index = simple_hash_demo(key)
        hash_table[index].append((key, value))
        print(f"'{key}' → hash = {index}")
        print(f"  Table[{index}] = {hash_table[index]}")
        
        if len(hash_table[index]) > 1:
            print("  ⚠️ Collision handled by chaining!")
        print()
    
    wait_for_enter()
    
    print_section("Searching with Chaining")
    
    print("\nTo search for a key:")
    print("  1. Hash the key to get index")
    print("  2. Look at that index's list")
    print("  3. Linear search through the list")
    
    search_key = "berry"
    search_index = simple_hash_demo(search_key)
    
    print(f"\nSearching for '{search_key}':")
    print(f"  Step 1: hash('{search_key}') = {search_index}")
    print(f"  Step 2: Look at Table[{search_index}] = {hash_table[search_index]}")
    print(f"  Step 3: Search the list...")
    
    for i, (k, v) in enumerate(hash_table[search_index]):
        print(f"    Check #{i+1}: '{k}'...", end="")
        if k == search_key:
            print(f" ✅ Found! Value = {v}")
            break
        else:
            print(" ❌")
    
    wait_for_enter()
    
    print_section("Strategy 2: Open Addressing (Alternative)")
    
    print("""
OPEN ADDRESSING: If slot is full, try the next slot.

Linear Probing:
  If index N is full, try N+1, then N+2, N+3...
  
Example:
  hash("cat") = 3 → Table[3] is full
  Try Table[4] → full
  Try Table[5] → empty! Store here.

Pros: No lists needed, cache-friendly
Cons: Can cause clustering

Python uses CHAINING, not open addressing.
    """)
    
    wait_for_enter()
    
    print_section("Load Factor")
    
    print("""
LOAD FACTOR = number_of_items / table_size

Examples:
  • 7 items, size 10 → load factor = 0.7
  • 15 items, size 10 → load factor = 1.5 (too high!)
  
Rules of thumb:
  • < 0.7: Good performance ✅
  • > 0.7: Should resize (make table bigger)
  • > 1.0: Guaranteed collisions, getting slow ⚠️

Python dicts resize automatically when load factor > 0.66
    """)
    
    wait_for_enter()
    
    print("\n✅ Lesson 3 Complete!")
    print("\nKey Takeaways:")
    print("  • Collisions are handled by chaining (lists) or open addressing")
    print("  • Chaining: store multiple items at same index in a list")
    print("  • Load factor tells us when to resize the table")
    print("  • Keep load factor < 0.7 for good performance")


# ============================================================================
# LESSON 4: Python Dictionary Deep Dive
# ============================================================================

def lesson_4_python_dict():
    """Master Python's Built-in Hash Table"""
    print_header("LESSON 4: Python Dictionary Deep Dive")
    
    print("Python's dict is a highly optimized hash table.")
    print("Let's master all the ways to use it! 🐍")
    
    wait_for_enter()
    
    print_section("Dictionary Basics")
    
    print("\n1️⃣ Creating Dictionaries:\n")
    
    # Different ways to create
    dict1 = {"name": "Alice", "age": 25, "city": "NYC"}
    dict2 = dict(name="Bob", age=30, city="LA")
    dict3 = dict([("name", "Charlie"), ("age", 35)])
    
    print(f"  Literal syntax: {dict1}")
    print(f"  dict() function: {dict2}")
    print(f"  From list of tuples: {dict3}")
    
    wait_for_enter()
    
    print("\n2️⃣ Accessing Values:\n")
    
    person = {"name": "Alice", "age": 25}
    
    print(f"  person['name'] = {person['name']}")
    print(f"  person.get('age') = {person.get('age')}")
    print(f"  person.get('job', 'Unknown') = {person.get('job', 'Unknown')}")
    print("\n  ⚠️ person['job'] would raise KeyError!")
    print("  ✅ person.get('job', default) returns default instead")
    
    wait_for_enter()
    
    print("\n3️⃣ Modifying Dictionaries:\n")
    
    print("  person['age'] = 26  # Update existing")
    person['age'] = 26
    print(f"  Result: {person}")
    
    print("\n  person['job'] = 'Engineer'  # Add new key")
    person['job'] = 'Engineer'
    print(f"  Result: {person}")
    
    print("\n  del person['city']  # Would delete if existed")
    print("  person.pop('job', None)  # Safe delete")
    person.pop('job', None)
    print(f"  Result: {person}")
    
    wait_for_enter()
    
    print_section("Checking Existence")
    
    print("\n4️⃣ Check if Key Exists:\n")
    
    print(f"  'name' in person → {' name' in person}")
    print(f"  'job' in person → {'job' in person}")
    print("\n  Always check before accessing to avoid KeyError!")
    
    wait_for_enter()
    
    print_section("Iteration Patterns")
    
    print("\n5️⃣ Iterating Through Dictionaries:\n")
    
    scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
    
    print("  # Iterate over keys:")
    print("  for name in scores:")
    for name in scores:
        print(f"    {name}")
    
    print("\n  # Iterate over values:")
    print("  for score in scores.values():")
    for score in scores.values():
        print(f"    {score}")
    
    print("\n  # Iterate over key-value pairs:")
    print("  for name, score in scores.items():")
    for name, score in scores.items():
        print(f"    {name}: {score}")
    
    wait_for_enter()
    
    print_section("Advanced: defaultdict")
    
    print("\n6️⃣ Using defaultdict (no KeyError!):\n")
    
    from collections import defaultdict
    
    print("  # Regular dict - KeyError risk:")
    print("  counts = {}")
    print("  counts['apple'] += 1  # ❌ KeyError!\n")
    
    print("  # defaultdict - auto-creates default value:")
    counts = defaultdict(int)
    print("  counts = defaultdict(int)")
    print("  counts['apple'] += 1  # ✅ Works! Defaults to 0")
    counts['apple'] += 1
    counts['apple'] += 1
    counts['banana'] += 1
    print(f"  Result: {dict(counts)}")
    
    wait_for_enter()
    
    print_section("Advanced: Counter")
    
    print("\n7️⃣ Using Counter (specialized for counting):\n")
    
    from collections import Counter
    
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    counter = Counter(words)
    
    print(f"  words = {words}")
    print(f"  counter = Counter(words)")
    print(f"  Result: {counter}")
    print(f"\n  counter.most_common(2) = {counter.most_common(2)}")
    print("  → Returns top 2 most frequent items!")
    
    wait_for_enter()
    
    print("\n✅ Lesson 4 Complete!")
    print("\nKey Takeaways:")
    print("  • Use .get(key, default) for safe access")
    print("  • 'key in dict' checks existence in O(1)")
    print("  • .items() for iterating key-value pairs")
    print("  • defaultdict prevents KeyError")
    print("  • Counter is perfect for frequency counting")


# ============================================================================
# LESSON 5: Common Patterns
# ============================================================================

def lesson_5_patterns():
    """Common Hash Table Patterns in Practice"""
    print_header("LESSON 5: Common Hash Table Patterns")
    
    print("Let's see how hash tables solve real problems! 💼")
    
    wait_for_enter()
    
    print_section("Pattern 1: Frequency Counter")
    
    print("\n🎯 Problem: Count how many times each word appears\n")
    
    text = "the cat and the dog and the bird"
    words = text.split()
    
    print(f"Text: '{text}'")
    print(f"Words: {words}\n")
    
    # Method 1: Manual
    print("Method 1: Manual counting with dict")
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    print(f"Result: {freq}\n")
    
    # Method 2: defaultdict
    print("Method 2: defaultdict (cleaner)")
    freq2 = defaultdict(int)
    for word in words:
        freq2[word] += 1
    print(f"Result: {dict(freq2)}\n")
    
    # Method 3: Counter
    print("Method 3: Counter (best)")
    freq3 = Counter(words)
    print(f"Result: {freq3}")
    
    wait_for_enter()
    
    print_section("Pattern 2: Grouping")
    
    print("\n🎯 Problem: Group items by category\n")
    
    students = [
        {"name": "Alice", "grade": "A"},
        {"name": "Bob", "grade": "B"},
        {"name": "Charlie", "grade": "A"},
        {"name": "David", "grade": "C"},
        {"name": "Eve", "grade": "B"},
    ]
    
    print("Students:")
    for s in students:
        print(f"  {s}")
    
    print("\nGrouping by grade...")
    groups = defaultdict(list)
    for student in students:
        groups[student['grade']].append(student['name'])
    
    print("\nResult:")
    for grade, names in sorted(groups.items()):
        print(f"  Grade {grade}: {names}")
    
    wait_for_enter()
    
    print_section("Pattern 3: Deduplication")
    
    print("\n🎯 Problem: Remove duplicates from a list\n")
    
    numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6, 4]
    print(f"Original: {numbers}")
    
    # Using set (which is also a hash table!)
    unique = list(set(numbers))
    print(f"Unique (unordered): {unique}")
    
    # Preserving order
    seen = {}
    unique_ordered = []
    for num in numbers:
        if num not in seen:
            seen[num] = True
            unique_ordered.append(num)
    print(f"Unique (ordered): {unique_ordered}")
    
    wait_for_enter()
    
    print_section("Pattern 4: Caching (Memoization)")
    
    print("\n🎯 Problem: Cache expensive function results\n")
    
    cache = {}
    call_count = [0]  # Use list to avoid global issues
    
    def expensive_function(n: int) -> int:
        """Simulate expensive calculation (e.g., API call, database query)"""
        call_count[0] += 1
        # In real life, this might be a slow database query or API call
        return n * n
    
    def cached_function(n: int) -> int:
        """Cached version - much faster for repeated calls"""
        if n in cache:
            print(f"  Cache HIT for {n}! ⚡")
            return cache[n]
        
        print(f"  Cache MISS for {n}. Computing... 🔄")
        result = expensive_function(n)
        cache[n] = result
        return result
    
    print("Calling cached_function multiple times:\n")
    for i in [5, 3, 5, 7, 3, 5]:
        result = cached_function(i)
        print(f"    cached_function({i}) = {result}\n")
    
    print(f"Total expensive function calls: {call_count[0]}")
    print(f"Calls saved by caching: {6 - call_count[0]}")
    
    wait_for_enter()
    
    print_section("Pattern 5: Two-Sum Problem")
    
    print("\n🎯 Problem: Find two numbers that add up to target\n")
    
    numbers = [2, 7, 11, 15]
    target = 9
    
    print(f"Numbers: {numbers}")
    print(f"Target: {target}")
    print("\nNaive approach: Try all pairs - O(n²)")
    print("Hash table approach: O(n) time! ✨\n")
    
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        print(f"  Checking {num}:")
        print(f"    Need {complement} to reach {target}")
        
        if complement in seen:
            print(f"    ✅ Found! {complement} + {num} = {target}")
            print(f"    Indices: [{seen[complement]}, {i}]")
            break
        
        seen[num] = i
        print(f"    Added {num} to seen dict")
    
    wait_for_enter()
    
    print("\n✅ Lesson 5 Complete!")
    print("\nKey Takeaways:")
    print("  • Frequency counting: Use Counter or defaultdict(int)")
    print("  • Grouping: Use defaultdict(list)")
    print("  • Deduplication: Use set or dict for seen items")
    print("  • Caching: Store results in dict for O(1) lookup")
    print("  • Many O(n²) problems become O(n) with hash tables!")


# ============================================================================
# LESSON 6: Performance Analysis
# ============================================================================

def lesson_6_performance():
    """Understanding Hash Table Performance"""
    print_header("LESSON 6: Performance Analysis")
    
    print("Let's analyze when hash tables shine (and when they don't)! ⚡")
    
    wait_for_enter()
    
    print_section("Time Complexity Summary")
    
    print("""
Hash Table Operations:
┌────────────┬──────────────┬────────────┐
│ Operation  │ Average Case │ Worst Case │
├────────────┼──────────────┼────────────┤
│ Insert     │     O(1)     │    O(n)    │
│ Search     │     O(1)     │    O(n)    │
│ Delete     │     O(1)     │    O(n)    │
│ Space      │     O(n)     │    O(n)    │
└────────────┴──────────────┴────────────┘

Average case: Keys distributed uniformly (good hash function)
Worst case: All keys collide (bad hash function or adversarial input)
    """)
    
    wait_for_enter()
    
    print_section("Comparison with Other Structures")
    
    print("""
Search Operation Comparison:
┌──────────────────┬────────────┬──────────┬────────────┐
│ Data Structure   │   Search   │  Insert  │   Sorted?  │
├──────────────────┼────────────┼──────────┼────────────┤
│ Array/List       │    O(n)    │   O(1)*  │     No     │
│ Sorted Array     │  O(log n)  │   O(n)   │    Yes     │
│ Binary Search    │  O(log n)  │ O(log n) │    Yes     │
│ Tree (BST)       │            │          │            │
│ Hash Table       │    O(1)    │   O(1)   │     No     │
└──────────────────┴────────────┴──────────┴────────────┘
* Append only, insert at position is O(n)

Hash tables win for pure lookup speed! 🏆
But you lose ordering information.
    """)
    
    wait_for_enter()
    
    print_section("When to Use Hash Tables")
    
    print("""
✅ USE HASH TABLE WHEN:

  • Need fast lookup by key (O(1))
  • Counting frequencies
  • Checking existence/membership
  • Removing duplicates
  • Caching computed results
  • Grouping data by categories
  • Order doesn't matter
  • Keys are hashable (immutable)

❌ DON'T USE HASH TABLE WHEN:

  • Need sorted/ordered data → Use BST or sorted list
  • Need range queries → Use BST
  • Need minimum/maximum often → Use heap
  • Keys aren't hashable → Use list/array
  • Memory is extremely limited → Hash table overhead
  • Need deterministic worst-case → BST guarantees O(log n)
    """)
    
    wait_for_enter()
    
    print_section("Real-World Performance Tips")
    
    print("""
🎯 Optimization Tips:

1. Choose good initial size
   └─ If you know you'll have 100 items, start with size ~150
   └─ Avoids resizing (expensive operation)

2. Use appropriate default value
   └─ defaultdict(int) for counters
   └─ defaultdict(list) for grouping

3. Consider memory overhead
   └─ Dicts use more memory than lists
   └─ Trade space for time

4. Beware of worst-case
   └─ Adversarial input can cause all collisions
   └─ Python's hash is designed to resist this

5. Keys must be immutable
   └─ ✅ strings, numbers, tuples
   └─ ❌ lists, dicts, sets
    """)
    
    wait_for_enter()
    
    print_section("Python Dict Internals (Bonus)")
    
    print("""
Fun Facts about Python's dict:

• Python 3.7+: Dicts maintain insertion order! 🎉
• Implemented in C for maximum speed
• Uses open addressing with random probing (not chaining!)
• Resizes when load factor > 0.66
• Minimum size: 8 slots
• Grows by factor of ~2-4x when resizing
• Hash function includes randomization (security feature)

You don't need to worry about these details usually,
but it's cool to know what's happening under the hood! 🔧
    """)
    
    wait_for_enter()
    
    print("\n✅ Lesson 6 Complete!")
    print("\nKey Takeaways:")
    print("  • Hash tables are O(1) average, O(n) worst case")
    print("  • Fastest for lookup, but don't maintain order")
    print("  • Use when you need speed, not when you need sorting")
    print("  • Python's dict is highly optimized and battle-tested")


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """Main tutorial program"""
    clear_screen()
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║          🗂️  HASH TABLES INTERACTIVE TUTORIAL  🗂️           ║
║                                                              ║
║                         Day 5                                ║
║                 Learn Hash Tables by Doing                   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

Welcome! This tutorial has 6 interactive lessons:

  1️⃣  Introduction to Hash Tables (The O(1) Superpower)
  2️⃣  Hash Functions (Converting Keys to Indices)
  3️⃣  Collision Handling (Chaining Strategy)
  4️⃣  Python Dictionary Deep Dive (Master dict!)
  5️⃣  Common Patterns (Real-world applications)
  6️⃣  Performance Analysis (When to use hash tables)

⏱️  Estimated time: 30-45 minutes
📚 Learn by seeing code in action
🎯 Understand O(1) lookup magic

Ready to become a hash table expert? Let's go! 🚀
    """)
    
    wait_for_enter()
    
    lessons = [
        ("1️⃣  Introduction to Hash Tables", lesson_1_intro),
        ("2️⃣  Hash Functions", lesson_2_hash_functions),
        ("3️⃣  Collision Handling", lesson_3_collisions),
        ("4️⃣  Python Dictionary Deep Dive", lesson_4_python_dict),
        ("5️⃣  Common Patterns", lesson_5_patterns),
        ("6️⃣  Performance Analysis", lesson_6_performance),
    ]
    
    for i, (title, lesson_func) in enumerate(lessons, 1):
        clear_screen()
        lesson_func()
        
        if i < len(lessons):
            print("\n" + "═" * 60)
            print(f"\n✅ {title} complete!")
            print(f"\n📍 Progress: {i}/{len(lessons)} lessons finished")
            print(f"⏭️  Next: {lessons[i][0]}")
            wait_for_enter()
    
    # Final summary
    clear_screen()
    print_header("🎉 TUTORIAL COMPLETE! 🎉")
    
    print("""
Congratulations! You've completed all 6 lessons! 🏆

You now understand:
  ✅ How hash tables achieve O(1) lookup
  ✅ Hash functions and collision handling
  ✅ Python's dict, defaultdict, and Counter
  ✅ Common hash table patterns
  ✅ When to use (and not use) hash tables
  ✅ Performance characteristics

🚀 NEXT STEPS:

1. Build Project 1: Custom Hash Table
   └─ Implement hash table from scratch
   └─ File: day5/hash_table.py
   └─ Time: 60-90 minutes

2. Build Project 2: Word Frequency Analyzer
   └─ Real-world application of hash tables
   └─ File: day5/word_frequency.py
   └─ Time: 60-90 minutes

3. Check Day 5 README for detailed guides

💡 Remember: Hash tables are everywhere in production code.
   Master them today, use them forever!

Happy coding! 🎯
    """)
    
    print("\n" + "═" * 60)
    print("\nTo start Project 1, run:")
    print("  python hash_table.py")
    print("\nOr read the guide first:")
    print("  cat README.md")
    print("═" * 60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Tutorial interrupted. Run again anytime!")
        sys.exit(0)
