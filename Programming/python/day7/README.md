# Day 7: Week 1 Review & Mastery Assessment 🎯

> **Date:** October 6, 2025  
> **Focus:** Review, practice, and validate Week 1 learning  
> **Time:** 3-4 hours  
> **Goal:** Ensure deep understanding before moving to Week 2

---

## 🎉 Week 1 Complete! What You've Learned

### **Day 1: Python Basics & CLI**
- ✅ Functions, control flow, type hints
- ✅ File I/O and JSON persistence
- ✅ CLI development with argparse
- ✅ **Projects:** Unit Converter, Phone Book, Password Generator

### **Day 2: Arrays & Search**
- ✅ Lists, dynamic arrays
- ✅ Linear search algorithms
- ✅ Sorting with custom keys
- ✅ **Project:** Smart Todo List

### **Day 3: Stacks & Queues**
- ✅ Stack (LIFO) - brackets, command history
- ✅ Queue (FIFO) - task scheduling
- ✅ Priority Queue (heapq)
- ✅ Deque for time-series data
- ✅ **Projects:** Brackets Checker, Command History, Task Queue, System Monitor

### **Day 4: Trees & Recursion**
- ✅ Binary Search Trees
- ✅ Tree traversals (inorder, preorder, postorder, BFS)
- ✅ Recursion patterns
- ✅ **Projects:** BST Implementation, Directory Tree Explorer

### **Day 5: Hash Tables**
- ✅ Hash functions
- ✅ Collision handling (chaining)
- ✅ Load factor and resizing
- ✅ O(1) lookup
- ✅ **Projects:** Custom Hash Table, Word Frequency Analyzer

### **Day 6 Part 1: Graphs - Traversals**
- ✅ Graph representations (adjacency list)
- ✅ BFS (breadth-first search)
- ✅ DFS (depth-first search)
- ✅ Path finding
- ✅ **Project:** Graph Implementation

### **Day 6 Part 2: Graphs - Advanced** (If completed)
- ✅ Weighted graphs
- ✅ Dijkstra's algorithm
- ✅ Cycle detection
- ✅ Topological sort
- ✅ **Project:** Network Topology Analyzer

---

## 📊 Week 1 Stats

**Total Projects:** 15+  
**Lines of Code:** ~4,500+  
**Data Structures Mastered:** 7 (Arrays, Stacks, Queues, Trees, Hash Tables, Graphs, Heaps)  
**Algorithms Learned:** 10+ (Linear search, BFS, DFS, Tree traversals, Dijkstra, etc.)  
**Time Invested:** ~22-24 hours  

---

## 🎯 Day 7 Structure

### **Part 1: Concept Review** (60 min)
Quick review of each data structure with key questions

### **Part 2: Coding Challenges** (90 min)
Apply what you learned to solve real problems

### **Part 3: Mini Capstone Project** (60 min)
Build something that combines multiple data structures

### **Part 4: Self-Assessment** (30 min)
Test your understanding

---

## 📚 Part 1: Concept Review

### Quick Quiz - Test Your Understanding

**Arrays & Lists:**
1. What's the time complexity of accessing an element by index? `O(1)`
2. What's the time complexity of searching for a value? `O(n)`
3. When should you use a list vs a set? _List: order matters, duplicates ok. Set: fast lookup, no duplicates_

**Stacks (LIFO):**
1. What operations does a stack support? `push, pop, peek`
2. Give 3 real-world uses of stacks? _Undo/redo, brackets matching, function call stack_
3. What data structure did we use for stack? `list` or `deque`

**Queues (FIFO):**
1. What's the difference between queue and stack? _Queue: first in first out. Stack: last in first out_
2. What's a priority queue? _Items dequeued by priority, not insertion order_
3. When should you use deque over list? _When you need O(1) operations on both ends_

**Trees:**
1. What makes a Binary Search Tree special? _Left < Parent < Right property_
2. What's the difference between BFS and DFS on a tree? _BFS: level by level. DFS: deep first_
3. What's the average time complexity of BST operations? `O(log n)`

**Hash Tables:**
1. How do hash tables achieve O(1) lookup? _Hash function converts key to array index_
2. What happens when two keys hash to same index? _Collision! Handle with chaining or open addressing_
3. When should load factor trigger a resize? _Typically > 0.7_

