# Day 5 Roadmap: Hash Tables & Dictionaries 🗺️

> **Goal:** Master hash tables, Python dictionaries, and O(1) lookup patterns through practical implementations

---

## 📅 Session Overview

**Total Time:** ~4-5 hours (flexible)  
**Core Projects:** 2 (Hash Table + Word Frequency)  
**Optional Projects:** 2 (LRU Cache + Anagrams)  
**Prerequisites:** Completed Days 1-4 (especially understanding of arrays and basic data structures)

---

## 🎯 Learning Path

### Phase 1: Foundations (45-60 minutes)

**Objective:** Understand hash table theory and Python dictionary internals

```
┌─────────────────────────────────────┐
│  1. Interactive Tutorial (30-45 min)│
│     → learn_hash_tables.py          │
│     → 6 lessons with hands-on       │
│                                     │
│  2. Read Hash Function Guide (15 min)│
│     → HASH_FUNCTION_GUIDE.md        │
│     → Understand hashing principles │
└─────────────────────────────────────┘
```

**Key Questions to Answer:**
- How does a hash function convert keys to indices?
- What happens when two keys hash to the same index?
- Why is O(1) lookup "average case" not "always"?
- How does Python's dict handle collisions?
- When should load factor trigger resizing?

**Success Check:**
- [ ] Can explain hash function purpose
- [ ] Understand collision handling strategies
- [ ] Know when hash tables beat other structures

---

### Phase 2: Implementation (60-90 minutes)

**Objective:** Build hash table from scratch to understand internals

```
┌──────────────────────────────────────────┐
│  Project 1: Hash Table Implementation    │
│  File: hash_table.py                     │
│                                          │
│  Components:                             │
│  ├── HashTable class                     │
│  ├── Hash function (modulo-based)        │
│  ├── Chaining with lists                 │
│  ├── Insert/search/delete operations     │
│  ├── Resize when load factor > 0.7       │
│  └── Statistics tracking                 │
│                                          │
│  Estimated: 60-90 minutes                │
└──────────────────────────────────────────┘
```

**Implementation Steps:**

1. **Step 1: Basic Structure** (15 min)
   - Create HashTable class with `__init__`
   - Initialize array of empty lists (buckets)
   - Track size and item count

2. **Step 2: Hash Function** (10 min)
   - Implement `_hash()` method
   - Convert key to integer
   - Modulo by table size

3. **Step 3: Insert Operation** (15 min)
   - Hash key to get index
   - Add (key, value) to bucket
   - Update existing keys
   - Increment count

4. **Step 4: Search Operation** (10 min)
   - Hash key to get index
   - Linear search in bucket
   - Return value or None

5. **Step 5: Delete Operation** (10 min)
   - Hash key to get index
   - Remove from bucket if found
   - Decrement count

6. **Step 6: Resizing** (15 min)
   - Check load factor after insert
   - Create larger table (2x size)
   - Rehash all items

7. **Step 7: Testing** (15 min)
   - Test basic operations
   - Test resizing behavior
   - Verify collision handling

**Success Check:**
- [ ] All operations work correctly
- [ ] Resizing happens automatically
- [ ] Can track load factor
- [ ] Handles collisions properly

---

### Phase 3: Application (60-90 minutes)

**Objective:** Apply hash tables to real-world text processing

```
┌──────────────────────────────────────────┐
│  Project 2: Word Frequency Analyzer      │
│  File: word_frequency.py                 │
│                                          │
│  Features:                               │
│  ├── Parse text files                    │
│  ├── Count word frequencies (dict)       │
│  ├── Case-insensitive counting           │
│  ├── Filter stop words                   │
│  ├── Display top N words                 │
│  ├── Export to JSON/CSV                  │
│  └── CLI with argparse                   │
│                                          │
│  Estimated: 60-90 minutes                │
└──────────────────────────────────────────┘
```

**Implementation Steps:**

1. **Step 1: File Reading** (10 min)
   - Read text file
   - Handle file not found errors
   - Support multiple encodings

2. **Step 2: Text Tokenization** (15 min)
   - Split into words
   - Remove punctuation
   - Convert to lowercase
   - Handle edge cases

3. **Step 3: Frequency Counting** (15 min)
   - Use `defaultdict(int)` or `Counter`
   - Increment counts for each word
   - Filter stop words

4. **Step 4: Display Results** (15 min)
   - Sort by frequency (descending)
   - Display top N words
   - Format output nicely

5. **Step 5: Export Features** (15 min)
   - JSON export
   - CSV export
   - Support both formats

6. **Step 6: CLI Interface** (15 min)
   - argparse setup
   - File path argument
   - Optional flags (--top, --export, --format)

**Success Check:**
- [ ] Can analyze any text file
- [ ] Top words displayed correctly
- [ ] Export works in both formats
- [ ] CLI is user-friendly

---

### Phase 4: Advanced (Optional, 60-90 min each)

**Option A: LRU Cache** (for caching patterns)

