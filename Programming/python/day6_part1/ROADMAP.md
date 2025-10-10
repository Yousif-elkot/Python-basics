# Day 6 Roadmap: Graphs Part 1 🕸️

> **Goal:** Master graph data structure and traversal algorithms (BFS & DFS)

---

## 📅 Session Overview

**Total Time:** ~3-4 hours  
**Core Project:** Graph implementation with BFS and DFS  
**Prerequisites:** Understanding of queues (Day 3), recursion (Day 4), and basic data structures

---

## 🎯 Learning Path

### Phase 1: Interactive Tutorial (30-45 minutes)

**Run the tutorial:**
```bash
cd day6
python learn_graphs.py
```

**6 Lessons:**
1. **What Are Graphs?** - Definition, types, and real-world examples
2. **Graph Representations** - Adjacency list vs adjacency matrix
3. **Breadth-First Search (BFS)** - Level-by-level traversal with queue
4. **Depth-First Search (DFS)** - Deep-first exploration with recursion
5. **BFS vs DFS Comparison** - When to use which algorithm
6. **Real-World Applications** - Social networks, GPS, web crawlers, dependencies

**What you'll learn:**
- Graph terminology (vertex, edge, path, cycle)
- Directed vs undirected graphs
- Weighted vs unweighted graphs
- How BFS explores level by level
- How DFS explores as deep as possible
- Real-world use cases

---

### Phase 2: Implementation (90-120 minutes)

**File:** `graph.py`

**Implement these methods:**

#### 1. `add_vertex(vertex)` - 10 minutes
```python
# Add a new vertex to the graph
# Just add it to self.graph with empty neighbor list
```

#### 2. `add_edge(v1, v2, weight=None)` - 15 minutes
```python
# Connect two vertices with an edge
# Remember: undirected = add both directions!
```

#### 3. `bfs(start)` - 30 minutes ⭐
```python
# Breadth-First Search using queue (deque)
# Algorithm:
# 1. Create queue with start vertex
# 2. Create visited set
# 3. While queue not empty:
#    - Dequeue vertex
#    - If not visited, mark visited and add to result
#    - Enqueue all unvisited neighbors
```

#### 4. `dfs(start)` - 30 minutes ⭐
```python
# Depth-First Search using recursion
# Algorithm:
# 1. Create visited set and result list
# 2. Recursive helper function:
#    - Mark current as visited
#    - Add to result
#    - For each unvisited neighbor, recurse
```

#### 5. `has_path(start, end)` - 20 minutes
```python
# Check if path exists between two vertices
# Hint: Use BFS, but stop early if you find end
```

#### 6. `shortest_path(start, end)` - 30 minutes
```python
# Find shortest path using BFS
# Hint: Track parent of each vertex, then reconstruct path
```

---

### Phase 3: Testing (30 minutes)

**Run tests:**
```bash
python graph.py
```

**4 test scenarios:**
1. ✅ Undirected graph (social network)
2. ✅ Directed graph (Twitter follows)
3. ✅ Disconnected components
4. ✅ Cyclic graph

**Expected output:**
- All BFS and DFS traversals correct
- Path finding works
- Handles edge cases (cycles, disconnected)

---

## 🧪 Example Usage

### Social Network (Undirected)
```python
g = Graph(directed=False)

g.add_edge("Alice", "Bob")
g.add_edge("Bob", "Charlie")
g.add_edge("Charlie", "Diana")

print(g.bfs("Alice"))
# ['Alice', 'Bob', 'Charlie', 'Diana']

print(g.has_path("Alice", "Diana"))
# True

print(g.shortest_path("Alice", "Diana"))
# ['Alice', 'Bob', 'Charlie', 'Diana']
```

### Twitter Follows (Directed)
```python
g = Graph(directed=True)

g.add_edge("Alice", "Bob")  # Alice follows Bob
g.add_edge("Bob", "Charlie")  # Bob follows Charlie

print(g.has_path("Alice", "Charlie"))
# True (Alice → Bob → Charlie)

print(g.has_path("Charlie", "Alice"))
# False (no reverse path in directed graph!)
```

---

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| `add_vertex()` | O(1) | O(1) |
| `add_edge()` | O(1) | O(1) |
| `bfs()` | O(V + E) | O(V) |
| `dfs()` | O(V + E) | O(V) |
| `has_path()` | O(V + E) | O(V) |
| `shortest_path()` | O(V + E) | O(V) |

**V** = number of vertices  
**E** = number of edges

---

## 💡 Key Concepts

### BFS (Breadth-First Search)
- **Data Structure:** Queue (FIFO)
- **Strategy:** Explore all neighbors before going deeper
- **Use Cases:**
  - ✅ Shortest path (unweighted graph)
  - ✅ Level-order traversal
  - ✅ Social network "degrees of separation"
  - ✅ Web crawlers

### DFS (Depth-First Search)
- **Data Structure:** Stack (LIFO) or Recursion
- **Strategy:** Explore as far as possible before backtracking
- **Use Cases:**
  - ✅ Pathfinding in mazes
  - ✅ Cycle detection
  - ✅ Topological sorting
  - ✅ Solving puzzles

---

## 🎯 Success Criteria

By the end of Day 6, you should:
- ✅ Understand what graphs are and when to use them
- ✅ Know the difference between directed and undirected graphs
- ✅ Implement adjacency list representation
- ✅ Implement BFS using a queue
- ✅ Implement DFS using recursion
- ✅ Find paths between vertices
- ✅ Explain BFS vs DFS tradeoffs

---

## 🚀 Tomorrow: Day 7

**Graphs Part 2:**
- Dijkstra's algorithm (weighted shortest path)
- Topological sorting
- Cycle detection
- Network Topology Analyzer project (DevOps-focused!)

---

## 📝 Tips

1. **Draw it out!** ✏️
   - Visualize the graph on paper
   - Trace BFS and DFS step by step

2. **Use `collections.deque`** 📦
   - Much faster than list for queue operations
   - `from collections import deque`

3. **Track visited nodes** ✅
   - Always use a `visited` set
   - Prevents infinite loops in cyclic graphs

4. **Test incrementally** 🧪
   - Test each method after implementing
   - Start with simple 3-4 vertex graphs

5. **Understand the difference** 🤔
   - BFS: Level by level (nearest first)
   - DFS: Deep first (explore fully before backtracking)

---

**Ready to build your graph? Let's go!** 🚀
