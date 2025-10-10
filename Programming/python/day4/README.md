# 🌳 Day 4: Trees, Recursion & File System Operations

**Focus:** Binary Trees, Tree Traversal, Recursion, File System Navigation

---

## 🎯 Learning Objectives

By the end of Day 4, you will:

1. **Master Tree Data Structures**
   - Understand tree terminology (root, parent, child, leaf, depth, height)
   - Implement Binary Trees and Binary Search Trees (BST)
   - Learn tree traversal algorithms (inorder, preorder, postorder, level-order)

2. **Master Recursion**
   - Understand recursive thinking and base cases
   - Implement recursive algorithms for tree operations
   - Learn when to use recursion vs iteration
   - Practice stack frame visualization

3. **Apply Trees to Real Problems**
   - File system hierarchies (directories and files)
   - Expression evaluation (math expression trees)
   - Decision trees for simple logic
   - Hierarchical data organization

4. **Build Production Tools**
   - Directory tree visualizer (like `tree` command)
   - File search with filters
   - Duplicate file finder
   - Directory size analyzer

---

## 📚 Project Overview

### **Project 1: Binary Search Tree Implementation** (Foundation)
**Time Estimate:** 60-75 minutes

Build a complete Binary Search Tree from scratch with comprehensive operations.

**Features:**
- Node class with left/right pointers
- Insert operation (maintaining BST property)
- Search operation (find values efficiently)
- Delete operation (3 cases: leaf, one child, two children)
- Tree traversals: inorder, preorder, postorder, level-order
- Helper methods: min/max value, height, count nodes, is balanced
- Visualization: print tree structure

**Learning Focus:**
- Tree node structure and pointers
- Recursive algorithms
- BST properties (left < parent < right)
- Tree balancing concepts

**Test Cases:**
- Insert multiple values and verify BST property
- Search for existing and non-existing values
- Delete nodes (all 3 cases)
- Traverse tree and verify order
- Check tree properties (height, balance)

**Files:**
- `binary_search_tree.py` - BST implementation with tests
- `learn_recursion.py` - Interactive recursion exercises

---

### **Project 2: Directory Tree Explorer** (Real-World Application)
**Time Estimate:** 75-90 minutes

Build a powerful directory tree visualizer and analyzer using tree concepts.

**Features:**
- Visual tree representation of directories (like `tree` command)
- Customizable depth limit
- File/directory filtering (by extension, size, date)
- Statistics: total files, total size, file type distribution
- Color-coded output (directories vs files)
- Export tree structure to JSON/text
- Search functionality (find files by name/pattern)

**Learning Focus:**
- OS module and file system navigation
- Recursive directory traversal
- Tree visualization algorithms
- Real-world tree applications

**CLI Commands:**
```bash
python dir_explorer.py show /path --depth 3
python dir_explorer.py stats /path --human-readable
python dir_explorer.py search /path --pattern "*.py"
python dir_explorer.py export /path --format json
```

**Use Cases:**
- Project structure visualization
- Find large files consuming disk space
- Locate specific file types
- Generate documentation of project structure

**Files:**
- `dir_explorer.py` - Main CLI tool
- `tree_visualizer.py` - Tree drawing utilities
- `DIR_EXPLORER_USAGE.md` - Documentation

---

### **Project 3: Expression Evaluator** (Algorithm Challenge)
**Time Estimate:** 60-75 minutes

Build a math expression parser and evaluator using expression trees.

**Features:**
- Parse infix expressions (e.g., "3 + 4 * 2")
- Build expression tree
- Evaluate tree recursively
- Support operations: +, -, *, /, ^, ()
- Handle operator precedence correctly
- Convert between infix, prefix, postfix notation
- Visualize expression tree

**Learning Focus:**
- Expression trees and parsing
- Operator precedence and associativity
- Shunting yard algorithm (optional)
- Tree evaluation with recursion

**Example:**
```python
# Input: "3 + 4 * 2"
# Tree:      +
#          /   \
#         3     *
#              / \
#             4   2
# Result: 11

# Postfix: 3 4 2 * +
# Prefix:  + 3 * 4 2
```

