#!/usr/bin/env python3
"""
Day 6: Graph Implementation with BFS and DFS
Build a complete graph data structure!
"""

from collections import deque
from typing import List, Optional, Set, Dict, Any

class Graph:
    """
    Graph data structure using adjacency list representation.
    
    Supports:
    - Directed and undirected graphs
    - Weighted edges (optional)
    - BFS and DFS traversals
    - Path finding
    """
    
    def __init__(self, directed: bool = False):
        """
        Initialize an empty graph.
        
        Args:
            directed: If True, edges are directional (A→B doesn't mean B→A)
                     If False, edges are bidirectional (A↔B)
        
        Example:
            >>> g = Graph(directed=False)  # Friendship graph
            >>> g = Graph(directed=True)   # Twitter follow graph
        """
        self.graph: Dict[Any, List[Any]] = {}  # adjacency list
        self.directed = directed
    
    def add_vertex(self, vertex: Any) -> None:
        """
        Add a new vertex to the graph.
        
        Args:
            vertex: The vertex to add (can be any hashable type)
        
        Time Complexity: O(1)
        
        Example:
            >>> g = Graph()
            >>> g.add_vertex("Alice")
            >>> g.add_vertex("Bob")
        
        TODO: Implement this method
        Algorithm:
        1. Check if vertex already exists (if not in self.graph)
        2. If new, add it with an empty list of neighbors: self.graph[vertex] = []
        """
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, v1: Any, v2: Any, weight: Optional[int] = None) -> None:
        """
        Add an edge between two vertices.
        
        Args:
            v1: First vertex
            v2: Second vertex
            weight: Optional edge weight (for weighted graphs)
        
        Time Complexity: O(1)
        
        Behavior:
        - Undirected graph: Adds edge in both directions (v1↔v2)
        - Directed graph: Adds edge in one direction (v1→v2)
        
        Example:
            >>> g = Graph(directed=False)
            >>> g.add_vertex("Alice")
            >>> g.add_vertex("Bob")
            >>> g.add_edge("Alice", "Bob")  # Alice ↔ Bob
        
        TODO: Implement this method
        Algorithm:
        1. Make sure both vertices exist (call add_vertex if needed)
        2. Add v2 to v1's neighbor list
        3. If undirected graph, also add v1 to v2's neighbor list
        
        Note: For now, ignore weight (we'll use it tomorrow in Day 7)
        """
        self.add_vertex(v1)
        self.add_vertex(v2)

        self.graph[v1].append(v2)
        if not self.directed:
            self.graph[v2].append(v1)

    def get_vertices(self) -> List[Any]:
        """
        Get all vertices in the graph.
        
        Returns:
            List of all vertices
        
        Time Complexity: O(V)
        """
        return list(self.graph.keys())
    
    def get_neighbors(self, vertex: Any) -> List[Any]:
        """
        Get all neighbors of a vertex.
        
        Args:
            vertex: The vertex to get neighbors for
        
        Returns:
            List of neighboring vertices
        
        Time Complexity: O(1)
        """
        return self.graph.get(vertex, [])
    
    def bfs(self, start: Any) -> List[Any]:
        """
        Breadth-First Search traversal from start vertex.
        
        Args:
            start: Starting vertex
        
        Returns:
            List of vertices in BFS order
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        
        Algorithm:
        1. Create a queue, add start vertex
        2. Create a visited set to track visited vertices
        3. While queue is not empty:
           a. Dequeue a vertex
           b. If not visited, mark it as visited and add to result
           c. Enqueue all unvisited neighbors
        4. Return the result list
        
        Example:
            Graph:
                A
               / \\
              B   C
             / \\
            D   E
            
            >>> g.bfs("A")
            ['A', 'B', 'C', 'D', 'E']
        
        TODO: Implement this method
        Use collections.deque for the queue (already imported)
        """
        queue = deque([start])

        visited = set()
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result
    
    def dfs(self, start: Any) -> List[Any]:
        """
        Depth-First Search traversal from start vertex.
        
        Args:
            start: Starting vertex
        
        Returns:
            List of vertices in DFS order
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        
        Algorithm (Recursive):
        1. Create a visited set
        2. Create a result list
        3. Call recursive helper function:
           a. Mark current vertex as visited
           b. Add to result list
           c. For each unvisited neighbor:
              - Recursively visit neighbor
        4. Return the result list
        
        Example:
            Graph:
                A
               / \\
              B   C
             / \\
            D   E
            
            >>> g.dfs("A")
            ['A', 'B', 'D', 'E', 'C']  (goes deep first!)
        
        TODO: Implement this method
        You'll need a helper function for recursion
        """
        visited = set()
        result = []

        def dfs_helper(vertex: Any):
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        dfs_helper(neighbor)

        dfs_helper(start)
        return result   
    
    def has_path(self, start: Any, end: Any) -> bool:
        """
        Check if a path exists from start to end vertex.
        
        Args:
            start: Starting vertex
            end: Destination vertex
        
        Returns:
            True if path exists, False otherwise
        
        Time Complexity: O(V + E)
        
        Algorithm (using BFS):
        1. If start == end, return True
        2. Use BFS to explore from start
        3. If we reach end during BFS, return True
        4. If BFS completes without finding end, return False
        
        Example:
            >>> g.add_edge("A", "B")
            >>> g.add_edge("B", "C")
            >>> g.has_path("A", "C")
            True
            >>> g.has_path("C", "A")  # In directed graph
            False
        
        TODO: Implement this method
        Hint: Similar to BFS, but stop early if you find the end vertex
        """
        if start == end:
            return True
        
        queue = deque([start])
        visited = set()

        while queue:
            vertex = queue.popleft()
            if vertex == end:
                return True
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return False
    def shortest_path(self, start: Any, end: Any) -> Optional[List[Any]]:
        """
        Find shortest path from start to end (unweighted graph).
        
        Args:
            start: Starting vertex
            end: Destination vertex
        
        Returns:
            List of vertices in shortest path, or None if no path exists
        
        Time Complexity: O(V + E)
        
        Algorithm (BFS with parent tracking):
        1. Use BFS but track parent of each vertex
        2. When we reach end, reconstruct path by following parents
        3. Reverse the path (since we built it backwards)
        
        Example:
            >>> g.add_edge("A", "B")
            >>> g.add_edge("B", "C")
            >>> g.add_edge("A", "D")
            >>> g.add_edge("D", "C")
            >>> g.shortest_path("A", "C")
            ['A', 'D', 'C']  or  ['A', 'B', 'C']  (both length 3)
        
        TODO: Implement this method
        Hint: Use a dictionary to store parent of each vertex during BFS
        """
        if start == end:
            return [start]
        
        queue = deque([start])
        visited = set()
        parent = {start: None}  # Track parent of each vertex

        while queue:
            vertex = queue.popleft()
            if vertex == end:
                # Reconstruct path
                path = []
                while vertex is not None:
                    path.append(vertex)
                    vertex = parent[vertex]
                return path[::-1]  # Reverse the path
            
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    if neighbor not in visited and neighbor not in parent:
                        parent[neighbor] = vertex
                        queue.append(neighbor)
        
        return None  # No path found
    
    def __str__(self) -> str:
        """String representation of the graph."""
        result = "Graph ({})\n".format(
            "directed" if self.directed else "undirected"
        )
        result += "-" * 40 + "\n"
        
        for vertex in sorted(self.graph.keys(), key=str):
            neighbors = self.graph[vertex]
            arrow = " → " if self.directed else " ↔ "
            if neighbors:
                result += f"{vertex}{arrow}{neighbors}\n"
            else:
                result += f"{vertex} (isolated)\n"
        
        return result


