#!/usr/bin/env python3
"""
Day 6 Part 2: Interactive Tutorial - Advanced Graph Algorithms
Learn: Weighted Graphs, Dijkstra's Algorithm, Cycle Detection, Topological Sort
"""

import time
import heapq
from collections import deque
from typing import Dict, List, Tuple, Optional

def clear_screen():
    """Clear the terminal screen."""
    print("\n" * 2)

def print_header(title: str):
    """Print a formatted section header."""
    print("=" * 60)
    print(f"  {title}")
    print("=" * 60)

def print_section(title: str):
    """Print a formatted subsection."""
    print("\n" + "-" * 60)
    print(f"{title}")
    print("-" * 60)

def wait_for_input(message: str = "Press ENTER to continue..."):
    """Wait for user to press ENTER."""
    input(f"\n{message}\n")

class WeightedGraph:
    """Simple weighted graph for demonstrations."""
    
    def __init__(self, directed: bool = False):
        self.graph: Dict[str, List[Tuple[str, int]]] = {}
        self.directed = directed
    
    def add_edge(self, from_vertex: str, to_vertex: str, weight: int):
        """Add weighted edge to graph."""
        if from_vertex not in self.graph:
            self.graph[from_vertex] = []
        if to_vertex not in self.graph:
            self.graph[to_vertex] = []
        
        self.graph[from_vertex].append((to_vertex, weight))
        if not self.directed:
            self.graph[to_vertex].append((from_vertex, weight))
    
    def dijkstra(self, start: str, end: str) -> Tuple[Optional[int], List[str]]:
        """Find shortest weighted path using Dijkstra's algorithm."""
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        parent = {start: None}
        pq = [(0, start)]  # (distance, vertex)
        visited = set()
        
        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            visited.add(current)
            
            if current == end:
                # Reconstruct path
                path = []
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return distances[end], path[::-1]
            
            for neighbor, weight in self.graph[current]:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parent[neighbor] = current
                    heapq.heappush(pq, (distance, neighbor))
        
        return None, []
    
    def display(self):
        """Display the graph."""
        for vertex, edges in sorted(self.graph.items()):
            edge_str = ", ".join([f"{neighbor}({weight})" for neighbor, weight in edges])
            print(f"  {vertex} → [{edge_str}]")


def lesson_1_weighted_graphs():
    """Lesson 1: Introduction to Weighted Graphs."""
    clear_screen()
    print_header("LESSON 1: Weighted Graphs")
    
    print("""
In Day 6 Part 1, we learned about UNWEIGHTED graphs.
All edges were equal - it took 1 step to go from A to B.

But real-world problems often have COSTS:
• 🗺️ Roads have different distances
• 🌐 Network connections have different latencies  
• 💰 Flights have different prices
• ⏱️ Tasks take different amounts of time

A WEIGHTED GRAPH has a VALUE (weight) on each edge.
    """)
    
    wait_for_input()
    
    print_section("EXAMPLE: City Network")
    print("""
Unweighted Graph (from Part 1):
    NYC --- Boston
     |        |
    Philly -- DC

All edges = 1 step. Shortest path NYC → DC = 2 steps

Weighted Graph (real distances in miles):
    NYC --215mi-- Boston
     |              |
    100mi          300mi
     |              |
    Philly -140mi- DC

Now shortest path NYC → DC = 1 direct route? NO!
NYC → Philly → DC = 240 miles (SHORTER!)
NYC → Boston → DC = 515 miles (LONGER!)

🔑 KEY INSIGHT: More steps can be shorter distance!
    """)
    
    wait_for_input()
    
    print_section("Creating a Weighted Graph")
    
    graph = WeightedGraph()
    print("\nBuilding city network...")
    time.sleep(0.5)
    
    graph.add_edge("NYC", "Boston", 215)
    print("  Added: NYC --- 215mi --> Boston")
    time.sleep(0.3)
    
    graph.add_edge("NYC", "Philly", 100)
    print("  Added: NYC --- 100mi --> Philly")
    time.sleep(0.3)
    
    graph.add_edge("Boston", "DC", 300)
    print("  Added: Boston --- 300mi --> DC")
    time.sleep(0.3)
    
    graph.add_edge("Philly", "DC", 140)
    print("  Added: Philly --- 140mi --> DC")
    time.sleep(0.3)
    
    print("\nFull graph:")
    graph.display()
    
    print("""
Notice: Each edge now has a TUPLE: (neighbor, weight)
Not just: ['NYC', 'Boston']
But: [('Boston', 215), ('Philly', 100)]
    """)
    
    wait_for_input()