**Test Cases:**
- Simple expressions: "5 + 3", "10 - 4"
- Precedence: "3 + 4 * 2" should be 11, not 14
- Parentheses: "(3 + 4) * 2" should be 14
- Complex: "2 ^ 3 + 4 * (5 - 1)"
- Edge cases: single numbers, negative numbers

**Files:**
- `expression_evaluator.py` - Main implementation
- `expression_tree.py` - Tree structure
- `test_expressions.py` - Test suite

---

### **Project 4: Duplicate File Finder** (Practical Tool)
**Time Estimate:** 45-60 minutes

Build a tool to find duplicate files using file hashing and tree structures.

**Features:**
- Scan directories recursively for files
- Calculate file hashes (MD5/SHA256)
- Group duplicate files by hash
- Show duplicate file groups
- Optional: Delete duplicates interactively
- Size reporting (space that can be freed)
- Ignore list (skip certain directories/files)

**Learning Focus:**
- File I/O and hashing
- Tree traversal for file scanning
- Dictionary/hash table for grouping
- Real-world utility programming

**CLI Commands:**
```bash
python duplicate_finder.py scan /path
python duplicate_finder.py scan /path --min-size 1MB
python duplicate_finder.py scan /path --ignore "node_modules,.git"
python duplicate_finder.py scan /path --delete  # Interactive mode
```

**Example Output:**
```
🔍 Scanning /home/user/projects...

Found 3 groups of duplicates:

Group 1 (2 files, 1.5 MB each):
  - /home/user/projects/backup/file1.txt
  - /home/user/projects/old/file1.txt

Group 2 (3 files, 500 KB each):
  - /home/user/downloads/image.png
  - /home/user/pictures/image.png
  - /home/user/desktop/image.png

Total duplicates: 5 files
Potential space savings: 3.5 MB
```

**Files:**
- `duplicate_finder.py` - Main implementation
- `file_hasher.py` - Hashing utilities
- `DUPLICATE_FINDER_USAGE.md` - Documentation

---

## 🗓️ Suggested Schedule

### **Morning Session (3-4 hours)**
1. **Warm-up:** Review tree concepts (30 min)
   - Read `learn_recursion.py` lessons
   - Draw trees on paper
   - Practice recursive thinking

2. **Project 1: Binary Search Tree** (2-2.5 hours)
   - Implement Node class
   - Add insert, search operations
   - Implement traversals
   - Add delete operation
   - Test thoroughly

3. **Break:** Review and document (30 min)

### **Afternoon Session (3-4 hours)**
1. **Project 2: Directory Tree Explorer** (2-2.5 hours)
   - Implement basic tree traversal
   - Add visualization
   - Build CLI interface
   - Add statistics and filtering

2. **Break:** Test with real directories (30 min)

3. **Choose One:**
   - **Option A:** Project 3 (Expression Evaluator) - For algorithm practice
   - **Option B:** Project 4 (Duplicate Finder) - For practical utility
   - Both are valuable; pick based on interest/energy

4. **Wrap-up:** Document and commit (30-45 min)

---

## 🎓 Learning Resources

### **Tree Concepts to Study:**

1. **Tree Terminology**
   - Root, parent, child, sibling, leaf
   - Depth (distance from root)
   - Height (longest path to leaf)
   - Balanced vs unbalanced trees

2. **Binary Tree Properties**
   - Max nodes at level L: 2^L
   - Max nodes in tree of height H: 2^(H+1) - 1
   - Min height for N nodes: log₂(N)

3. **BST Properties**
   - Left subtree < parent < right subtree
   - Inorder traversal gives sorted order
   - Search/Insert/Delete: O(log n) average, O(n) worst

4. **Traversal Orders**
   - **Inorder** (Left, Root, Right): Sorted for BST
   - **Preorder** (Root, Left, Right): Copy tree structure
   - **Postorder** (Left, Right, Root): Delete tree safely
   - **Level-order** (BFS): Level by level

### **Recursion Patterns:**

```python
# Base case + Recursive case
def recursive_function(data):
    # Base case: stop condition
    if stopping_condition:
        return base_value
    
    # Recursive case: break problem into smaller pieces
    result = combine(
        recursive_function(smaller_data_1),
        recursive_function(smaller_data_2)
    )
    return result
```

### **Tree Traversal Template:**