**Graphs:**
1. What's the difference between directed and undirected graphs? _Directed: one-way edges. Undirected: bidirectional_
2. When should you use BFS vs DFS? _BFS: shortest path. DFS: explore all paths, detect cycles_
3. What's Dijkstra's algorithm used for? _Shortest path in weighted graphs_

---

## 💻 Part 2: Coding Challenges

### Challenge 1: Valid Parentheses (Stack) ⭐⭐
**Problem:** Check if brackets are balanced: `{[()]}` ✅ vs `{[(])}` ❌

```python
def is_valid_parentheses(s: str) -> bool:
    """
    Given a string containing just the characters 
    '(', ')', '{', '}', '[' and ']', determine if valid.
    
    Examples:
    >>> is_valid_parentheses("()")
    True
    >>> is_valid_parentheses("()[]{}")
    True
    >>> is_valid_parentheses("(]")
    False
    >>> is_valid_parentheses("([)]")
    False
    """
    # TODO: Implement using stack
    pass
```

**Hint:** Push opening brackets, pop and match closing brackets.

---

### Challenge 2: Level Order Traversal (Queue) ⭐⭐
**Problem:** Print tree level by level

```python
def level_order_traversal(root: TreeNode) -> List[List[int]]:
    """
    Given binary tree root, return level order traversal.
    
    Example:
        3
       / \
      9  20
        /  \
       15   7
    
    Output: [[3], [9, 20], [15, 7]]
    """
    # TODO: Implement using BFS with queue
    pass
```

**Hint:** Use queue, track level boundaries.

---

### Challenge 3: Two Sum (Hash Table) ⭐⭐
**Problem:** Find two numbers that add up to target

```python
def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given array of integers, return indices of two numbers 
    that add up to target.
    
    Example:
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]  # nums[0] + nums[1] = 2 + 7 = 9
    """
    # TODO: Implement using hash table for O(n) solution
    pass
```

**Hint:** Store `{value: index}` in dict, look for `target - current`.

---

### Challenge 4: Find Path in Binary Tree (DFS) ⭐⭐⭐
**Problem:** Find path from root to target node

```python
def find_path(root: TreeNode, target: int) -> List[int]:
    """
    Find path from root to node with value = target.
    
    Example:
        5
       / \
      3   8
     / \
    1   4
    
    >>> find_path(root, 4)
    [5, 3, 4]
    """
    # TODO: Implement using DFS
    pass
```

**Hint:** Use recursion, build path as you go, backtrack if wrong.

---

### Challenge 5: Find Islands (Graph DFS) ⭐⭐⭐
**Problem:** Count connected components in grid

```python
def num_islands(grid: List[List[str]]) -> int:
    """
    Given 2D grid of '1' (land) and '0' (water), 
    count number of islands.
    
    Example:
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    
    Output: 3  (two separate islands of 1s)
    """
    # TODO: Implement using DFS to explore each island
    pass
```

**Hint:** Treat grid as graph, DFS from each unvisited land cell.

---

### Challenge 6: Course Schedule (Topological Sort) ⭐⭐⭐⭐
**Problem:** Check if all courses can be completed given prerequisites

```python
def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Check if you can finish all courses given prerequisites.
    prerequisites[i] = [a, b] means to take course a, must take b first.
    
    Example:
    >>> can_finish(2, [[1, 0]])
    True  # Take course 0, then course 1
    
    >>> can_finish(2, [[1, 0], [0, 1]])
    False  # Circular dependency!
    """
    # TODO: Implement using cycle detection or topological sort
    pass
```

**Hint:** Build graph, detect cycle using DFS.

---

## 🏗️ Part 3: Mini Capstone Project

### **Build: Task Dependency Manager**

Combine everything you learned into one practical tool!

**Features:**
1. **Tasks as Graph** - Each task is a vertex
2. **Dependencies as Edges** - Task A depends on Task B
3. **Topological Sort** - Find valid execution order
4. **Priority Queue** - Schedule tasks by priority
5. **Hash Table** - Fast task lookup by ID
6. **Tree View** - Display task hierarchy

