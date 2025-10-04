# Day 5: Hash Tables & Dictionaries 🗂️

> **Focus:** Understanding hash tables, Python dictionaries, hash functions, collision handling, and O(1) lookup magic

---

## 📚 Learning Objectives

By the end of Day 5, you will:

1. **Understand Hash Tables** - How they achieve O(1) lookup/insert/delete
2. **Master Python Dictionaries** - Built-in hash table implementation
3. **Learn Hash Functions** - Converting keys to array indices
4. **Handle Collisions** - Chaining vs open addressing strategies
5. **Implement Custom Solutions** - Build hash table from scratch
6. **Apply to Real Problems** - Word frequency, caching, grouping, deduplication

---

## 🎯 Why Hash Tables Matter

### The O(1) Superpower

**Problem:** Finding an item in a list is O(n) - you might check every element

```python
# Linear search - O(n)
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
"Eve" in names  # Checks up to 5 items
```

**Solution:** Hash tables give O(1) average case lookup!

```python
# Hash table - O(1)
names_set = {"Alice", "Bob", "Charlie", "David", "Eve"}
"Eve" in names_set  # Checks ~1 location (on average)
```

### Real-World Applications

| Use Case | Example | Why Hash Table? |
|----------|---------|----------------|
| **Caching** | Store computed results | Fast retrieval by key |
| **Frequency Counting** | Word counter, character count | Increment values quickly |
| **Deduplication** | Remove duplicates | Check existence in O(1) |
| **Grouping** | Group by category | Organize data efficiently |
| **Database Indexing** | Index by primary key | Instant record lookup |
| **DNS Lookup** | Domain → IP mapping | Fast hostname resolution |

---

## 🧠 Core Concepts

### 1. Hash Function

Converts a key into an array index:

```python
def simple_hash(key, size):
    """Convert string key to array index"""
    return sum(ord(c) for c in key) % size

# Example:
simple_hash("cat", 10)  # → 4
simple_hash("dog", 10)  # → 5
```

**Properties of Good Hash Functions:**
- ✅ Deterministic (same input → same output)
- ✅ Uniform distribution (spreads keys evenly)
- ✅ Fast to compute (O(1))
- ✅ Minimizes collisions

### 2. Collision Handling

**Collision:** When two keys hash to the same index

