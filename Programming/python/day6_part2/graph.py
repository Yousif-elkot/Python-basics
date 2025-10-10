#!/usr/bin/env python3
"""
Day 6 Part 2: Advanced Graph Algorithms Implementation
Implement: Weighted graphs, Dijkstra, Cycle Detection, Topological Sort
"""

import heapq
from collections import deque
from typing import Dict, List, Tuple, Optional, Set
from enum import Enum


class Color(Enum):
    """Colors for cycle detection (3-color algorithm)."""
    WHITE = 0  # Not visited
    GRAY = 1   # Being processed (in current DFS path)
    BLACK = 2  # Completely processed


class Graph:
    """
    Advanced Graph implementation with weighted edges.
    Supports both directed and undirected graphs.
    """
    
    def __init__(self, directed: bool = False):
        """
        Initialize an empty graph.
        
        Args:
            directed: If True, edges are one-way. If False, edges are bidirectional.
        """
        self.graph: Dict[str, List[Tuple[str, int]]] = {}
        self.directed = directed
    
    def add_vertex(self, vertex: str) -> None:
        """
        Add a vertex to the graph.
        
        Args:
            vertex: The vertex to add
        """
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, from_vertex: str, to_vertex: str, weight: int = 1) -> None:
        """
        Add an edge between two vertices with optional weight.
        
        Args:
            from_vertex: Starting vertex
            to_vertex: Ending vertex
            weight: Weight/cost of the edge (default: 1)
        """
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.graph[from_vertex].append((to_vertex, weight))
        if not self.directed:
            self.graph[to_vertex].append((from_vertex, weight))


    def get_neighbors(self, vertex: str) -> List[Tuple[str, int]]:
        """
        Get all neighbors of a vertex with their weights.
        
        Args:
            vertex: The vertex to get neighbors for
            
        Returns:
            List of tuples (neighbor, weight)
        """
        return self.graph.get(vertex, [])
    
    
    def dijkstra(self, start: str, end: str) -> Tuple[Optional[int], List[str]]:
        """
        Find shortest weighted path using Dijkstra's algorithm.
        
        Args:
            start: Starting vertex
            end: Ending vertex
            
        Returns:
            Tuple of (total_distance, path)
            If no path exists, returns (None, [])
        
        Algorithm:
        1. Initialize distances: start=0, all others=infinity
        2. Use priority queue (min-heap) to track vertices by distance
        3. Keep parent dict to reconstruct path
        4. While queue not empty:
           - Pop vertex with smallest distance
           - If it's the end vertex, reconstruct and return path
           - For each neighbor, check if we found shorter path
           - If yes, update distance and parent, add to queue
        """
        # TODO: Implement Dijkstra's algorithm
        # Hint: Use heapq for priority queue: heapq.heappush() and heapq.heappop()
        # Data structures you'll need:
        # - distances: dict mapping vertex to current best distance
        # - parent: dict mapping vertex to its parent in shortest path
        # - pq: priority queue as list of tuples (distance, vertex)
        # - visited: set of vertices we've processed
        
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        parent = {start: None}
        pq = [(0, start)]  # (distance, vertex)
        visited: Set[str] = set()

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            if current_vertex == end:
                # Reconstruct path
                path = []
                while current_vertex is not None:
                    path.append(current_vertex)
                    current_vertex = parent[current_vertex]
                return distances[end], path[::-1]
            
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parent[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))

        return None, [] #no path found

    def has_cycle(self) -> bool:
        """
        Detect if graph contains a cycle using 3-color DFS algorithm.
        
        Returns:
            True if cycle exists, False otherwise
            
        Algorithm (for directed graph):
        1. Color all vertices WHITE (unvisited)
        2. For each WHITE vertex, do DFS:
           - Mark vertex GRAY (in current path)
           - Visit all neighbors
           - If neighbor is GRAY, cycle found!
           - If neighbor is WHITE, recursively visit
           - After visiting all neighbors, mark BLACK (done)
        """
        # TODO: Implement cycle detection
        # Hint: Use 3-color algorithm with DFS
        # Create helper function: _has_cycle_util(vertex, color, parent)
        
        color = {vertex: Color.WHITE for vertex in self.graph}

        def has_cycle_util(vertex: str) -> bool:
            #mark vertex as GRAY (current path)
            color[vertex] = Color.GRAY

            #visit all neighbors
            for nieghbor, _ in self.graph[vertex]:
                #if nieghbour is white, recurse
                if color[nieghbor] == Color.WHITE:
                    if has_cycle_util(nieghbor):
                        return True
            
                elif color[nieghbor] == Color.GRAY:
                    return True
                
            # mark vertex as black (done)
            color[vertex] = Color.BLACK
            return False
        
        # check from unvisited vertex
        for vertex in self.graph:
            if color[vertex] == Color.WHITE:
                if has_cycle_util(vertex):
                    return True
        return False

    def topological_sort(self) -> Optional[List[str]]:
        """
        Return topological ordering of vertices (only for DAGs).
        
        Returns:
            List of vertices in topological order
            None if graph has a cycle (not a DAG)
            
        Algorithm:
        1. First check if graph has cycle (can't sort if cyclic!)
        2. Do DFS from each unvisited vertex
        3. When vertex is completely processed, add to stack
        4. Return reversed stack (or pop all elements)
        
        Example:
            A → B → C
            A → D
            D → C
            
            Valid order: [A, D, B, C] or [A, B, D, C]
        """
        # TODO: Implement topological sort
        # Hint: Use DFS + stack
        # Steps:
        # 1. Check for cycles first (return None if cycle exists)
        # 2. Create visited set and result stack
        # 3. Create helper function: _topo_sort_util(vertex, visited, stack)
        # 4. For each unvisited vertex, call helper
        # 5. Return reversed stack
        
        if self.has_cycle():
            return None
        
        visited = set()
        stack = []

        # helper function for DFS
        def topo_sort_util(vertex: str):
            visited.add(vertex)

            #visit all nieghbours
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    topo_sort_util(neighbor)

            # add to stack after visiting all
            stack.append(vertex)

        # do DFS from each unvisited vertex
        for vertex in self.graph:
            if vertex not in visited:
                topo_sort_util(vertex)

        # Stack is built in correct order (dependencies added last, so they appear first)
        return stack
    
    def display(self) -> None:
        """Display the graph in a readable format."""
        if not self.graph:
            print("Empty graph")
            return
        
        arrow = "→" if self.directed else "↔"
        print(f"\nGraph ({'directed' if self.directed else 'undirected'})")
        print("-" * 40)
        
        for vertex in sorted(self.graph.keys()):
            edges = self.graph[vertex]
            if edges:
                edge_strs = [f"{neighbor}({weight})" for neighbor, weight in edges]
                print(f"{vertex} {arrow} {edge_strs}")
            else:
                print(f"{vertex} (isolated)")