def lesson_2_dijkstra_intro():
    """Lesson 2: Introduction to Dijkstra's Algorithm."""
    clear_screen()
    print_header("LESSON 2: Dijkstra's Algorithm")
    
    print("""
PROBLEM: BFS finds shortest PATH (fewest edges)
         But NOT shortest DISTANCE (minimum weight)!

NYC → Philly → DC = 3 edges but 240 miles
NYC → DC = 1 edge but maybe 300 miles (if direct)

We need: DIJKSTRA'S ALGORITHM 🎯

Named after: Edsger Dijkstra (1956)
Use Case: Find shortest weighted path in a graph
Examples: GPS navigation, network routing, flight planning
    """)
    
    wait_for_input()
    
    print_section("How Dijkstra Works")
    print("""
Think of it as "greedy BFS with a priority queue":

1. Start at source, set distance = 0
2. Set all other distances = infinity
3. Use PRIORITY QUEUE (min-heap) to always explore closest vertex
4. For each vertex, update neighbor distances if we found shorter path
5. Keep track of parent to reconstruct path

Key Difference from BFS:
• BFS uses QUEUE (FIFO) - explores in order added
• Dijkstra uses PRIORITY QUEUE - explores closest first!
    """)
    
    wait_for_input()
    
    print_section("DIJKSTRA'S ALGORITHM - STEP BY STEP")
    
    print("""
Graph:
    A --1-- B
    |       |
    4       2
    |       |
    C --1-- D

Find shortest path: A → D
    """)
    
    wait_for_input()
    
    print("\n🔍 SIMULATION:")
    print("-" * 60)
    
    steps = [
        {
            "step": 1,
            "action": "Start at A",
            "distances": {"A": 0, "B": "∞", "C": "∞", "D": "∞"},
            "pq": [(0, "A")],
            "current": "A",
            "explanation": "Initialize: A=0, everything else=infinity"
        },
        {
            "step": 2,
            "action": "Visit A, update neighbors",
            "distances": {"A": 0, "B": 1, "C": 4, "D": "∞"},
            "pq": [(1, "B"), (4, "C")],
            "current": "B",
            "explanation": "From A: B=0+1=1, C=0+4=4. Add to priority queue."
        },
        {
            "step": 3,
            "action": "Visit B (smallest in PQ), update neighbors",
            "distances": {"A": 0, "B": 1, "C": 4, "D": 3},
            "pq": [(3, "D"), (4, "C")],
            "current": "D",
            "explanation": "From B: D=1+2=3. PQ picks smallest (D=3) next."
        },
        {
            "step": 4,
            "action": "Visit D, update neighbors",
            "distances": {"A": 0, "B": 1, "C": 4, "D": 3},
            "pq": [(4, "C")],
            "current": "C",
            "explanation": "D→C=3+1=4, but C already=4. No improvement."
        },
        {
            "step": 5,
            "action": "Visit C (no improvements possible)",
            "distances": {"A": 0, "B": 1, "C": 4, "D": 3},
            "pq": [],
            "current": None,
            "explanation": "Done! Shortest path A→D = 3 (via B)"
        }
    ]
    
    for step_data in steps:
        print(f"\nStep {step_data['step']}: {step_data['action']}")
        print(f"  Current vertex: {step_data['current']}")
        print(f"  Distances: {step_data['distances']}")
        print(f"  Priority Queue: {step_data['pq']}")
        print(f"  💡 {step_data['explanation']}")
        time.sleep(1.5)
    
    print("\n" + "=" * 60)
    print("✅ RESULT: Shortest path A → D = 3 (A → B → D)")
    print("Path: A → B → D (not A → C → D which is 5!)")
    print("=" * 60)
    
    wait_for_input()


