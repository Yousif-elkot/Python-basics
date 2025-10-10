# Day 6 Part 2: Advanced Graph Algorithms - Learning Roadmap

## 🎯 Learning Path

### Phase 1: Tutorial (45-60 min)
**Goal:** Understand advanced graph concepts

1. **Run Interactive Tutorial**
   ```bash
   python learn_advanced_graphs.py
   ```

2. **Lessons to Complete:**
   - ✅ Lesson 1: Weighted Graphs (10 min)
   - ✅ Lesson 2: Dijkstra Introduction (15 min)
   - ✅ Lesson 3: Dijkstra Live Demo (10 min)
   - ✅ Lesson 4: Cycle Detection (10 min)
   - ✅ Lesson 5: Topological Sort (10 min)
   - ✅ Lesson 6: Algorithm Comparison (10 min)

### Phase 2: Implementation (60-90 min)
**Goal:** Implement advanced algorithms

1. **Open graph.py**
   - Review the Graph class structure
   - Note the TODO comments

2. **Implement Methods (in order):**
   
   **Step 1: Basic Setup (10 min)**
   - `add_vertex()` - Add vertices to graph
   - `add_edge()` - Add weighted edges
   - `get_neighbors()` - Get neighbors with weights
   
   **Step 2: Dijkstra's Algorithm (30 min)**
   - `dijkstra()` - Shortest weighted path
   - Use priority queue (heapq)
   - Track parent pointers for path reconstruction
   
   **Step 3: Cycle Detection (20 min)**
   - `has_cycle()` - Detect cycles using 3-color DFS
   - Helper: `_has_cycle_util()` - Recursive DFS with colors
   
   **Step 4: Topological Sort (20 min)**
   - `topological_sort()` - Dependency ordering
   - Helper: `_topo_sort_util()` - DFS with stack
   - Check for cycles first!

3. **Test Your Implementation**
   ```bash
   python graph.py
   ```

### Phase 3: Project (30-45 min)
**Goal:** Build practical DevOps tool

Build the **Network Topology Analyzer**:
- Model server network with latencies
- Find optimal routes (Dijkstra)
- Detect network loops (cycle detection)
- Order server startup (topological sort)

## 📊 Complexity Reference

| Algorithm | Time Complexity | Space Complexity | Data Structure |
|-----------|----------------|------------------|----------------|
| BFS | O(V + E) | O(V) | Queue |
| DFS | O(V + E) | O(V) | Stack/Recursion |
| Dijkstra | O((V+E) log V) | O(V) | Priority Queue |
| Cycle Detection | O(V + E) | O(V) | DFS + Colors |
| Topological Sort | O(V + E) | O(V) | DFS + Stack |

## 🔑 Key Concepts

### Dijkstra's Algorithm
- **Purpose:** Shortest path in weighted graph
- **Requirement:** Non-negative weights only
- **How:** Greedy approach with priority queue
- **Output:** Distance + path

### Cycle Detection
- **Purpose:** Find circular dependencies
- **Method:** 3-color DFS algorithm
- **Colors:**
  - WHITE (0): Not visited
  - GRAY (1): Being processed (in current path)
  - BLACK (2): Completely processed
- **Rule:** If we reach GRAY vertex → cycle found!

### Topological Sort
- **Purpose:** Linear ordering respecting dependencies
- **Requirement:** Must be DAG (no cycles!)
- **Method:** DFS + stack
- **Output:** Order where A comes before B if A→B edge exists

## 🎓 Learning Tips

### Understanding Dijkstra
1. Think "greedy BFS with weights"
2. Always explore closest unvisited vertex
3. Priority queue ensures we explore in distance order
4. Parent tracking allows path reconstruction

### Understanding Cycle Detection
1. GRAY vertices are "in current path"
2. Reaching GRAY vertex = found way back = cycle!
3. BLACK vertices are "done, won't cause cycles"
4. WHITE vertices are "not yet explored"

### Understanding Topological Sort
1. DFS visits vertices depth-first
2. Add to stack when DONE (after all descendants)
3. Reverse stack gives topological order
4. Why? Descendants added first, then ancestors

## 🏗️ Real-World Applications

### Dijkstra
- 🗺️ GPS navigation (shortest route)
- 🌐 Network routing (lowest latency)
- 💰 Financial arbitrage (best exchange rate)
- 🎮 Game pathfinding (A* algorithm uses Dijkstra)

### Cycle Detection
- 📦 Package managers (circular dependencies)
- 🔧 Build systems (circular imports)
- 💰 Finance (detect circular transactions)
- 🗓️ Task scheduling (impossible task dependencies)

### Topological Sort
- 📦 Package installation order (npm, pip)
- 🏗️ Build systems (compile order)
- 🎓 Course prerequisites
- 🚀 Service startup sequences
- ⚙️ Makefile dependency resolution

## ✅ Success Criteria

### Phase 1 Complete
- [ ] Completed all 6 tutorial lessons
- [ ] Understand weighted graphs
- [ ] Understand Dijkstra's algorithm
- [ ] Understand cycle detection
- [ ] Understand topological sort

### Phase 2 Complete
- [ ] Implemented `add_vertex()` and `add_edge()`
- [ ] Implemented `get_neighbors()`
- [ ] Implemented `dijkstra()` with priority queue
- [ ] Implemented `has_cycle()` with 3-color DFS
- [ ] Implemented `topological_sort()` with DFS + stack
- [ ] All tests passing (4/4)

### Phase 3 Complete
- [ ] Network Topology Analyzer built
- [ ] Can model server networks
- [ ] Can find optimal routes
- [ ] Can detect network loops
- [ ] Can order server startup

## 🚀 Next Steps

After completing Day 6 Part 2:
1. Take Day 7 for Week 1 Review
2. Complete coding challenges
3. Build capstone project
4. Prepare for Week 2 (Algorithms & Patterns)

## 📚 Additional Resources

### If you want to dive deeper:
- **Bellman-Ford Algorithm:** Dijkstra for negative weights
- **A\* Search:** Dijkstra + heuristic for faster pathfinding
- **Kruskal's Algorithm:** Minimum spanning tree
- **Prim's Algorithm:** Alternative MST algorithm
- **Floyd-Warshall:** All-pairs shortest paths

### Practice Problems:
- LeetCode: #743 (Network Delay Time) - Dijkstra
- LeetCode: #207 (Course Schedule) - Cycle Detection
- LeetCode: #210 (Course Schedule II) - Topological Sort
- LeetCode: #787 (Cheapest Flights Within K Stops) - Modified Dijkstra

---

**Time to master advanced graphs!** 🎯💪