```
┌──────────────────────────────────────────┐
│  Project 3: LRU Cache                    │
│  File: lru_cache.py                      │
│                                          │
│  Challenge: O(1) get + put + eviction    │
│  Solution: Dictionary + Doubly Linked List│
│                                          │
│  Components:                             │
│  ├── Dictionary for O(1) lookup          │
│  ├── Doubly linked list for order        │
│  ├── Move to front on access             │
│  ├── Remove from tail when full          │
│  └── Track hits/misses                   │
│                                          │
│  Estimated: 90-120 minutes               │
└──────────────────────────────────────────┘
```

**Option B: Anagram Finder** (for algorithm practice)

```
┌──────────────────────────────────────────┐
│  Project 4: Group Anagrams               │
│  File: anagrams.py                       │
│                                          │
│  Challenge: Group anagrams efficiently   │
│  Key Insight: Sort letters as dict key   │
│                                          │
│  Components:                             │
│  ├── Read word list                      │
│  ├── Sort characters (anagram signature) │
│  ├── Group by signature in dict          │
│  ├── Display groups                      │
│  └── Filter by group size                │
│                                          │
│  Estimated: 60-90 minutes                │
└──────────────────────────────────────────┘
```

---

## 📊 Time Estimates

### Minimum Path (Core Learning)
- **Phase 1:** 45-60 min (Tutorial + Reading)
- **Phase 2:** 60-90 min (Hash Table Implementation)
- **Phase 3:** 60-90 min (Word Frequency Analyzer)
- **Total:** 2.5-4 hours

### Full Path (Maximum Learning)
- **Core:** 2.5-4 hours
- **Phase 4:** +60-120 min (1-2 optional projects)
- **Total:** 3.5-6 hours

### Recommended Schedule

**If you have 3-4 hours:**
- ✅ Do Phases 1-3 (core projects)
- ⏭️ Skip Phase 4

**If you have 5+ hours:**
- ✅ Do Phases 1-3
- ✅ Add Project 3 (LRU Cache) - more practical
- ⏭️ Save Project 4 for later

---

## 🎓 Concepts Covered

### By End of Phase 1
- ✅ Hash function design principles
- ✅ Collision handling (chaining vs open addressing)
- ✅ Load factor and resizing
- ✅ O(1) lookup explanation
- ✅ Python dictionary internals

### By End of Phase 2
- ✅ Implement hash table from scratch
- ✅ Handle dynamic resizing
- ✅ Track performance metrics
- ✅ Compare with built-in dict

### By End of Phase 3
- ✅ Text processing techniques
- ✅ Frequency counting patterns
- ✅ Dictionary comprehensions
- ✅ defaultdict and Counter usage
- ✅ File I/O and export formats

### By End of Phase 4 (Optional)
- ✅ Advanced data structure combination (dict + linked list)
- ✅ Caching patterns and eviction policies
- ✅ String manipulation algorithms
- ✅ Grouping and classification problems

---

## 🛠️ Tools & Techniques

### Python Collections Module

```python
from collections import defaultdict, Counter, OrderedDict

# defaultdict - No KeyError
counts = defaultdict(int)
counts['word'] += 1  # Works even if 'word' not in dict

# Counter - Specialized for counting
counter = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
counter.most_common(2)  # [('a', 3), ('b', 2)]

# OrderedDict - Maintains insertion order (Python 3.7+ dicts do this too)
ordered = OrderedDict([('a', 1), ('b', 2)])
```

### Dictionary Patterns

```python
# Pattern 1: Frequency Counter
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

# Pattern 2: Grouping
groups = {}
for item in items:
    key = classify(item)
    groups.setdefault(key, []).append(item)

# Pattern 3: Memoization (Caching)
cache = {}
def expensive_function(n):
    if n in cache:
        return cache[n]
    result = compute(n)
    cache[n] = result
    return result

# Pattern 4: Dictionary Comprehension
squares = {x: x**2 for x in range(10)}
```

---

## 📚 Reference Materials

### Created for Day 5

| File | Purpose | Read When |
|------|---------|-----------|
| `learn_hash_tables.py` | Interactive tutorial | Start of Phase 1 |
| `HASH_FUNCTION_GUIDE.md` | Deep dive into hashing | Phase 1 |
| `COLLISION_GUIDE.md` | Collision strategies | During Phase 2 |
| `DICT_PATTERNS.md` | Common patterns | Phase 3 or reference |
| `QUICK_START.md` | Project setup guide | Before each project |

### Documentation to Reference