def lesson_3_dijkstra_live():
    """Lesson 3: Live Dijkstra demonstration."""
    clear_screen()
    print_header("LESSON 3: Dijkstra Live Demo - Server Network")
    
    print("""
SCENARIO: You manage a data center with 5 servers.
You need to route data from ServerA to ServerE.
Network has different latencies (milliseconds).

Let's find the FASTEST route!
    """)
    
    wait_for_input()
    
    print_section("Building Network")
    
    network = WeightedGraph()
    
    # Create a more complex network
    edges = [
        ("ServerA", "ServerB", 4),
        ("ServerA", "ServerC", 2),
        ("ServerB", "ServerC", 1),
        ("ServerB", "ServerD", 5),
        ("ServerC", "ServerD", 8),
        ("ServerC", "ServerE", 10),
        ("ServerD", "ServerE", 2),
    ]
    
    print("\nAdding connections:")
    for from_v, to_v, weight in edges:
        network.add_edge(from_v, to_v, weight)
        print(f"  {from_v} --{weight}ms--> {to_v}")
        time.sleep(0.2)
    
    print("\nComplete network topology:")
    network.display()
    
    wait_for_input("Press ENTER to run Dijkstra...")
    
    print_section("Running Dijkstra: ServerA → ServerE")
    
    distance, path = network.dijkstra("ServerA", "ServerE")
    
    print(f"\n✅ SHORTEST PATH FOUND!")
    print(f"   Distance: {distance}ms")
    print(f"   Route: {' → '.join(path)}")
    
    print(f"\n💡 Explanation:")
    print(f"   Not the direct route ServerA → ServerC → ServerE (12ms)!")
    print(f"   Better: ServerA → ServerC → ServerB → ServerD → ServerE ({distance}ms)")
    print(f"   Saved: {12 - distance}ms per request")
    
    wait_for_input()


def lesson_4_cycle_detection():
    """Lesson 4: Cycle Detection."""
    clear_screen()
    print_header("LESSON 4: Cycle Detection")
    
    print("""
A CYCLE is a path that starts and ends at the same vertex.

Examples:
✅ A → B → C → A (cycle!)
✅ A → B → A (cycle!)
❌ A → B → C → D (no cycle)

WHY DETECT CYCLES?
• Package dependencies: "A needs B, B needs A" = deadlock!
• Task scheduling: "Task1 depends on Task2, Task2 on Task1" = impossible!
• Compiler: Circular imports cause errors
• Finance: Detect circular transactions (money laundering)
    """)
    
    wait_for_input()
    
    print_section("The 3-Color Algorithm (DFS-based)")
    
    print("""
We use DFS with 3 colors to track vertex state:

🔵 WHITE (0): Vertex not yet visited
🟡 GRAY (1):  Vertex being processed (in current DFS path)
🟢 GREEN (2): Vertex completely processed (all descendants visited)

CYCLE DETECTION RULE:
If we reach a GRAY vertex during DFS → CYCLE FOUND! 🚨

Why? Gray means it's in our current path.
Reaching it again = we found a way back!
    """)
    
    wait_for_input()
    
    print_section("Example: Package Dependencies")
    
    print("""
Graph (directed):
    Package A → Package B
    Package B → Package C
    Package C → Package A  ← CYCLE!

Let's trace the algorithm:
    """)
    
    time.sleep(1)
    
    print("""
Start DFS from A:
  1. Visit A, mark GRAY (in progress) 🟡
  2. Explore neighbor B
     3. Visit B, mark GRAY 🟡
     4. Explore neighbor C
        5. Visit C, mark GRAY 🟡
        6. Explore neighbor A
           7. A is GRAY! 🚨 CYCLE DETECTED!
              Path: A → B → C → A

🔴 ERROR: Circular dependency! Cannot install packages.
    """)
    
    wait_for_input()
    
    print_section("Acyclic Graph (No Cycle)")
    
    print("""
Graph (directed):
    Package A → Package B
    Package B → Package C
    Package C → Package D

DFS Trace:
  1. Visit A, mark GRAY 🟡
  2. Visit B, mark GRAY 🟡
  3. Visit C, mark GRAY 🟡
  4. Visit D, mark GRAY 🟡
  5. D has no neighbors, mark GREEN ✅ 🟢
  6. Back to C, all neighbors done, mark GREEN ✅ 🟢
  7. Back to B, all neighbors done, mark GREEN ✅ 🟢
  8. Back to A, all neighbors done, mark GREEN ✅ 🟢

✅ NO CYCLE! Safe to install: D → C → B → A
    """)
    
    wait_for_input()


