# Day 6 Part 2: Advanced Graph Algorithms 🕸️

> **Date:** October 5-6, 2025  
> **Focus:** Weighted graphs, Dijkstra's algorithm, Cycle detection, Topological sort  
> **Time:** 2-3 hours  
> **Difficulty:** ⭐⭐⭐⭐⭐ (Advanced)

---

## 🎯 Today's Goals

Building on Part 1 (BFS & DFS), now add advanced algorithms:

1. **Weighted Graphs** - Edges with costs/distances
2. **Dijkstra's Algorithm** - Shortest path in weighted graphs
3. **Cycle Detection** - Find if graph has cycles
4. **Topological Sort** - Order tasks with dependencies
5. **Build Network Analyzer** - DevOps-focused project!

---

## 📚 What You'll Learn

### Weighted Graphs
```
Regular graph:          Weighted graph:
A --- B                 A --5-- B
|     |                 |       |
C --- D                3|       |2
                        |       |
                        C --7-- D

BFS finds: A → B (2 steps)
But shortest DISTANCE: A → C → D → B (3+7+2 = 12) might be shorter!
```

**Use cases:**
- 🗺️ GPS navigation (distance/time)
- 🌐 Network routing (latency)
- 💰 Cost optimization
- ⚡ Resource allocation

---

### Dijkstra's Algorithm

**The Problem:**
- BFS finds shortest PATH (number of edges)
- But what about shortest DISTANCE (sum of weights)?

**Dijkstra's Solution:**
- Finds shortest weighted path from source to all vertices
- Uses priority queue (heap) to always explore closest vertex first
- Greedy algorithm: makes locally optimal choice

**Algorithm:**
1. Set distance to start = 0, all others = ∞
2. Use min-heap, always process closest unvisited vertex
3. For each neighbor, update distance if shorter path found
4. Repeat until all vertices processed

**Time Complexity:** O((V + E) log V) with heap

**Example:**
```
Graph:
    A --1-- B
    |       |
    4       2
    |       |
    C --1-- D

Dijkstra from A:
- A: 0 (start)
- B: 1 (via A)
- C: 4 (via A)
- D: 3 (via A→B→D, not A→C→D!)
```

---

### Cycle Detection

**Why detect cycles?**
- Package dependencies (prevent circular imports)
- Deadlock detection
- Workflow validation
- Graph coloring

**Algorithm (DFS-based):**
- Use 3 colors: WHITE (unvisited), GRAY (visiting), BLACK (done)
- If we reach a GRAY vertex, cycle found!

**Directed vs Undirected:**
- Directed: A→B→C→A is a cycle
- Undirected: Need to track parent (A-B-A is not a cycle, just backtracking)

---

### Topological Sort

**The Problem:**
Order tasks when some depend on others.

**Example - Package Installation:**
```
Dependencies:
- app depends on: db, cache
- db depends on: config
- cache depends on: config

Valid install order: config → db → cache → app
(or: config → cache → db → app)
```

**Algorithm (DFS-based):**
1. Do DFS on all vertices
2. When vertex is finished (all children visited), add to stack
3. Return reversed stack

**Only works on DAGs (Directed Acyclic Graphs)!**

---

## 🛠️ Methods to Implement

Extend your Graph class from Part 1:

### 1. `add_weighted_edge(v1, v2, weight)`
```python
# Add edge with weight (distance, cost, time)
g.add_weighted_edge("NYC", "Boston", 215)  # 215 miles
```

### 2. `dijkstra(start)`
```python
# Find shortest weighted paths from start to all vertices
distances, paths = g.dijkstra("NYC")
print(distances["Boston"])  # 215
print(paths["Boston"])      # ['NYC', 'Boston']
```

### 3. `has_cycle()`
```python
# Detect if graph contains a cycle
if g.has_cycle():
    print("⚠️ Circular dependency detected!")
```

### 4. `topological_sort()`
```python
# Order vertices respecting dependencies
install_order = g.topological_sort()
# ['config', 'db', 'cache', 'app']
```

---

## 🎯 Project: Network Topology Analyzer

