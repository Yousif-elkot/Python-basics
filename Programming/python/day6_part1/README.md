# Day 6: Graphs Part 1 - Implementation & Traversals 🕸️

> **Date:** October 5-6, 2025  
> **Focus:** Graph data structure, BFS, DFS  
> **Time:** 3-4 hours  
> **Difficulty:** ⭐⭐⭐⭐ (Advanced)

---

## 🎯 Today's Goals

1. **Understand Graphs** - Most flexible data structure (social networks, maps, dependencies)
2. **Graph Representations** - Adjacency list vs adjacency matrix
3. **Breadth-First Search (BFS)** - Level-by-level exploration using queue
4. **Depth-First Search (DFS)** - Deep exploration using stack/recursion
5. **Build Graph Class** - Full implementation with both traversals

---

## 📚 What Are Graphs?

A **graph** is a collection of **vertices (nodes)** connected by **edges**.

### Real-World Examples:
- 🌐 **Social Networks** - People (vertices) + Friendships (edges)
- 🗺️ **Maps** - Cities (vertices) + Roads (edges)
- 🌳 **Dependencies** - Packages (vertices) + Dependencies (edges)
- 🌐 **Web Pages** - Pages (vertices) + Links (edges)
- 🖧 **Computer Networks** - Devices (vertices) + Connections (edges)

### Types of Graphs:
```
Undirected Graph:        Directed Graph (Digraph):
    A --- B                  A --> B
    |     |                  ↓     ↓
    C --- D                  C --> D

Weighted Graph:          Cyclic Graph:
    A --5-- B                A --> B
    |       |                ↓     ↓
    3       2                C <-- D
    |       |                (has cycle)
    C --7-- D
```

---

## 🧠 Graph Representations

### 1. Adjacency List (What we'll use!)
```python
{
    'A': ['B', 'C'],    # A connects to B and C
    'B': ['A', 'D'],    # B connects to A and D
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```
**Pros:** Memory efficient (O(V + E)), fast for sparse graphs  
**Cons:** Slower to check if edge exists

### 2. Adjacency Matrix
```python
     A  B  C  D
A [[ 0, 1, 1, 0 ],
B  [ 1, 0, 0, 1 ],
C  [ 1, 0, 0, 1 ],
D  [ 0, 1, 1, 0 ]]
```
**Pros:** O(1) edge lookup  
**Cons:** O(V²) space, wasteful for sparse graphs

---

## 🔍 Graph Traversals

### Breadth-First Search (BFS) - Level by Level
```
Uses: Queue (FIFO)
Order: Visit all neighbors before going deeper

Example:
        A
       / \
      B   C
     / \   \
    D   E   F

BFS from A: A → B → C → D → E → F
(Level 0)   (Level 1) (Level 2)
```

**Use Cases:**
- ✅ Shortest path in unweighted graph
- ✅ Level-order traversal
- ✅ Social network "degrees of separation"
- ✅ Web crawlers

**Algorithm:**
1. Start at root, add to queue
2. While queue not empty:
   - Dequeue a vertex
   - Visit it (mark as visited)
   - Enqueue all unvisited neighbors

---

### Depth-First Search (DFS) - Go Deep First
```
Uses: Stack (LIFO) or Recursion
Order: Explore as far as possible before backtracking

Example:
        A
       / \
      B   C
     / \   \
    D   E   F

DFS from A: A → B → D → E → C → F
(Goes deep first!)
```

**Use Cases:**
- ✅ Pathfinding
- ✅ Cycle detection
- ✅ Topological sorting
- ✅ Solving mazes
- ✅ Dependency resolution

**Algorithm:**
1. Start at root, mark as visited
2. For each unvisited neighbor:
   - Recursively visit neighbor (or push to stack)

---

## 🛠️ Today's Implementation

### Graph Class Structure:
```python
class Graph:
    def __init__(self, directed=False):
        """
        directed: False = undirected (friendship)
                  True = directed (Twitter follow)
        """
        self.graph = {}           # adjacency list
        self.directed = directed
    
    def add_vertex(self, vertex):
        """Add a new vertex"""
        pass  # TODO
    
    def add_edge(self, v1, v2, weight=None):
        """Add an edge between two vertices"""
        pass  # TODO
    
    def bfs(self, start):
        """Breadth-First Search traversal"""
        pass  # TODO
    
    def dfs(self, start):
        """Depth-First Search traversal"""
        pass  # TODO
    
    def has_path(self, start, end):
        """Check if path exists using BFS"""
        pass  # TODO
    
    def shortest_path(self, start, end):
        """Find shortest path using BFS"""
        pass  # TODO
```

---

## 📋 Learning Path (3-4 hours)

### Phase 1: Interactive Tutorial (30-45 min)
```bash
python learn_graphs.py
```
- 6 lessons on graph theory
- Hands-on examples
- Visual representations
- BFS vs DFS comparison

### Phase 2: Implementation (90-120 min)
```bash
# Work on graph.py
# Implement each method step by step
```

**Methods to implement:**
1. ✅ `add_vertex()` - Add vertex to graph
2. ✅ `add_edge()` - Connect two vertices
3. ✅ `bfs()` - Breadth-first traversal
4. ✅ `dfs()` - Depth-first traversal
5. ✅ `has_path()` - Check if path exists
6. ✅ `shortest_path()` - Find shortest path

### Phase 3: Testing (30 min)
```bash
python graph.py
```
- Test with sample graphs
- Verify BFS and DFS orders
- Test edge cases (cycles, disconnected graphs)

---

## 🎯 Projects