def lesson_5_topological_sort():
    """Lesson 5: Topological Sort."""
    clear_screen()
    print_header("LESSON 5: Topological Sort")
    
    print("""
TOPOLOGICAL SORT: Linear ordering of vertices such that
for every directed edge A → B, A comes before B.

REAL-WORLD USE CASES:
• 📦 Package installation order
• 🏗️ Project task scheduling
• 🎓 College course prerequisites
• 🔧 Build systems (compile order)
• 🚀 Server startup sequence
    """)
    
    wait_for_input()
    
    print_section("Example: Course Prerequisites")
    
    print("""
Courses (edges show prerequisites):

    Intro_CS → Data_Structures → Algorithms
         ↓            ↓
    OOP_Class  →  Databases
    
Prerequisites:
• Intro_CS must come before Data_Structures
• Intro_CS must come before OOP_Class
• Data_Structures must come before Algorithms
• Data_Structures must come before Databases
• OOP_Class must come before Databases

QUESTION: What order should you take these courses?
    """)
    
    wait_for_input("Press ENTER to see topological sort...")
    
    print("""
TOPOLOGICAL SORT ALGORITHM (DFS-based):
1. Do DFS from each unvisited vertex
2. When vertex is completely processed, add it to STACK
3. Pop stack to get topological order

Why stack? We add vertices AFTER visiting all descendants.
So descendants are added first, then ancestors.
Reversing (stack) gives correct order!
    """)
    
    time.sleep(1)
    
    print("\n🔍 DFS Traversal:")
    print("-" * 60)
    
    print("""
Visit Intro_CS:
  Visit Data_Structures:
    Visit Algorithms:
      (No dependencies, finish) → Add to stack: [Algorithms]
    Visit Databases:
      (No dependencies, finish) → Add to stack: [Algorithms, Databases]
    (Finished Data_Structures) → Add to stack: [Algorithms, Databases, Data_Structures]
  Visit OOP_Class:
    (Already visited Databases)
    (Finished OOP_Class) → Add to stack: [Algorithms, Databases, Data_Structures, OOP_Class]
  (Finished Intro_CS) → Add to stack: [Algorithms, Databases, Data_Structures, OOP_Class, Intro_CS]
    """)
    
    print("\n✅ TOPOLOGICAL ORDER (reverse of stack):")
    print("   1. Intro_CS")
    print("   2. Data_Structures")
    print("   3. OOP_Class")
    print("   4. Databases")
    print("   5. Algorithms")
    
    print("\n💡 Valid order! All prerequisites satisfied.")
    
    wait_for_input()
    
    print_section("Key Properties")
    
    print("""
IMPORTANT:
• Topological sort ONLY works on DAGs (Directed Acyclic Graphs)
• If graph has cycle → NO topological order exists!
• Multiple valid orders may exist (not unique)
• Time Complexity: O(V + E) - same as DFS

Example: OOP_Class could come before OR after Data_Structures
Both are valid as long as Intro_CS comes first!
    """)
    
    wait_for_input()


