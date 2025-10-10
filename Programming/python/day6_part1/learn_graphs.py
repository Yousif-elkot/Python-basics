#!/usr/bin/env python3
"""
Day 6: Interactive Graph Tutorial
Learn graphs, BFS, and DFS through hands-on examples!

Run: python learn_graphs.py
"""

from collections import deque
import time
import sys

def clear_screen():
    """Clear terminal screen"""
    print("\033[2J\033[H", end="")

def print_header(title):
    """Print section header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60 + "\n")

def wait_for_enter(prompt="Press ENTER to continue..."):
    """Wait for user input"""
    input(f"\n{prompt}")

def print_graph_visual(graph_type="undirected"):
    """Print visual representation of graphs"""
    if graph_type == "undirected":
        print("""
    Undirected Graph (Friendship):
    
        Alice ————— Bob
          |           |
          |           |
        Charlie ——— Diana
        
    Edges go both ways!
    If Alice → Bob, then Bob → Alice
        """)
    elif graph_type == "directed":
        print("""
    Directed Graph (Twitter Follow):
    
        Alice ————→ Bob
          ↓           ↓
          |           |
        Charlie ←—— Diana
        
    Edges have direction!
    Alice follows Bob, but Bob might not follow Alice
        """)
    elif graph_type == "weighted":
        print("""
    Weighted Graph (City Distances):
    
        NYC ——5mi—— Boston
         |            |
        3mi          2mi
         |            |
        Philly ——7mi—— DC
        
    Edges have values (distance, cost, time)
        """)

# ============================================================================
# LESSON 1: What Are Graphs?
# ============================================================================

def lesson_1():
    """Introduction to graphs"""
    clear_screen()
    print_header("LESSON 1: What Are Graphs?")
    
    print("""
A GRAPH is a collection of VERTICES (nodes) connected by EDGES.

Think of it as:
- 🌐 Social Network: People + Friendships
- 🗺️ Map: Cities + Roads
- 🌳 Dependency Graph: Packages + Dependencies
- 🖧 Network: Computers + Connections

Graphs are the MOST FLEXIBLE data structure!
    """)
    
    wait_for_enter()
    
    print("\n" + "-" * 60)
    print("TYPES OF GRAPHS:")
    print("-" * 60)
    
    print("\n1. UNDIRECTED GRAPH:")
    print_graph_visual("undirected")
    
    wait_for_enter("Press ENTER to see directed graphs...")
    
    print("\n2. DIRECTED GRAPH:")
    print_graph_visual("directed")
    
    wait_for_enter("Press ENTER to see weighted graphs...")
    
    print("\n3. WEIGHTED GRAPH:")
    print_graph_visual("weighted")
    
    wait_for_enter()
    
    print("\n" + "-" * 60)
    print("KEY TERMINOLOGY:")
    print("-" * 60)
    print("""
• VERTEX (Node): A point in the graph
• EDGE: A connection between two vertices
• DEGREE: Number of edges connected to a vertex
• PATH: Sequence of vertices connected by edges
• CYCLE: Path that starts and ends at the same vertex
• CONNECTED: Path exists between any two vertices
    """)
    
    wait_for_enter()

# ============================================================================
# LESSON 2: Graph Representations
# ============================================================================

def lesson_2():
    """Graph representations"""
    clear_screen()
    print_header("LESSON 2: How to Store Graphs?")
    
    print("""
We need to represent graphs in code. Two main approaches:
    """)
    
    print("\n" + "-" * 60)
    print("1. ADJACENCY LIST (Most common!)")
    print("-" * 60)
    
    # Example graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }
    
    print("""
Graph:
    A --- B
    |     |
    C --- D

Adjacency List (Dictionary of Lists):
""")
    for vertex, neighbors in graph.items():
        print(f"  '{vertex}': {neighbors}  ← {vertex} connects to {', '.join(neighbors)}")
    
    print("""
PROS:
✅ Memory efficient: O(V + E) space
✅ Fast to iterate over neighbors
✅ Good for sparse graphs (few edges)

CONS:
❌ Slow to check if specific edge exists: O(E)
    """)
    
    wait_for_enter("Press ENTER to see adjacency matrix...")
    
    print("\n" + "-" * 60)
    print("2. ADJACENCY MATRIX (2D Array)")
    print("-" * 60)
    
    print("""
Same graph as 2D array:

     A  B  C  D