# ============================================================
#  TESTS - Run this file to test your implementation
# ============================================================

def test_weighted_graph():
    """Test weighted graph and Dijkstra's algorithm."""
    print("=" * 60)
    print("  TEST 1: Dijkstra's Algorithm (Shortest Weighted Path)")
    print("=" * 60)
    
    graph = Graph(directed=False)
    
    # Create city network
    graph.add_edge("NYC", "Boston", 215)
    graph.add_edge("NYC", "Philly", 100)
    graph.add_edge("Boston", "DC", 300)
    graph.add_edge("Philly", "DC", 140)
    
    print("\nCity Network:")
    graph.display()
    
    print("\n🔍 Finding shortest path: NYC → DC")
    distance, path = graph.dijkstra("NYC", "DC")
    
    if distance is not None:
        print(f"  Distance: {distance} miles")
        print(f"  Path: {' → '.join(path)}")
        
        # Verify it's the shortest
        if distance == 240 and path == ["NYC", "Philly", "DC"]:
            print("  ✅ Correct! NYC → Philly → DC is shorter than NYC → Boston → DC")
        else:
            print(f"  ❌ Expected distance 240 and path ['NYC', 'Philly', 'DC']")
    else:
        print("  ❌ No path found (should exist!)")
    
    print()


def test_cycle_detection():
    """Test cycle detection."""
    print("=" * 60)
    print("  TEST 2: Cycle Detection")
    print("=" * 60)
    
    # Test 1: Graph WITH cycle
    print("\nTest 2a: Cyclic Graph")
    cyclic = Graph(directed=True)
    cyclic.add_edge("A", "B")
    cyclic.add_edge("B", "C")
    cyclic.add_edge("C", "A")  # Creates cycle!
    
    cyclic.display()
    
    has_cycle = cyclic.has_cycle()
    print(f"\nHas cycle? {has_cycle}")
    if has_cycle:
        print("  ✅ Correct! Detected cycle A → B → C → A")
    else:
        print("  ❌ Should detect cycle!")
    
    # Test 2: Graph WITHOUT cycle
    print("\n" + "-" * 60)
    print("Test 2b: Acyclic Graph (DAG)")
    acyclic = Graph(directed=True)
    acyclic.add_edge("A", "B")
    acyclic.add_edge("B", "C")
    acyclic.add_edge("A", "D")
    acyclic.add_edge("D", "C")
    
    acyclic.display()
    
    has_cycle = acyclic.has_cycle()
    print(f"\nHas cycle? {has_cycle}")
    if not has_cycle:
        print("  ✅ Correct! No cycle detected")
    else:
        print("  ❌ Should NOT detect cycle!")
    
    print()