**Strategy 1: Chaining** (Python's approach)
```
Index 0: → ["apple", 3] → ["banana", 5]
Index 1: → ["cherry", 2]
Index 2: → ["date", 8] → ["elderberry", 1]
```

**Strategy 2: Open Addressing**
```
If slot is full, try next slot:
- Linear probing: index + 1, index + 2, ...
- Quadratic probing: index + 1², index + 2², ...
```

### 3. Load Factor

```
Load Factor = Number of items / Table size
```

- **< 0.7**: Good performance
- **> 0.7**: Start resizing (Python does this automatically)
- **Resizing**: Create bigger table, rehash all items

### 4. Time Complexity

| Operation | Average Case | Worst Case | Space |
|-----------|-------------|-----------|--------|
| Insert | O(1) | O(n) | O(n) |
| Search | O(1) | O(n) | - |
| Delete | O(1) | O(n) | - |

**Worst case** happens when all keys collide (rare with good hash function)

---

## 🐍 Python Dictionary Deep Dive

### Dictionary Basics

```python
# Creation
person = {"name": "Alice", "age": 25, "city": "NYC"}
person = dict(name="Alice", age=25, city="NYC")

# Access
person["name"]           # → "Alice"
person.get("job", "N/A") # → "N/A" (default if missing)

# Modify
person["age"] = 26
person["job"] = "Engineer"

# Delete
del person["city"]
person.pop("job", None)  # Safe delete with default

# Check existence
"name" in person  # → True

# Iteration
for key in person:              # Keys only
for value in person.values():   # Values only
for k, v in person.items():     # Both
```

### Advanced Dictionary Operations

```python
# Merging (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2  # → {"a": 1, "b": 3, "c": 4}

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
# → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Default values
from collections import defaultdict
word_count = defaultdict(int)
for word in ["cat", "dog", "cat"]:
    word_count[word] += 1  # No KeyError!

# Counting
from collections import Counter
counts = Counter(["a", "b", "a", "c", "b", "a"])
# → Counter({'a': 3, 'b': 2, 'c': 1})
counts.most_common(2)  # → [('a', 3), ('b', 2)]
```

---

## 🛠️ Day 5 Projects

### Project 1: Hash Table Implementation ⚙️

**Goal:** Build a hash table from scratch to understand internals

**Features:**
- Custom hash function
- Chaining collision handling
- Insert, search, delete operations
- Dynamic resizing when load factor > 0.7
- Clear statistics (load factor, collisions)

**Skills:**
- Implement hash function
- Handle collisions with linked lists
- Resize and rehash operations
- Track performance metrics

**File:** `day5/hash_table.py`

---

### Project 2: Word Frequency Analyzer 📊

**Goal:** Analyze text files and count word frequencies

**Features:**
- Count word occurrences in text files
- Case-insensitive counting
- Filter stop words (the, a, an, etc.)
- Display top N most frequent words
- Export results to JSON/CSV
- Compare multiple files
- Visualize with bar charts (optional)

**Skills:**
- Text processing and tokenization
- Dictionary for frequency counting
- File I/O operations
- Sorting by value
- Data export formats

**File:** `day5/word_frequency.py`

---

### Project 3: LRU Cache (Least Recently Used) 🗄️

**Goal:** Build a caching system with automatic eviction

**Features:**
- Store key-value pairs with capacity limit
- O(1) get and put operations
- Evict least recently used item when full
- Track cache hits and misses
- Statistics (hit rate, evictions)
- CLI for testing

**Skills:**
- Combine dictionary + doubly linked list
- Maintain access order
- Implement eviction policy
- Performance optimization

**File:** `day5/lru_cache.py`

---

### Project 4: Group Anagrams Finder 🔤

**Goal:** Group words that are anagrams of each other

**Features:**
- Find all anagram groups in a word list
- Support multiple input sources (file, stdin, API)
- Display groups sorted by frequency
- Filter by minimum group size
- Export to JSON
- Interactive CLI

**Skills:**
- String manipulation (sorting, hashing)
- Grouping with dictionaries
- Tuple as dictionary key
- Data organization

**File:** `day5/anagrams.py`

---

## 📋 Project Selection Guide

| If you want to... | Do this project |
|------------------|----------------|
| **Understand internals** | Project 1: Hash Table |
| **Text processing skills** | Project 2: Word Frequency |
| **Learn caching patterns** | Project 3: LRU Cache |
| **Algorithm problem solving** | Project 4: Anagrams |

**Recommendation:** Do Projects 1 + 2 minimum, then choose 3 or 4 based on interest.

---

## 🎓 Learning Resources

### Interactive Tutorial
- `learn_hash_tables.py` - 6 interactive lessons on hash table concepts

### Guides
- `HASH_FUNCTION_GUIDE.md` - Deep dive into hash functions
- `COLLISION_GUIDE.md` - Collision handling strategies
- `DICT_PATTERNS.md` - Common dictionary patterns in Python

---

## 🔗 Connection to Previous Days

| Day | Connection | Application |
|-----|-----------|------------|
| **Day 1** | Phone Book | Used dictionary for contacts |
| **Day 2** | Todo List | Could use dict for O(1) lookup by ID |
| **Day 3** | Command History | Could use dict for fast command search |
| **Day 4** | BST vs Hash** | Trees: O(log n) sorted, Hash: O(1) unsorted |

---

## ☁️ Cloud Engineering Bridge

### AWS Applications

| AWS Service | Hash Table Usage |
|------------|------------------|
| **DynamoDB** | NoSQL database using hash keys for partitioning |
| **S3** | Object keys hashed for fast retrieval |
| **CloudFront** | Cache keys for CDN edge locations |
| **Lambda** | Environment variables stored as key-value |
| **Parameter Store** | Key-value storage for configuration |
| **ElastiCache** | Redis/Memcached for distributed caching |

### DevOps Patterns

- **Configuration Management:** Key-value stores (Consul, etcd)
- **Service Discovery:** DNS resolution using hash tables
- **Load Balancing:** Session affinity with hash-based routing
- **Monitoring:** Metric aggregation by labels (Prometheus)

---

## 📊 Success Criteria

By end of Day 5, you should be able to:

- [ ] Explain how hash tables achieve O(1) lookup
- [ ] Implement a basic hash function
- [ ] Handle collisions with chaining
- [ ] Use Python dictionaries effectively
- [ ] Apply defaultdict and Counter from collections
- [ ] Count frequencies in O(n) time
- [ ] Group data by keys efficiently
- [ ] Understand when to use hash table vs tree vs array

---

## 🚀 Getting Started

### Quick Start

1. **Learn the concepts:**
   ```bash
   python learn_hash_tables.py
   ```

2. **Read the roadmap:**
   ```bash
   cat ROADMAP.md
   ```

3. **Start with Project 1:**
   ```bash
   cat QUICK_START.md
   ```

### Recommended Flow

**Morning Session (1-1.5 hours):**
- Run `learn_hash_tables.py` (30-45 min)
- Read `HASH_FUNCTION_GUIDE.md` (15-30 min)

**Afternoon Session (1.5-2 hours):**
- Project 1: Hash Table Implementation (60-90 min)
- Test thoroughly

**Evening Session (1-1.5 hours):**
- Project 2: Word Frequency Analyzer (60-90 min)

**Optional:**
- Project 3 or 4 if you have energy (60-90 min each)

---

## 💡 Key Takeaways

### When to Use Hash Tables

✅ **Use hash table when:**
- Need fast lookup by key (O(1))
- Counting frequencies
- Removing duplicates
- Grouping by category
- Caching results
- Order doesn't matter

❌ **Don't use hash table when:**
- Need sorted order (use BST or sorted list)
- Need range queries (use BST)
- Keys aren't hashable (use list/array)
- Memory is extremely limited

### Python Dictionary Tips

```python
# ✅ Good practices
if key in dict:            # Check before accessing
    value = dict[key]

value = dict.get(key, default)  # Safe access

for k, v in dict.items():  # Iterate both

# ❌ Avoid
try:                       # Don't use exceptions for control flow
    value = dict[key]
except KeyError:
    pass

for k in dict.keys():      # Redundant, just use: for k in dict
```

---

## 📈 Progress Tracking

Track your learning in the main roadmap:

```bash
# Update after each project
echo "Day 5 - Hash Tables: Completed Project X" >> ../progress.log
```

---

## 🎯 Next Steps

After completing Day 5:

**Day 6:** Graphs & Graph Algorithms (BFS, DFS, Dijkstra)  
**Day 7:** More Graph Problems (Topological Sort, Minimum Spanning Tree)  
**Day 8:** Dynamic Programming Foundations  

---

**Remember:** Hash tables are one of the most used data structures in production code. Master them! 💪

**Estimated Time:** 3-4 hours (core projects) + 1-2 hours (optional projects)

Good luck! 🚀
