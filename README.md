# 🚀 30-Day Python & Cloud Engineering Journey

Welcome to my **30-day coding adventure**! This repository tracks my daily progress as I build Python fundamentals and work toward Cloud Engineering skills.

Each day includes hands-on projects, code improvements, and detailed documentation. The goal is to develop professional coding habits while building a portfolio of practical applications.

---

## 📈 Learning Philosophy

**🎯 Build → Improve → Document → Repeat**

- Start with simple, working solutions
- Iteratively add features and improve code quality
- Practice Git workflows and professional documentation
- Focus on real-world applications and best practices

---

## �️ Journey Timeline

### ✅ **Day 1** — _Foundations & CLI Applications_

📁 **[View Details →](day1/README.md)**

**🔧 Unit Converter**

- Basic Python syntax, functions, and control flow
- Input validation and error handling
- Professional code organization with type hints

**📞 Phone Book CLI**

- Dictionary data structures and JSON persistence
- Menu-driven interface design
- CRUD operations and user experience

**� Password Generator**

- Cryptographically secure random generation
- Advanced CLI interfaces with argparse
- Security-focused programming practices
- Character set manipulation and validation

**�💡 Key Skills:** Python fundamentals, file I/O, function design, CLI development, security programming, professional documentation

---

### ✅ **Day 2** — _Arrays, Lists & Search Algorithms_

📁 **[View Details →](day2/Smart_Todo_List/README.md)**

**📝 Smart Todo List**

- Dynamic arrays and list operations (insertion, deletion, traversal)
- Linear search algorithms with multiple criteria
- Sorting algorithms with custom key functions
- Advanced CLI interface with comprehensive error handling
- Data persistence with JSON serialization

**💡 Key Skills:** Arrays & lists, search algorithms, sorting algorithms, data structures, algorithm complexity analysis

---

### ✅ **Day 3** — _Stacks, Queues & System Integration_

📁 **[View Details →](day3/README.md)**

**🧮 Balanced Brackets Checker**

- Stack (LIFO) data structure for bracket matching
- Algorithm problem-solving with edge cases
- Character-by-character validation logic
- Comprehensive test suite with 11 test cases

**🔄 Command History Manager**

- Stack implementation with undo/redo functionality
- Command tracking with timestamps and exit codes
- Search through history with pattern matching
- JSON persistence and statistics tracking
- Professional CLI with argparse

**📋 Task Queue Simulator**

- Queue (FIFO) and Priority Queue implementations
- Task scheduling with priority levels using heapq
- Dual-mode operation (FIFO vs Priority)
- Status tracking (pending/completed) with execution simulation
- JSON persistence and comprehensive CLI

**🖥️ System Monitor**

- Python + Bash integration using subprocess module
- Parse Linux system commands (free, df, uptime)
- Deque-based time-series metric storage
- Alert threshold detection and warnings
- Full CLI with 4 commands: snapshot, monitor, history, export
- JSON export for external tool integration

**💡 Key Skills:** Stack (LIFO), Queue (FIFO), Priority Queue (heapq), Deque, Collections module, Subprocess integration, Bash command parsing, Time-series data, Alert systems, Argparse CLI design, JSON serialization, Dataclasses

**☁️ Cloud Engineering Bridge:** AWS SQS message queues, CloudWatch monitoring & alarms, Event-driven architecture, Task scheduling patterns, Infrastructure automation, EC2 monitoring

---

### ✅ **Day 4** — _Trees, Recursion & File Systems_

📁 **[View Details →](day4/README.md)**

**🌳 Binary Search Tree**

- TreeNode and BST class implementation
- Insert and search operations (O(log n) average case)
- All 4 traversals: inorder, preorder, postorder, level-order (BFS)
- Delete operation with 3 cases (leaf, one child, two children)
- Helper methods: count_nodes, height, find_min, find_max, is_balanced
- ASCII tree visualization with box-drawing characters
- Comprehensive testing suite

**📁 Directory Tree Explorer CLI**

- Recursive directory scanning and tree building
- DirectoryNode tree structure (N-ary tree)
- ASCII visualization with proper connectors (├──, └──, │)
- Size calculation with human-readable formatting (bytes/KB/MB/GB)
- Full CLI with argparse: show and stats commands
- Depth limiting and ignore patterns (.git, node_modules, etc.)
- Error handling for permission issues
- Production-ready command-line tool

**💡 Key Skills:** Recursion patterns (base case + recursive case), Binary Search Trees (BST), Tree traversal algorithms (DFS & BFS), N-ary trees, File system operations (os module), Recursive aggregation, ASCII art generation, CLI design with subparsers, Path manipulation, Error handling