- **Python Docs:** [collections module](https://docs.python.org/3/library/collections.html)
- **Python Docs:** [dict methods](https://docs.python.org/3/library/stdtypes.html#dict)
- **Big O Cheat Sheet:** Hash table complexity

---

## 🎯 Success Metrics

### Knowledge Check

After Day 5, you should be able to answer:

1. **How does a hash table achieve O(1) lookup?**
   - Hash function converts key → index
   - Direct array access is O(1)
   - Collision handling may cause O(n) worst case

2. **What's the difference between chaining and open addressing?**
   - Chaining: Store collisions in linked lists
   - Open addressing: Find next empty slot

3. **When does Python resize a dictionary?**
   - When load factor exceeds ~0.67
   - Creates larger table, rehashes all items

4. **Hash Table vs BST - when to use each?**
   - Hash Table: Fast lookup, no order
   - BST: Sorted order, range queries

5. **What makes a good hash function?**
   - Deterministic, uniform distribution, fast, minimizes collisions

### Code Check

You should be able to:

- [ ] Implement a hash table from scratch in 30 minutes
- [ ] Count word frequencies in a text file in 10 minutes
- [ ] Use defaultdict and Counter effectively
- [ ] Explain collision handling to someone else
- [ ] Choose appropriate data structure for a problem

---

## 🔄 Testing Strategy

### Project 1: Hash Table

```python
# Test basic operations
ht = HashTable()
ht.insert("name", "Alice")
assert ht.search("name") == "Alice"
ht.delete("name")
assert ht.search("name") is None

# Test collisions
# (depends on your hash function)

# Test resizing
for i in range(100):
    ht.insert(f"key{i}", i)
# Should resize automatically
```

### Project 2: Word Frequency

```python
# Create test file
with open('test.txt', 'w') as f:
    f.write("cat dog cat bird dog cat")

# Test counting
freq = count_words('test.txt')
assert freq['cat'] == 3
assert freq['dog'] == 2
assert freq['bird'] == 1

# Test top N
top = get_top_words(freq, 2)
assert top == [('cat', 3), ('dog', 2)]
```

---

## 💡 Common Pitfalls

### 1. Forgetting About None Keys
```python
# ❌ Bad
def search(key):
    return self.table[self._hash(key)]  # What if key not found?

# ✅ Good
def search(key):
    for k, v in self.table[self._hash(key)]:
        if k == key:
            return v
    return None
```

### 2. Not Handling Load Factor
```python
# ❌ Bad
def insert(key, value):
    # Just insert, never resize

# ✅ Good
def insert(key, value):
    # Insert logic
    if self.load_factor() > 0.7:
        self._resize()
```

### 3. Inefficient String Processing
```python
# ❌ Bad (creates many intermediate strings)
for char in punctuation:
    text = text.replace(char, ' ')

# ✅ Good (single pass)
import re
words = re.findall(r'\w+', text.lower())
```

### 4. KeyError Without Checking
```python
# ❌ Bad
count = freq[word] + 1

# ✅ Good
count = freq.get(word, 0) + 1
# Or use defaultdict(int)
```

---

## 🚀 Challenge Extensions

If you finish early and want more:

### Challenge 1: Bloom Filter
- Probabilistic data structure
- Space-efficient set membership testing
- False positives possible, false negatives impossible

### Challenge 2: Consistent Hashing
- Used in distributed systems
- Minimal key redistribution on resize
- Important for caching layers

### Challenge 3: Perfect Hash Function
- No collisions for known set of keys
- Used in compilers, databases

### Challenge 4: Two-Sum Problem
- Given array and target, find two numbers that sum to target
- O(n) solution using hash table

---

## 🔗 Connections

### To Previous Days
- **Day 2:** Linear search in arrays → O(n)
- **Day 4:** BST search → O(log n)
- **Day 5:** Hash table search → O(1) average

### To Future Days
- **Day 6:** Graph adjacency lists use dictionaries
- **Day 8:** Dynamic programming uses memoization (dictionary cache)
- **Day 15:** Database indexing uses hash tables

### To Cloud Engineering
- **DynamoDB:** Partition key uses hash for distribution
- **Redis/Memcached:** In-memory key-value stores
- **CloudFront:** Cache keys for CDN
- **Lambda:** Environment variables = dictionary

---

## 📈 Progress Tracking

Update after each phase:

```bash
# In your terminal
echo "Phase 1 complete: $(date)" >> day5_progress.txt
echo "Phase 2 complete: $(date)" >> day5_progress.txt
echo "Phase 3 complete: $(date)" >> day5_progress.txt
```

---

## 🎯 End-of-Day Checklist

- [ ] Completed `learn_hash_tables.py` tutorial
- [ ] Implemented hash table from scratch (Project 1)
- [ ] Built word frequency analyzer (Project 2)
- [ ] Tested all projects thoroughly
- [ ] Read collision handling guide
- [ ] Understand when to use hash tables vs other structures
- [ ] (Optional) Completed LRU Cache or Anagrams
- [ ] Committed code to Git
- [ ] Updated main README.md

---

## 🔜 Tomorrow Preview

**Day 6: Graphs & Graph Algorithms**

You'll learn:
- Graph representations (adjacency matrix vs list)
- BFS (Breadth-First Search)
- DFS (Depth-First Search)
- Shortest path algorithms
- Real-world applications (social networks, navigation)

Graphs use hash tables (dictionaries) for adjacency lists! 🔗

---

**Remember:** Hash tables are everywhere in production code. Master them today, use them forever! 💪

**Estimated Total Time:** 3-5 hours (core) + 1-2 hours (optional)

Ready to achieve O(1) lookup mastery? Let's go! 🚀
