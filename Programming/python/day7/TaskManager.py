"""
V - Visualize & Verify (The "What")

P - Pseudocode (The "How")

C - Code (The "Do")

R - Refine & Reflect (The "Check")
"""

from collections import defaultdict
from typing import List, Dict, Set

class TaskManager:
    def __init__(self):
        # For O(1) task lookup by ID. Stores {task_id: priority}
        self.tasks: Dict[str, int] = {}

        # The graph's adjacency list. Stores {task_B: [task_A, ...]}
        self.graph: Dict[str, List[str]] = defaultdict(list)

    def add_task(self, task_id: str, priority: int = 2):
        # pseudocode: In the self.tasks dictionary, set the key 'task_id' to the value 'priority'.
        self.tasks[task_id] = priority

    def add_dependency(self, task_a: str, task_b: str):
        # This means task_a depends on task_b (B -> A)
        # pseudocode: Append task_a to the list of neighbors for task_b in self.graph.
        self.graph[task_b].append(task_a)

    def get_execution_order(self) -> List[str]:
        # --- This is the Topological Sort algorithm ---

        # pseudocode: Initialize result list and visited/visiting sets.
        result: List[str] = []
        visiting: Set[str] = set()
        visited: Set[str] = set()

        def dfs(task: str):
            # pseudocode: Mark the current task as being "in progress".
            visiting.add(task)  
            visited.add(task)  

            # pseudocode: Explore all the tasks that depend on this one.
            for neighbor in self.graph[task]:
                # pseudocode: If we find a cycle, raise an error.
                if neighbor in visiting:
                    raise Exception(f"Circular dependency detected involving task: {neighbor}")
                
                # pseudocode: If we haven't processed this neighbor before, run DFS on it.
                if neighbor not in visited:
                    dfs(neighbor)  

            # pseudocode: Remove the task from the "in progress" path.
            visiting.remove(task)  

            # pseudocode: Add the completed task to the FRONT of our result list.
            result.insert(0, task)  

        # pseudocode: Loop through all known tasks to start the DFS.
        # We need this to handle tasks that might not be part of any dependency.
        for task in self.tasks:
            if task not in visited:
                dfs(task)  

        # pseudocode: Return the final valid execution order.
        return result
    
# --- Let's test your masterpiece ---

print("--- Test Case 1: Valid Order ---")
manager = TaskManager()
manager.add_task("deploy", priority=1)
manager.add_task("test", priority=2)
manager.add_task("build", priority=3)
manager.add_task("setup", priority=4)

manager.add_dependency("deploy", "test")  # deploy depends on test
manager.add_dependency("test", "build")
manager.add_dependency("build", "setup")

try:
    order = manager.get_execution_order()
    print("Execution Order:", order)
    # Expected Output: ['setup', 'build', 'test', 'deploy']
except Exception as e:
    print(e)


print("\n--- Test Case 2: Circular Dependency ---")
manager_cycle = TaskManager()
manager_cycle.add_task("task_a")
manager_cycle.add_task("task_b")

manager_cycle.add_dependency("task_a", "task_b")
manager_cycle.add_dependency("task_b", "task_a") # B depends on A, A depends on B!

try:
    order = manager_cycle.get_execution_order()
    print("Execution Order:", order)
except Exception as e:
    print(e)
    # Expected Output: An exception saying a circular dependency was detected.