### Project 1: Graph Implementation ⭐⭐⭐⭐
**File:** `graph.py`  
**Description:** Complete graph class with BFS and DFS  
**Features:**
- Adjacency list representation
- Directed and undirected support
- BFS traversal (queue-based)
- DFS traversal (recursive)
- Path finding algorithms

**Concepts:**
- Graph theory fundamentals
- Queue and stack data structures
- Recursion
- Visited tracking

---

## 🧪 Testing Examples

### Example 1: Social Network
```python
# Create undirected graph (friendships)
g = Graph(directed=False)

# Add people
g.add_vertex("Alice")
g.add_vertex("Bob")
g.add_vertex("Charlie")
g.add_vertex("Diana")

# Add friendships
g.add_edge("Alice", "Bob")
g.add_edge("Bob", "Charlie")
g.add_edge("Charlie", "Diana")

# BFS from Alice
print(g.bfs("Alice"))
# Output: ['Alice', 'Bob', 'Charlie', 'Diana']

# Check if path exists
print(g.has_path("Alice", "Diana"))  # True
```

### Example 2: City Routes
```python
# Create directed graph (one-way streets)
g = Graph(directed=True)

g.add_vertex("NYC")
g.add_vertex("Boston")
g.add_vertex("Chicago")

g.add_edge("NYC", "Boston")
g.add_edge("Boston", "Chicago")
# Note: No edge from Chicago to NYC!

print(g.has_path("NYC", "Chicago"))      # True
print(g.has_path("Chicago", "NYC"))      # False (no path!)
```

### Example 3: Maze Solving
```python
# Represent maze as graph
maze = Graph(directed=False)

# Add positions
for i in range(9):
    maze.add_vertex(i)

# Add connections (walkable paths)
maze.add_edge(0, 1)
maze.add_edge(1, 2)
maze.add_edge(2, 5)
maze.add_edge(5, 8)  # path to exit

# Find path from start (0) to exit (8)
print(maze.shortest_path(0, 8))
# Output: [0, 1, 2, 5, 8]
```

---

## 📊 Complexity Analysis

| Operation | Adjacency List | Adjacency Matrix |
|-----------|----------------|------------------|
| Add Vertex | O(1) | O(V²) (resize) |
| Add Edge | O(1) | O(1) |
| Remove Vertex | O(V + E) | O(V²) |
| Remove Edge | O(E) | O(1) |
| BFS/DFS | O(V + E) | O(V²) |
| Check Edge | O(E) | O(1) |

**V** = number of vertices  
**E** = number of edges

---

## 🎓 Key Concepts to Master

### 1. Graph Terminology
- **Vertex (Node)** - A point in the graph
- **Edge** - Connection between vertices
- **Directed** - Edge has direction (A → B)
- **Undirected** - Edge is bidirectional (A ↔ B)
- **Weighted** - Edge has a value (distance, cost)
- **Path** - Sequence of vertices connected by edges
- **Cycle** - Path that starts and ends at same vertex
- **Connected** - Path exists between any two vertices
- **Degree** - Number of edges connected to a vertex

### 2. BFS vs DFS

| Aspect | BFS | DFS |
|--------|-----|-----|
| **Data Structure** | Queue (FIFO) | Stack (LIFO) or Recursion |
| **Order** | Level by level | Go deep first |
| **Shortest Path** | ✅ Yes (unweighted) | ❌ No |
| **Memory** | O(V) - broader | O(H) - height |
| **Use Case** | Shortest path, nearest neighbor | Pathfinding, cycle detection |

### 3. Applications
- **BFS:** GPS navigation, social networks, web crawlers
- **DFS:** Maze solving, topological sort, dependency graphs

---

## 💡 Tips for Success

1. **Draw It Out** ✏️
   - Visualize the graph on paper
   - Trace BFS and DFS step by step
   - Understand the order of visits

2. **Use Collections Module** 📦
   - `from collections import deque` for BFS queue
   - Much faster than list for queue operations

3. **Track Visited Nodes** ✅
   - Always use a `visited` set
   - Prevents infinite loops in cyclic graphs

4. **Test Edge Cases** 🧪
   - Empty graph
   - Single vertex
   - Disconnected components
   - Cyclic graphs

5. **Start Simple** 🎯
   - Begin with small graphs (3-4 vertices)
   - Verify correctness before scaling up

---

## 🔗 Resources

- **Visualizations:**
  - [VisuAlgo - Graph Traversals](https://visualgo.net/en/dfsbfs)
  - [Graph Explorer](https://cs.usfca.edu/~galles/visualization/BFS.html)

- **Reading:**
  - Graph theory basics
  - BFS and DFS algorithms
  - Path finding algorithms

---

## 🏆 Success Criteria

By the end of Day 6, you should be able to:
- ✅ Explain what graphs are and when to use them
- ✅ Implement a Graph class with adjacency list
- ✅ Add vertices and edges
- ✅ Perform BFS traversal using a queue
- ✅ Perform DFS traversal using recursion
- ✅ Find paths between vertices
- ✅ Explain the difference between BFS and DFS
- ✅ Choose the right traversal for different problems

---

## 🚀 Tomorrow: Day 7

**Graphs Part 2:**
- Dijkstra's algorithm (weighted shortest path)
- Topological sorting
- Cycle detection
- Network Topology Analyzer project

---

## 📝 Notes

**Graph Intuition:**
- Think of it as a tree with NO RULES!
- Trees are just restricted graphs (no cycles, one path between nodes)
- Graphs can have cycles, multiple paths, disconnected components

**When to use graphs:**
- Relationships between entities
- Network modeling
- Dependencies
- Navigation and routing
- Social connections

---

**Ready to build your first graph? Let's go!** 🚀