A [[ 0, 1, 1, 0 ],   ← A connects to B and C
B  [ 1, 0, 0, 1 ],   ← B connects to A and D
C  [ 1, 0, 0, 1 ],   ← C connects to A and D
D  [ 0, 1, 1, 0 ]]   ← D connects to B and C

1 = edge exists, 0 = no edge

PROS:
✅ O(1) edge lookup: matrix[A][B] tells if edge exists
✅ Simple to implement

CONS:
❌ O(V²) space (wasteful if graph has few edges)
❌ Slow to iterate over neighbors: O(V)
    """)
    
    print("\n💡 WE'LL USE ADJACENCY LIST (Python dict)!")
    
    wait_for_enter()

# ============================================================================
# LESSON 3: Breadth-First Search (BFS)
# ============================================================================

def lesson_3():
    """BFS explanation and demo"""
    clear_screen()
    print_header("LESSON 3: Breadth-First Search (BFS)")
    
    print("""
BFS explores a graph LEVEL BY LEVEL, like ripples in water.

Uses: QUEUE (FIFO - First In, First Out)

Algorithm:
1. Start at root, add to queue
2. While queue not empty:
   - Dequeue a vertex
   - Mark it as visited
   - Enqueue all unvisited neighbors
    """)
    
    print("\nExample Graph:")
    print("""
        A
       / \\
      B   C
     / \\   \\
    D   E   F
    """)
    
    wait_for_enter("Press ENTER to watch BFS in action...")
    
    # BFS Demo
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }
    
    def bfs_demo(start):
        visited = set()
        queue = deque([start])
        order = []
        
        print("\n" + "-" * 60)
        print("BFS SIMULATION:")
        print("-" * 60)
        
        step = 1
        while queue:
            print(f"\nStep {step}:")
            print(f"  Queue: {list(queue)}")
            
            vertex = queue.popleft()
            if vertex in visited:
                continue
                
            visited.add(vertex)
            order.append(vertex)
            
            print(f"  Dequeue and visit: {vertex}")
            print(f"  Visited so far: {order}")
            
            neighbors = [n for n in graph[vertex] if n not in visited]
            if neighbors:
                for neighbor in neighbors:
                    if neighbor not in queue:
                        queue.append(neighbor)
                print(f"  Enqueue neighbors: {neighbors}")
            
            time.sleep(0.5)
            step += 1
        
        return order
    
    result = bfs_demo('A')
    
    print("\n" + "=" * 60)
    print(f"FINAL BFS ORDER: {' → '.join(result)}")
    print("=" * 60)
    
    print("""
Notice: We visit ALL neighbors of A (level 1) before ANY of their children (level 2)!

A (level 0) → B, C (level 1) → D, E, F (level 2)
    """)
    
    wait_for_enter()
    
    print("\n" + "-" * 60)
    print("BFS USE CASES:")
    print("-" * 60)
    print("""
✅ Shortest path in UNWEIGHTED graph
✅ Level-order traversal
✅ Social networks: "Degrees of separation"
✅ Web crawlers (explore nearby pages first)
✅ GPS navigation (find nearby locations)
    """)
    
    wait_for_enter()

# ============================================================================
# LESSON 4: Depth-First Search (DFS)
# ============================================================================

def lesson_4():
    """DFS explanation and demo"""
    clear_screen()
    print_header("LESSON 4: Depth-First Search (DFS)")
    
    print("""
DFS explores a graph by going AS DEEP AS POSSIBLE before backtracking.

Uses: STACK (LIFO - Last In, First Out) or RECURSION

Algorithm (Recursive):
1. Start at root, mark as visited
2. For each unvisited neighbor:
   - Recursively visit that neighbor
    """)
    
    print("\nSame Graph:")
    print("""
        A
       / \\
      B   C
     / \\   \\
    D   E   F
    """)
    
    wait_for_enter("Press ENTER to watch DFS in action...")
    
    # DFS Demo
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }
    
    def dfs_demo(vertex, visited, order, depth=0):
        indent = "  " * depth
        print(f"\n{indent}Visit: {vertex} (depth {depth})")
        
        visited.add(vertex)
        order.append(vertex)
        
        print(f"{indent}Visited so far: {order}")
        
        neighbors = [n for n in graph[vertex] if n not in visited]
        if neighbors:
            print(f"{indent}Explore neighbors: {neighbors}")
        else:
            print(f"{indent}No unvisited neighbors, BACKTRACK!")
        
        time.sleep(0.5)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_demo(neighbor, visited, order, depth + 1)
        
        return order
    
    print("\n" + "-" * 60)
    print("DFS SIMULATION (Recursive):")
    print("-" * 60)
    
    visited = set()
    order = []
    result = dfs_demo('A', visited, order)
    
    print("\n" + "=" * 60)
    print(f"FINAL DFS ORDER: {' → '.join(result)}")
    print("=" * 60)
    
    print("""