**Example:**
```python
manager = TaskManager()

# Add tasks
manager.add_task("deploy", priority=1)
manager.add_task("test", priority=2)
manager.add_task("build", priority=3)
manager.add_task("setup", priority=4)

# Add dependencies
manager.add_dependency("deploy", "test")  # deploy depends on test
manager.add_dependency("test", "build")
manager.add_dependency("build", "setup")

# Get execution order
order = manager.get_execution_order()
print(order)  # ['setup', 'build', 'test', 'deploy']

# Check for circular dependencies
if manager.has_circular_dependency():
    print("⚠️ Cannot execute! Fix dependencies.")

# Get tasks by priority
next_task = manager.get_next_task()
print(next_task)  # 'setup' (highest priority of ready tasks)
```

**Implementation Plan:**
1. Use Graph for dependency tracking
2. Use Hash Table for O(1) task lookup
3. Use Priority Queue for task scheduling
4. Use Topological Sort for execution order
5. Use DFS for cycle detection

---

## 🎯 Part 4: Self-Assessment

### Rate Your Understanding (1-5)

**Data Structures:**
- [ ] Arrays and Lists (1 2 3 4 5)
- [ ] Stacks (1 2 3 4 5)
- [ ] Queues (1 2 3 4 5)
- [ ] Binary Search Trees (1 2 3 4 5)
- [ ] Hash Tables (1 2 3 4 5)
- [ ] Graphs (1 2 3 4 5)

**Algorithms:**
- [ ] Linear Search (1 2 3 4 5)
- [ ] BFS (1 2 3 4 5)
- [ ] DFS (1 2 3 4 5)
- [ ] Dijkstra's Algorithm (1 2 3 4 5)
- [ ] Topological Sort (1 2 3 4 5)

**Skills:**
- [ ] Problem Solving (1 2 3 4 5)
- [ ] Code Organization (1 2 3 4 5)
- [ ] Testing (1 2 3 4 5)
- [ ] Documentation (1 2 3 4 5)

### What to Improve?

**If you scored < 4 on anything:**
- Review that topic's materials
- Redo the practice problems
- Build another project using that concept

**If you scored 4-5 on everything:**
- 🎉 You're ready for Week 2!
- Consider doing bonus challenges
- Start thinking about Week 2 topics

---

## 📝 Reflection Questions

1. **What was the hardest concept this week?**
   - Why was it difficult?
   - How did you overcome it?

2. **What was your favorite project?**
   - What made it enjoyable?
   - What did you learn most from it?

3. **How has your problem-solving approach changed?**
   - Can you break down complex problems better?
   - Do you think about time/space complexity?

4. **What real-world applications can you see?**
   - How would you use graphs in DevOps?
   - Where would hash tables be useful?

5. **Are you ready for Week 2?**
   - What would you like to review?
   - What are you most excited to learn next?

---

## 🎯 Week 2 Preview

**Days 8-14: Advanced Algorithms & Python Patterns**

- **Day 8:** Sorting Algorithms (merge sort, quick sort)
- **Day 9:** Python Patterns (comprehensions, generators)
- **Day 10:** File I/O & Data Processing
- **Day 11:** Error Handling & Logging
- **Day 12:** Decorators & Context Managers
- **Day 13:** HTTP & REST APIs
- **Day 14:** Week 2 Project (Weather Dashboard)

---

## 🏆 Week 1 Accomplishments

**You should be proud! You:**
- ✅ Built 15+ projects from scratch
- ✅ Wrote ~4,500 lines of code
- ✅ Mastered 7 data structures
- ✅ Learned 10+ algorithms
- ✅ Invested 20+ hours of focused learning
- ✅ Developed professional coding habits
- ✅ Created a strong GitHub portfolio

**Week 1 Complete!** 🎉

---

## 📚 Resources for Review

**If you need more practice:**
- [LeetCode Easy Problems](https://leetcode.com) - Filter by data structure
- [VisuAlgo](https://visualgo.net) - Visualize algorithms
- [Python Tutor](https://pythontutor.com) - Step through code
- Your own projects - Review and enhance them!

---

**Take a break, celebrate your progress, and get ready for Week 2!** 🚀

You've built a SOLID foundation. Everything from here builds on what you've learned this week!