def lesson_6_comparison():
    """Lesson 6: Algorithm Comparison."""
    clear_screen()
    print_header("LESSON 6: Algorithm Comparison & When to Use")
    
    print("""
Let's compare all the graph algorithms you've learned!
    """)
    
    wait_for_input()
    
    print_section("ALGORITHM COMPARISON TABLE")
    print("""
┌──────────────────┬─────────────┬─────────────────┬──────────────────────┐
│ Algorithm        │ Complexity  │ Data Structure  │ Use Case             │
├──────────────────┼─────────────┼─────────────────┼──────────────────────┤
│ BFS              │ O(V + E)    │ Queue           │ Shortest path        │
│                  │             │                 │ (unweighted)         │
├──────────────────┼─────────────┼─────────────────┼──────────────────────┤
│ DFS              │ O(V + E)    │ Stack/Recursion │ Explore all paths    │
│                  │             │                 │ Detect cycles        │
├──────────────────┼─────────────┼─────────────────┼──────────────────────┤
│ Dijkstra         │ O((V+E)logV)│ Priority Queue  │ Shortest path        │
│                  │             │ (Min Heap)      │ (weighted, non-neg)  │
├──────────────────┼─────────────┼─────────────────┼──────────────────────┤
│ Cycle Detection  │ O(V + E)    │ Stack/Recursion │ Find cycles          │
│ (3-color DFS)    │             │ + Color array   │ Validate DAG         │
├──────────────────┼─────────────┼─────────────────┼──────────────────────┤
│ Topological Sort │ O(V + E)    │ Stack/Recursion │ Dependency order     │
│                  │             │ + Stack         │ Task scheduling      │
└──────────────────┴─────────────┴─────────────────┴──────────────────────┘
    """)
    
    wait_for_input()
    
    print_section("DECISION TREE: Which Algorithm?")
    
    print("""
START: I have a graph problem...

Q1: Is the graph weighted?
    ├─ NO → Use BFS or DFS
    │   └─ Q2: Need shortest path?
    │       ├─ YES → Use BFS
    │       └─ NO → Use DFS
    │
    └─ YES → Q3: All weights positive?
        ├─ YES → Use Dijkstra
        └─ NO → Use Bellman-Ford (not covered today)

Q4: Need to detect cycles?
    └─ Use DFS with 3-color algorithm

Q5: Need dependency ordering?
    └─ Use Topological Sort (requires no cycles!)
    """)
    
    wait_for_input()
    
    print_section("REAL-WORLD SCENARIOS")
    
    scenarios = [
        {
            "problem": "🗺️ GPS Navigation (Google Maps)",
            "graph": "Cities = vertices, Roads = weighted edges (distance/time)",
            "algorithm": "Dijkstra's Algorithm",
            "why": "Need shortest DISTANCE, graph is weighted"
        },
        {
            "problem": "📦 Package Manager (npm install)",
            "graph": "Packages = vertices, Dependencies = directed edges",
            "algorithm": "Topological Sort + Cycle Detection",
            "why": "Need install order, detect circular dependencies"
        },
        {
            "problem": "🌐 Social Network (LinkedIn)",
            "graph": "People = vertices, Connections = unweighted edges",
            "algorithm": "BFS",
            "why": "Find degrees of separation (shortest path, unweighted)"
        },
        {
            "problem": "🕷️ Web Crawler (Google Bot)",
            "graph": "Pages = vertices, Links = directed edges",
            "algorithm": "BFS",
            "why": "Explore nearby pages first, level by level"
        },
        {
            "problem": "🏗️ Build System (Makefile)",
            "graph": "Files = vertices, Dependencies = directed edges",
            "algorithm": "Topological Sort",
            "why": "Compile in correct order (A depends on B → compile B first)"
        },
        {
            "problem": "🔧 Server Startup Sequence",
            "graph": "Services = vertices, Dependencies = directed edges",
            "algorithm": "Topological Sort + Cycle Detection",
            "why": "Start services in order, detect circular dependencies"
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{i}. {scenario['problem']}")
        print(f"   Graph: {scenario['graph']}")
        print(f"   ✅ Use: {scenario['algorithm']}")
        print(f"   💡 Why: {scenario['why']}")
        time.sleep(1)
    
    wait_for_input()


def main_menu():
    """Display main menu and handle navigation."""
    lessons = [
        ("Lesson 1: Weighted Graphs", lesson_1_weighted_graphs),
        ("Lesson 2: Dijkstra's Algorithm - Introduction", lesson_2_dijkstra_intro),
        ("Lesson 3: Dijkstra's Algorithm - Live Demo", lesson_3_dijkstra_live),
        ("Lesson 4: Cycle Detection", lesson_4_cycle_detection),
        ("Lesson 5: Topological Sort", lesson_5_topological_sort),
        ("Lesson 6: Algorithm Comparison", lesson_6_comparison),
    ]
    
    current_lesson = 0
    
    while True:
        clear_screen()
        print_header("DAY 6 PART 2: ADVANCED GRAPH ALGORITHMS")
        
        print("\nLessons:")
        for i, (title, _) in enumerate(lessons):
            if i < current_lesson:
                status = "✅"
            elif i == current_lesson:
                status = "⭕"
                title += " ← YOU ARE HERE"
            else:
                status = "⭕"
            print(f"  {status} {title}")
        
        print("\n" + "-" * 60)
        print("Commands:")
        print("  [ENTER] - Start/Continue to next lesson")
        print("  [number] - Jump to specific lesson")
        print("  [q] - Quit")
        print("-" * 60)
        
        choice = input("\nYour choice: ").strip().lower()
        
        if choice == 'q':
            print("\n👋 See you later! Good luck with the implementation!")
            break
        elif choice.isdigit():
            lesson_num = int(choice) - 1
            if 0 <= lesson_num < len(lessons):
                current_lesson = lesson_num
                lessons[current_lesson][1]()
                current_lesson += 1
        elif choice == '':
            if current_lesson < len(lessons):
                lessons[current_lesson][1]()
                current_lesson += 1
            else:
                # All lessons complete
                clear_screen()
                print_header("🎉 CONGRATULATIONS! TUTORIAL COMPLETE!")
                print("""
You've mastered advanced graph algorithms!

✅ Weighted Graphs - Edges with costs
✅ Dijkstra's Algorithm - Shortest weighted path
✅ Cycle Detection - Find circular dependencies
✅ Topological Sort - Dependency ordering

NEXT STEP:
📝 Implement these in graph.py!
🏗️ Build the Network Topology Analyzer!

Methods to implement:
1. add_weighted_edge()
2. dijkstra()
3. has_cycle()
4. topological_sort()

Good luck! 🚀
                """)
                wait_for_input("Press ENTER to exit...")
                break


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