Notice: We go DEEP (A → B → D) before exploring other branches!

A → B → D (go deep) → backtrack → E → backtrack → backtrack → C → F
    """)
    
    wait_for_enter()
    
    print("\n" + "-" * 60)
    print("DFS USE CASES:")
    print("-" * 60)
    print("""
✅ Pathfinding in mazes
✅ Cycle detection
✅ Topological sorting (task dependencies)
✅ Solving puzzles (Sudoku, N-Queens)
✅ Finding connected components
    """)
    
    wait_for_enter()

# ============================================================================
# LESSON 5: BFS vs DFS Comparison
# ============================================================================

def lesson_5():
    """Compare BFS and DFS"""
    clear_screen()
    print_header("LESSON 5: BFS vs DFS - When to Use Which?")
    
    print("""
Let's compare them side by side!

Graph:
        A
       / \\
      B   C
     / \\   \\
    D   E   F
    """)
    
    print("\n" + "-" * 60)
    print("BFS (Breadth-First Search):")
    print("-" * 60)
    print("""
Order: A → B → C → D → E → F
       (Level 0) (Level 1) (Level 2)

Data Structure: Queue (FIFO)
Strategy: Explore all neighbors before going deeper
Memory: O(V) - stores all vertices at current level
    """)
    
    print("\n" + "-" * 60)
    print("DFS (Depth-First Search):")
    print("-" * 60)
    print("""
Order: A → B → D → E → C → F
       (Goes deep first, then backtracks)

Data Structure: Stack (LIFO) or Recursion
Strategy: Explore as far as possible before backtracking
Memory: O(H) - stores vertices along current path (height)
    """)
    
    wait_for_enter("Press ENTER to see comparison table...")
    
    print("\n" + "=" * 60)
    print("COMPARISON TABLE:")
    print("=" * 60)
    print("""
┌────────────────────┬─────────────────┬──────────────────────┐
│ Aspect             │ BFS             │ DFS                  │
├────────────────────┼─────────────────┼──────────────────────┤
│ Data Structure     │ Queue (FIFO)    │ Stack or Recursion   │
│ Order              │ Level by level  │ Deep first           │
│ Shortest Path      │ ✅ YES          │ ❌ NO                │
│ Memory Usage       │ O(V) broader    │ O(H) height          │
│ Implementation     │ Iterative       │ Recursive (easier!)  │
│ Use Case           │ Nearest first   │ Explore deep         │
└────────────────────┴─────────────────┴──────────────────────┘
    """)
    
    print("\n💡 WHEN TO USE WHICH:")
    print("-" * 60)
    print("""
Use BFS when:
✅ You need the SHORTEST PATH (unweighted graph)
✅ You want to explore NEARBY vertices first
✅ Finding minimum steps/moves

Use DFS when:
✅ You want to explore ALL PATHS
✅ Detecting CYCLES in a graph
✅ Solving MAZES or puzzles
✅ Topological sorting
    """)
    
    wait_for_enter()

# ============================================================================
# LESSON 6: Practical Applications
# ============================================================================

def lesson_6():
    """Real-world applications"""
    clear_screen()
    print_header("LESSON 6: Real-World Applications")
    
    print("""
Graphs are EVERYWHERE in real applications!
    """)
    
    print("\n" + "-" * 60)
    print("1. SOCIAL NETWORKS (Facebook, LinkedIn)")
    print("-" * 60)
    print("""
People = Vertices
Friendships = Edges

BFS Use: Find "degrees of separation"
- Alice → Bob → Charlie (2 degrees)
- "People you may know" (friends of friends)

DFS Use: Find if two people are connected through any path
    """)
    
    wait_for_enter()
    
    print("\n" + "-" * 60)
    print("2. GPS NAVIGATION (Google Maps)")
    print("-" * 60)
    print("""