**Build a DevOps tool that:**
1. Models a server network (vertices = servers, edges = connections with latency)
2. Finds fastest route between servers (Dijkstra)
3. Detects network loops (cycle detection)
4. Orders server startup sequence (topological sort)

**Example:**
```python
network = NetworkAnalyzer()

# Add servers
network.add_server("web1", "192.168.1.10")
network.add_server("web2", "192.168.1.11")
network.add_server("db1", "192.168.1.20")
network.add_server("cache1", "192.168.1.30")

# Add connections with latency (ms)
network.add_connection("web1", "cache1", 5)
network.add_connection("web1", "db1", 15)
network.add_connection("web2", "cache1", 8)
network.add_connection("cache1", "db1", 3)

# Analysis
network.find_fastest_route("web1", "db1")
# Output: web1 → cache1 → db1 (8ms total)

network.check_redundancy()
# Output: ✅ Network has redundant paths

network.detect_loops()
# Output: ⚠️ Loop detected: web1 → cache1 → db1 → web1
```

---

## 📋 Learning Path (2-3 hours)

### Phase 1: Weighted Graphs (30 min)
- Modify `add_edge()` to support weights
- Update graph representation

### Phase 2: Dijkstra's Algorithm (60 min)
- Implement priority queue version
- Test with sample graphs
- Compare with BFS results

### Phase 3: Cycle Detection (30 min)
- Implement DFS-based detection
- Test directed and undirected graphs

### Phase 4: Topological Sort (30 min)
- Implement DFS-based sort
- Handle invalid cases (cycles)

### Phase 5: Network Analyzer Project (60 min)
- Build NetworkAnalyzer class
- Integrate all algorithms
- Create CLI interface

---

## 🧪 Testing Examples

### Test 1: Dijkstra vs BFS
```python
g = Graph(directed=False)

# Create weighted graph
g.add_weighted_edge("A", "B", 10)
g.add_weighted_edge("A", "C", 1)
g.add_weighted_edge("C", "D", 1)
g.add_weighted_edge("D", "B", 1)

# BFS says: A → B (2 edges)
print(g.bfs("A"))  # ['A', 'B', 'C', 'D']

# Dijkstra says: A → C → D → B (distance = 3)
distances, paths = g.dijkstra("A")
print(paths["B"])  # ['A', 'C', 'D', 'B']
print(distances["B"])  # 3 (not 10!)
```

### Test 2: Cycle Detection
```python
g = Graph(directed=True)

g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("C", "A")  # Creates cycle!

print(g.has_cycle())  # True
```

### Test 3: Topological Sort
```python
g = Graph(directed=True)

# Package dependencies
g.add_edge("app", "db")
g.add_edge("app", "cache")
g.add_edge("db", "config")
g.add_edge("cache", "config")

order = g.topological_sort()
print(order)  # ['config', 'db', 'cache', 'app']
```

---

## 💡 Key Insights

### When to Use What:
- **BFS:** Shortest path (unweighted), level-order
- **DFS:** Exploring all paths, cycle detection, topological sort
- **Dijkstra:** Shortest path (weighted), GPS navigation
- **A*:** Dijkstra + heuristic (faster for specific goals)

### DevOps Applications:
- **Network Routing:** Find fastest path between servers
- **Dependency Management:** Install packages in correct order
- **Load Balancing:** Distribute traffic optimally
- **Failover Planning:** Redundant paths for reliability

---

## 🎓 Success Criteria

By the end of Day 6 Part 2, you should:
- ✅ Understand weighted graphs vs unweighted
- ✅ Implement Dijkstra's algorithm
- ✅ Detect cycles in directed graphs
- ✅ Perform topological sorting
- ✅ Build a practical network analyzer tool
- ✅ Know when to use each algorithm

---

## 🚀 Tomorrow: Day 7

**Week 1 Review & Mastery Check:**
- Review all data structures (Days 1-6)
- Coding challenges
- Build a capstone project combining everything
- Assess readiness for Week 2

---

**Let's master advanced graphs!** 🚀