def test_topological_sort():
    """Test topological sort."""
    print("=" * 60)
    print("  TEST 3: Topological Sort (Package Dependencies)")
    print("=" * 60)
    
    # Package dependency graph
    packages = Graph(directed=True)
    packages.add_edge("app", "auth")
    packages.add_edge("app", "database")
    packages.add_edge("auth", "database")
    packages.add_edge("auth", "utils")
    packages.add_edge("database", "utils")
    
    print("\nPackage Dependencies:")
    packages.display()
    
    print("\n🔍 Finding installation order...")
    order = packages.topological_sort()
    
    if order:
        print(f"  Install order: {' → '.join(order)}")
        
        # Verify constraints
        valid = True
        order_map = {pkg: i for i, pkg in enumerate(order)}
        
        # Check all dependencies are satisfied
        if "utils" in order_map and "database" in order_map:
            if order_map["utils"] < order_map["database"]:
                print("  ✅ utils installed before database")
            else:
                print("  ❌ utils should be installed before database")
                valid = False
        
        if "database" in order_map and "auth" in order_map:
            if order_map["database"] < order_map["auth"]:
                print("  ✅ database installed before auth")
            else:
                print("  ❌ database should be installed before auth")
                valid = False
        
        if "auth" in order_map and "app" in order_map:
            if order_map["auth"] < order_map["app"]:
                print("  ✅ auth installed before app")
            else:
                print("  ❌ auth should be installed before app")
                valid = False
        
        if valid:
            print("\n  ✅ Topological sort correct!")
    else:
        print("  ❌ Should return valid order!")
    
    print()


def test_cycle_in_topological():
    """Test that topological sort returns None for cyclic graphs."""
    print("=" * 60)
    print("  TEST 4: Topological Sort on Cyclic Graph")
    print("=" * 60)
    
    cyclic = Graph(directed=True)
    cyclic.add_edge("A", "B")
    cyclic.add_edge("B", "C")
    cyclic.add_edge("C", "A")  # Cycle!
    
    print("\nCyclic dependencies:")
    cyclic.display()
    
    print("\n🔍 Attempting topological sort...")
    order = cyclic.has_cycle()
    
    if cyclic.topological_sort() is None:
        print("  ✅ Correctly returned None (can't sort cyclic graph!)")
    else:
        print("  ❌ Should return None for cyclic graph!")
    
    print()


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("  TESTING ADVANCED GRAPH IMPLEMENTATION")
    print("=" * 60)
    print()
    
    test_weighted_graph()
    test_cycle_detection()
    test_topological_sort()
    test_cycle_in_topological()
    
    print("=" * 60)
    print("  🎉 ALL TESTS COMPLETE!")
    print("=" * 60)
    print("""
If all tests passed:
✅ Dijkstra's algorithm works correctly
✅ Cycle detection works correctly  
✅ Topological sort works correctly

Next: Build the Network Topology Analyzer! 🚀
    """)


if __name__ == "__main__":
    run_all_tests()