Intersections = Vertices
Roads = Edges (weighted by distance/time)

BFS Use: Find shortest path (unweighted)
DFS Use: Explore all possible routes

Real navigation: Dijkstra's algorithm (BFS + weights)
    """)
    
    wait_for_enter()
    
    print("\n" + "-" * 60)
    print("3. WEB CRAWLERS (Google Search)")
    print("-" * 60)
    print("""
Web Pages = Vertices
Links = Directed Edges

BFS Use: Crawl web level by level
- Start at homepage
- Visit all linked pages
- Then visit pages linked from those pages

This is how Google indexes the web!
    """)
    
    wait_for_enter()
    
    print("\n" + "-" * 60)
    print("4. DEPENDENCY RESOLUTION (npm, pip)")
    print("-" * 60)
    print("""
Packages = Vertices
Dependencies = Directed Edges

DFS Use: Install dependencies in correct order
- Package A depends on B and C
- B depends on D
- Install order: D → B → C → A (topological sort)

Cycle detection: Prevent circular dependencies!
    """)
    
    wait_for_enter()
    
    print("\n" + "-" * 60)
    print("5. NETWORK TOPOLOGY (DevOps/Cloud Engineering)")
    print("-" * 60)
    print("""
Servers = Vertices
Connections = Edges

BFS Use: Find nearest server (latency)
DFS Use: Check if all servers are connected

Cloud Engineering: AWS VPC topology, Kubernetes cluster
    """)
    
    wait_for_enter()
    
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print("=" * 60)
    print("""
Graphs are the MOST VERSATILE data structure!

They model:
• Relationships (social networks)
• Navigation (maps, GPS)
• Dependencies (package managers)
• Networks (cloud infrastructure)
• Web structure (search engines)

Master graphs → Master real-world problem solving! 🚀
    """)
    
    wait_for_enter()

# ============================================================================
# Main Menu
# ============================================================================

def main():
    """Main tutorial menu"""
    lessons = [
        ("What Are Graphs?", lesson_1),
        ("Graph Representations", lesson_2),
        ("Breadth-First Search (BFS)", lesson_3),
        ("Depth-First Search (DFS)", lesson_4),
        ("BFS vs DFS Comparison", lesson_5),
        ("Real-World Applications", lesson_6)
    ]
    
    current_lesson = 0
    
    while True:
        clear_screen()
        print("=" * 60)
        print("  DAY 6: INTERACTIVE GRAPH TUTORIAL")
        print("=" * 60)
        print("\nLessons:")
        
        for i, (title, _) in enumerate(lessons, 1):
            status = "✅" if i <= current_lesson else "⭕"
            current = " ← YOU ARE HERE" if i == current_lesson + 1 else ""
            print(f"  {status} Lesson {i}: {title}{current}")
        
        print("\n" + "-" * 60)
        print("Commands:")
        print("  [ENTER] - Start/Continue to next lesson")
        print("  [number] - Jump to specific lesson")
        print("  [q] - Quit")
        print("-" * 60)
        
        choice = input("\nYour choice: ").strip().lower()
        
        if choice == 'q':
            print("\n👋 Great work! Now build your own graph in graph.py!")
            break
        elif choice == '':
            if current_lesson < len(lessons):
                lessons[current_lesson][1]()
                current_lesson += 1
            else:
                print("\n🎉 Tutorial complete! Time to implement your own graph!")
                wait_for_enter()
                break
        elif choice.isdigit():
            lesson_num = int(choice) - 1
            if 0 <= lesson_num < len(lessons):
                lessons[lesson_num][1]()
                current_lesson = max(current_lesson, lesson_num + 1)
        
        if current_lesson >= len(lessons):
            clear_screen()
            print("=" * 60)
            print("  🎉 CONGRATULATIONS! TUTORIAL COMPLETE!")
            print("=" * 60)
            print("""
You've learned:
✅ What graphs are and when to use them
✅ Adjacency list representation
✅ Breadth-First Search (BFS) - level by level
✅ Depth-First Search (DFS) - deep first
✅ When to use BFS vs DFS
✅ Real-world applications

Next Step:
📝 Implement your own Graph class in graph.py!

Key methods to implement:
1. add_vertex()
2. add_edge()
3. bfs()
4. dfs()
5. has_path()
6. shortest_path()

Good luck! 🚀
            """)
            wait_for_enter()
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 See you later!")
        sys.exit(0)