**☁️ Cloud Engineering Bridge:** S3 bucket structure exploration, File system monitoring, Directory size analysis, AWS CLI tree commands, Infrastructure inventory tools, Recursive operations on cloud resources

---

### ✅ **Day 5** — _Hash Tables, Dictionaries & Text Analysis_

� **[View Details →](day5/README.md)**

**🗂️ Custom Hash Table Implementation**

- Hash function design using ASCII sum modulo table size
- Collision handling with chaining (linked lists in buckets)
- Dynamic resizing with load factor monitoring (> 0.7 triggers resize)
- Complete CRUD operations: insert, search, delete
- Automatic table doubling and rehashing of all items
- Statistics tracking (count, collisions, load factor)
- O(1) average-case lookup performance

**📊 Word Frequency Analyzer CLI**

- Text file reading with encoding support and error handling
- Text tokenization using regular expressions (regex)
- Stop word filtering (50+ common words: the, is, and, etc.)
- Frequency counting with Python's Counter
- Top N word analysis with bar chart visualization
- Dual export: JSON and CSV formats
- Full CLI with argparse: --top, --no-filter, --export, --output flags
- Production-ready text analysis tool

**💡 Key Skills:** Hash tables (O(1) lookup), Hash functions, Collision handling (chaining), Load factor & resizing, Python dictionaries internals, collections.Counter, collections.defaultdict, Regular expressions (re module), Text parsing & tokenization, CSV module, JSON serialization, CLI argument parsing, Data visualization (bar charts)

**☁️ Cloud Engineering Bridge:** Configuration management (key-value stores like AWS Parameter Store), Caching strategies (ElastiCache, CloudFront), Log analysis and metrics aggregation, CloudWatch Logs Insights queries, Data processing pipelines, ETL operations

---

### �🚀 **Days 6-30** — _The Adventure Continues..._

_Each day will introduce new concepts building toward Cloud Engineering applications_

---

## 🎯 30-Day Goals

### **Python Mastery**

- [✅] Core syntax and data structures
- [✅] Arrays, lists, and linear data structures
- [✅] Hash tables and dictionaries
- [✅] Regular expressions and text processing
- [ ] Object-oriented programming
- [ ] Error handling and testing
- [ ] API development and consumption

### **Development Skills**

- [ ✅ ] Git/GitHub professional workflows
- [ ✅ ] Code documentation and comments
- [ ✅ ] Project structure and organization
- [ ✅ ] Debugging and problem-solving
- [ ] Performance optimization

### **Cloud Engineering Prep**

- [ ] Automation scripting
- [ ] Configuration management
- [ ] Database interactions
- [ ] Web services and APIs
- [ ] DevOps tool integration

---

## 📊 Progress Stats

| Metric                | Count  |
| --------------------- | ------ |
| **Days Completed**    | 5 / 30 |
| **Projects Built**    | 15     |
| **Functions Written** | 180+   |
| **Git Commits**       | 45+    |
| **Lines of Code**     | 4200+  |

---

## 🛠️ Tech Stack

**Languages:** Python 3, Bash  
**Tools:** Git, GitHub, VS Code, Linux CLI  
**Libraries:** json, sys, typing, argparse, string, random, datetime, os, collections, heapq, subprocess, dataclasses, re, csv  
**Concepts:** CLI development, data persistence, error handling, security programming, documentation, arrays & lists, search algorithms, sorting algorithms, stacks (LIFO), queues (FIFO), priority queues, deques, system integration, subprocess management, time-series data, alert systems, bash parsing, recursion, binary search trees (BST), tree traversals (DFS/BFS), N-ary trees, file system operations, recursive algorithms, hash tables, collision handling, load factor, O(1) lookup, regular expressions, text parsing, data export (JSON/CSV)

---

## 🔗 Quick Navigation

- **[Day 1 Projects](day1/)** — Unit Converter, Phone Book CLI & Password Generator
- **[Day 2 Projects](day2/)** — Smart Todo List with Arrays & Search Algorithms
- **[Day 3 Projects](day3/)** — Balanced Brackets, Command History, Task Queue & System Monitor
- **[Day 4 Projects](day4/)** — Binary Search Tree & Directory Tree Explorer
- **[Day 5 Projects](day5/)** — Custom Hash Table & Word Frequency Analyzer
- **[Latest Code](day5/word_frequency.py)** — Most recent project
- **[Progress Tracker](PROGRESS_TRACKER.md)** — Detailed daily progress and stats

---

_"Every expert was once a beginner. Every pro was once an amateur. Every icon was once an unknown."_ 🌟