```python
def traverse(node):
    if node is None:  # Base case
        return
    
    # Preorder: Process node here
    traverse(node.left)   # Recurse left
    # Inorder: Process node here
    traverse(node.right)  # Recurse right
    # Postorder: Process node here
```

---

## 🔗 Connection to Cloud Engineering

### **AWS Services Using Trees:**

1. **S3 Bucket Structure**
   - Hierarchical folder/file organization
   - Prefix-based navigation (tree-like)
   - Our Directory Explorer mimics S3 navigation

2. **IAM Policies (JSON)**
   - Nested JSON structures form trees
   - Policy evaluation traverses tree
   - Expression trees help understand policy logic

3. **CloudFormation Templates**
   - Resource dependencies form directed graphs
   - Stack updates traverse dependency trees
   - Tree algorithms optimize deployment order

4. **Route 53 DNS**
   - DNS hierarchy is a tree structure
   - Domain name resolution traverses tree
   - Subdomain organization

5. **Lambda Function Hierarchies**
   - Parent-child invocation patterns
   - Event-driven tree structures
   - Our file finder could run as Lambda

### **DevOps Applications:**

- **File System Operations** → Deployment scripts, backup systems
- **Directory Analysis** → Build artifact management, cleanup scripts
- **Duplicate Detection** → Docker layer optimization, artifact deduplication
- **Tree Traversal** → Configuration management, dependency resolution

---

## 💡 Success Criteria

By end of Day 4, you should be able to:

- [ ] Explain tree terminology and properties
- [ ] Implement a working Binary Search Tree
- [ ] Write recursive functions confidently
- [ ] Visualize tree structures clearly
- [ ] Traverse directories recursively
- [ ] Build practical file system tools
- [ ] Understand when to use trees vs other data structures
- [ ] Apply tree concepts to real problems

---

## 🎯 Stretch Goals (If Time Permits)

1. **AVL Tree / Red-Black Tree**
   - Self-balancing BST
   - Rotation operations
   - Guaranteed O(log n) operations

2. **Trie (Prefix Tree)**
   - Autocomplete functionality
   - Dictionary implementation
   - String search optimization

3. **Heap Implementation**
   - Binary heap structure
   - Priority queue improvement
   - Heap sort algorithm

4. **File System Watcher**
   - Monitor directory changes
   - Trigger actions on file events
   - Real-time tree updates

5. **JSON/XML Tree Parser**
   - Parse structured data into trees
   - Query with path expressions
   - Transform tree structures

---

## 📦 Starter Code Structure

```
day4/
├── README.md                          # This file
├── ROADMAP.md                         # Detailed implementation steps
├── learn_recursion.py                 # Interactive recursion lessons
├── binary_search_tree.py              # Project 1: BST implementation
├── test_bst.py                        # BST test suite
├── dir_explorer.py                    # Project 2: Directory tool
├── tree_visualizer.py                 # Tree drawing utilities
├── DIR_EXPLORER_USAGE.md              # Documentation
├── expression_evaluator.py            # Project 3: Math expressions
├── expression_tree.py                 # Expression tree structure
├── test_expressions.py                # Expression test suite
├── duplicate_finder.py                # Project 4: Find duplicates
├── file_hasher.py                     # File hashing utilities
└── DUPLICATE_FINDER_USAGE.md          # Documentation
```

---

## 🚀 Getting Started

When you're ready to begin:

1. **Read this README fully** - Understand the big picture
2. **Review `learn_recursion.py`** - Interactive lessons
3. **Start with Project 1** - BST foundation
4. **Build incrementally** - Test as you go
5. **Take breaks** - Trees can be mentally intensive
6. **Ask questions** - I'm here to guide you!

---

## 🌟 Motivation

Trees are everywhere in computer science and cloud engineering. Today you're learning a fundamental structure that powers:

- File systems (every OS)
- Databases (B-trees, B+ trees)
- Compilers (syntax trees)
- AI/ML (decision trees, random forests)
- Graphics (scene graphs, BSP trees)
- Networking (routing tables, DNS)

**Master trees today, and you unlock dozens of advanced concepts!** 🌳

---

_"The best time to plant a tree was 20 years ago. The second best time is now."_ 

Let's grow your coding skills! 🌱 → 🌳

---

**Ready when you are! Sleep well, and let's conquer Day 4 together! 💪✨**