# ============================================================================
# Testing Section
# ============================================================================

def test_graph():
    """Test the Graph implementation."""
    print("=" * 60)
    print("  TESTING GRAPH IMPLEMENTATION")
    print("=" * 60)
    
    # Test 1: Undirected Graph (Social Network)
    print("\nTEST 1: Undirected Graph (Friendships)")
    print("-" * 60)
    g = Graph(directed=False)
    
    # Add vertices
    g.add_vertex("Alice")
    g.add_vertex("Bob")
    g.add_vertex("Charlie")
    g.add_vertex("Diana")
    
    # Add edges (friendships)
    g.add_edge("Alice", "Bob")
    g.add_edge("Bob", "Charlie")
    g.add_edge("Charlie", "Diana")
    g.add_edge("Alice", "Charlie")  # Direct friendship
    
    print(g)
    
    print("\nBFS from Alice:")
    bfs_result = g.bfs("Alice")
    print(f"  {bfs_result}")
    assert len(bfs_result) == 4, "❌ BFS should visit all 4 vertices"
    print("  ✅ BFS works!")
    
    print("\nDFS from Alice:")
    dfs_result = g.dfs("Alice")
    print(f"  {dfs_result}")
    assert len(dfs_result) == 4, "❌ DFS should visit all 4 vertices"
    print("  ✅ DFS works!")
    
    print("\nPath from Alice to Diana:")
    has_path = g.has_path("Alice", "Diana")
    print(f"  Path exists: {has_path}")
    assert has_path, "❌ Path should exist"
    print("  ✅ has_path works!")
    
    shortest = g.shortest_path("Alice", "Diana")
    print(f"  Shortest path: {shortest}")
    assert shortest is not None, "❌ Should find a path"
    print("  ✅ shortest_path works!")
    
    # Test 2: Directed Graph (Twitter Follows)
    print("\n" + "=" * 60)
    print("TEST 2: Directed Graph (Twitter Follows)")
    print("-" * 60)
    g2 = Graph(directed=True)
    
    g2.add_vertex("Alice")
    g2.add_vertex("Bob")
    g2.add_vertex("Charlie")
    
    # Alice follows Bob, Bob follows Charlie
    g2.add_edge("Alice", "Bob")
    g2.add_edge("Bob", "Charlie")
    # Note: Charlie doesn't follow anyone
    
    print(g2)
    
    print("\nPath tests:")
    print(f"  Alice → Charlie: {g2.has_path('Alice', 'Charlie')}")
    assert g2.has_path("Alice", "Charlie"), "❌ Path should exist"
    
    print(f"  Charlie → Alice: {g2.has_path('Charlie', 'Alice')}")
    assert not g2.has_path("Charlie", "Alice"), "❌ Path should NOT exist"
    
    print("  ✅ Directed graph works correctly!")
    
    # Test 3: Disconnected Graph
    print("\n" + "=" * 60)
    print("TEST 3: Disconnected Graph")
    print("-" * 60)
    g3 = Graph(directed=False)
    
    # Island 1
    g3.add_edge("A", "B")
    g3.add_edge("B", "C")
    
    # Island 2 (disconnected)
    g3.add_edge("X", "Y")
    
    print(g3)
    
    print("\nPath tests:")
    print(f"  A → C: {g3.has_path('A', 'C')}")
    assert g3.has_path("A", "C"), "❌ Path should exist within island"
    
    print(f"  A → X: {g3.has_path('A', 'X')}")
    assert not g3.has_path("A", "X"), "❌ Path should NOT exist across islands"
    
    print("  ✅ Handles disconnected components!")
    
    # Test 4: Cyclic Graph
    print("\n" + "=" * 60)
    print("TEST 4: Cyclic Graph")
    print("-" * 60)
    g4 = Graph(directed=True)
    
    # Create a cycle: A → B → C → A
    g4.add_edge("A", "B")
    g4.add_edge("B", "C")
    g4.add_edge("C", "A")
    
    print(g4)
    
    print("\nBFS from A (should handle cycle):")
    bfs_cycle = g4.bfs("A")
    print(f"  {bfs_cycle}")
    assert len(bfs_cycle) == 3, "❌ Should visit each vertex once"
    print("  ✅ Handles cycles correctly!")
    
    # Final Summary
    print("\n" + "=" * 60)
    print("  🎉 ALL TESTS PASSED!")
    print("=" * 60)
    print("""
Congratulations! Your Graph implementation works correctly!

You've successfully implemented:
✅ add_vertex() and add_edge()
✅ BFS traversal (breadth-first)
✅ DFS traversal (depth-first)
✅ has_path() (path existence check)
✅ shortest_path() (BFS-based pathfinding)

Your graph correctly handles:
✅ Undirected graphs (friendships)
✅ Directed graphs (follows)
✅ Disconnected components
✅ Cycles

Next up: Day 7 - More advanced graph algorithms!
    """)


if __name__ == "__main__":
    test_graph()
