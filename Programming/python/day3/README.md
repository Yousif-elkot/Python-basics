# 🔄 Day 3 — Stacks, Queues & Linux System Automation

**Date:** October 2, 2025  
**Focus:** Data Structures (Stacks/Queues) + System Scripting Bridge to Cloud Engineering

**Learning Mode:** 🎓 **Guided Hands-On** - You code everything, I coach you through it!

## 🎉 PROGRESS UPDATE

**Completed:** 4/4 Projects (100%) ✅
- ✅ **Challenge 1:** Balanced Brackets Checker - Stack algorithm mastered!
- ✅ **Project 2:** Command History Manager - Full professional implementation with JSON persistence!
- ✅ **Project 3:** Task Queue Simulator - Production CLI with FIFO & Priority Queue!
- ✅ **Project 4:** System Monitor - Complete with subprocess integration, deque-based time-series, alerts, and full CLI!

---

## 🎯 Today's Mission

Build practical tools that demonstrate **stack** and **queue** data structures while introducing **system automation** skills needed for Cloud Engineering. Since you're already proficient with Arch Linux and Git, let's leverage that expertise.

**📖 START HERE:** Read [GUIDED_LEARNING.md](./GUIDED_LEARNING.md) for step-by-step coaching!

---

## 📚 Core Concepts

### **Stack (LIFO - Last In, First Out)**

```
Stack Operations:
push()    - Add to top       → O(1)
pop()     - Remove from top  → O(1)
peek()    - View top         → O(1)
is_empty() - Check if empty  → O(1)
size()    - Get count        → O(1)
```

**Real-World Examples:**
- Command history (Ctrl+R in bash)
- Undo/Redo functionality
- Function call stack
- Browser back/forward buttons
- Expression evaluation

### **Queue (FIFO - First In, First Out)**

```
Queue Operations:
enqueue() - Add to rear      → O(1)
dequeue() - Remove from front → O(1)
front()   - View first item  → O(1)
is_empty() - Check if empty  → O(1)
size()    - Get count        → O(1)
```

**Real-World Examples:**
- Print job queue
- Task scheduling
- Message queues (AWS SQS preview!)
- Request handling in servers
- Breadth-first search

---

## 🛠️ Projects for Today

### **✅ Project 1: Command History Manager (Stack)** - COMPLETE!
**Difficulty:** ⭐⭐⭐  
**Time:** 3 hours (actual)  
**File:** `command_history.py`

**Implemented Features:**
- ✅ Command class with @dataclass for data management
- ✅ Stack-based history storage with max size limiting
- ✅ Undo/Redo functionality using two-stack pattern
- ✅ Case-insensitive substring search
- ✅ Statistics tracking (total, executed, most common command)
- ✅ JSON persistence (save/load complete state)
- ✅ Timestamp tracking with datetime
- ✅ Exit code tracking for success/failure
- ✅ Professional string formatting with status icons

**Skills Mastered:**
- Stack implementation (LIFO principle)
- @dataclass decorator for automatic boilerplate
- @classmethod for factory methods (from_dict)
- DateTime serialization (isoformat/fromisoformat)
- Two-stack pattern for undo/redo
- JSON serialization with complex objects
- Type hints with Optional, List
- Error handling with try/except

**Key Learning:**
- Understood difference between LIFO (Stack) and FIFO (Queue)
- Mastered two-stack pattern: one for history, one for undo operations
- Learned when @classmethod is better than __init__
- Implemented professional data structures from scratch

**Cloud Engineering Connection:**
- Understanding command history = better debugging
- Audit logging preparation (AWS CloudTrail concept)
- Automation script development
- State management for distributed systems

---

### **Project 2: System Task Queue Simulator (Queue)**
**Difficulty:** ⭐⭐⭐⭐  
**Time:** 3-4 hours  
**File:** `task_queue.py`

**Features:**
- Priority queue for system tasks
- Task scheduling with FIFO ordering
- CPU-bound vs I/O-bound task classification
- Task execution simulation with timing
- Concurrent task handling (basic threading intro)
- JSON-based task persistence
- Task status tracking (pending/running/completed/failed)

**Skills:**
- Queue implementation (deque-based)
- Priority queue using heapq
- Basic threading concepts
- Time complexity analysis
- State management

**Cloud Engineering Connection:**
- Job scheduling (AWS Batch, ECS tasks preview)
- Message queue systems (SQS/SNS foundation)
- Background task processing
- Microservices communication patterns

---

### **✅ Project 3: Task Queue Simulator (Queue & Priority Queue)** - COMPLETE!
**Difficulty:** ⭐⭐⭐⭐  
**Time:** 4 hours (actual)  
**Files:** `task_queue.py`, `test_task_queue.py`

**Implemented Features:**
- ✅ Task class with @dataclass (id, name, type, priority, status, timestamps)
- ✅ TaskType Enum for type safety (CPU, IO, NETWORK)
- ✅ TaskQueue class using `collections.deque` for O(1) FIFO operations
- ✅ PriorityTaskQueue class using `heapq` for O(log n) priority ordering
- ✅ TaskManager class coordinating queues + persistence
- ✅ Full CLI with argparse (add, list, next, complete, stats, clear)
- ✅ JSON persistence for tasks (survives restarts)
- ✅ Priority system: 1=highest (critical), 5=lowest
- ✅ FIFO tie-breaking for same-priority tasks
- ✅ Statistics tracking (counts, types, priorities, execution times)
- ✅ Comprehensive test suite

**CLI Commands:**
```bash
# Add tasks with priority
python task_queue.py add "Fix critical bug" --type CPU --priority 1
python task_queue.py add "Update docs" --type IO --priority 5

# List all pending tasks
python task_queue.py list

# Get next task (by priority or FIFO)
python task_queue.py next --start

# Mark task complete
python task_queue.py complete

# Show statistics
python task_queue.py stats

# Clear all tasks
python task_queue.py clear
```

**Skills Mastered:**
- Queue implementation (FIFO principle) with `collections.deque`
- Priority Queue with `heapq` min-heap
- Heap data structure (tree stored as array)
- Counter pattern for tie-breaking in heaps
- Tuple ordering in Python for heap comparisons
- TaskManager pattern for coordinating multiple data structures
- CLI development with argparse subcommands
- Complex JSON serialization/deserialization
- Enum for type-safe constants
- Timestamp tracking and datetime serialization

**Key Learning:**
- **deque vs list performance**: `popleft()` is O(1) vs O(n)
- **Min-heap property**: smallest element always at index 0
- **Heap index math**: left=2i+1, right=2i+2, parent=(i-1)//2
- **Why counter in heap**: prevents Task object comparison errors
- **Tuple comparison**: `(priority, counter, task)` compares left to right
- **FIFO tie-breaking**: same priority → compare counter → FIFO order

**Cloud Engineering Connection:**
- Task scheduling systems (AWS Batch, ECS)
- Message queue patterns (SQS/SNS)
- Job priority management
- Background task processing
- Microservices async communication

---

### **Project 4: Bash + Python Integration Script** 🐧
**Difficulty:** ⭐⭐⭐⭐⭐  
**Time:** 2-3 hours  
**File:** `system_monitor.py` + `system_monitor.sh`

**Features:**
- **Python side:**
  - Parse `top`, `df`, `free` command output
  - Store metrics in a queue (time-series data)
  - Analyze trends using sliding window
  - Generate alerts when thresholds exceeded
  - Export to JSON for dashboarding

- **Bash side:**
  - Wrapper script for easy invocation
  - Systemd service file template
  - Cron job examples
  - Log rotation setup

**Skills:**
- Subprocess management in Python
- Parsing system command output
- Bash script integration
- Queue for time-series data
- Statistical analysis basics

**Cloud Engineering Connection:**
- System monitoring (CloudWatch preview)
- Log aggregation
- Alert systems (SNS preparation)
- Infrastructure automation
- DevOps workflow introduction

---

## 🎓 Learning Objectives

### **Data Structures:**
- [x] Implement stack using Python lists
- [x] Implement stack as custom class with type hints
- [x] Implement queue using `collections.deque`
- [x] Implement priority queue using `heapq`
- [x] Understand when to use stack vs queue
- [x] Analyze time complexity of operations

### **Python Skills:**
- [x] Use `collections.deque` effectively
- [x] Work with `heapq` module
- [x] Implement `__repr__` and `__str__` methods
- [x] Use type hints for class methods
- [x] Work with `dataclasses` for task representation
- [x] Handle `subprocess` module for system commands
- [x] Use `threading` basics (optional)

### **System Integration:**
- [x] Read/write bash history format
- [x] Parse Linux command output
- [x] Understand systemd basics
- [x] Create cron job syntax
- [x] Integrate Python with shell scripts
- [x] Handle signals (SIGTERM, SIGINT)

### **Cloud Engineering Prep:**
- [x] Task scheduling concepts
- [x] Message queue patterns
- [x] Monitoring and alerting logic
- [x] Time-series data handling
- [x] Automation scripting

---

## 📊 Today's Challenges

### **✅ Challenge 1: Balanced Brackets Checker** - COMPLETE!
Use a **stack** to validate if brackets are balanced in code:
```python
check_brackets("({[]})")  # True
check_brackets("({[}])")  # False
check_brackets("((()))")  # True
```

**Solution Status:** ✅ Fully implemented in `balanced_brackets.py`
- All 11 test cases passing
- Time Complexity: O(n)
- Space Complexity: O(n)
- Algorithm: Stack-based with dictionary mapping for bracket pairs

### **Challenge 2: Task Scheduler**
Implement a simple round-robin scheduler using **queue**:
- Multiple tasks with different priorities
- Time slicing simulation
- Track task completion order

### **Challenge 3: System Alert Aggregator**
Build a tool that:
- Monitors system metrics every 10 seconds
- Stores last 100 readings in a queue
- Alerts if CPU > 80% for 3 consecutive readings
- Uses stack to track alert history

---

## 🔧 Implementation Guide

### **Stack Implementation Template:**

```python
from typing import Generic, TypeVar, Optional
from dataclasses import dataclass
from datetime import datetime

T = TypeVar('T')

class Stack(Generic[T]):
    """Generic stack implementation with Python list."""
    
    def __init__(self, max_size: Optional[int] = None):
        self._items: list[T] = []
        self._max_size = max_size
    
    def push(self, item: T) -> bool:
        """Add item to top of stack."""
        if self._max_size and len(self._items) >= self._max_size:
            return False
        self._items.append(item)
        return True
    
    def pop(self) -> Optional[T]:
        """Remove and return top item."""
        return self._items.pop() if self._items else None
    
    def peek(self) -> Optional[T]:
        """View top item without removing."""
        return self._items[-1] if self._items else None
    
    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Return number of items in stack."""
        return len(self._items)
    
    def __repr__(self) -> str:
        return f"Stack({self._items})"
```

### **Queue Implementation Template:**

```python
from collections import deque
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class Queue(Generic[T]):
    """Generic queue implementation using deque."""
    
    def __init__(self):
        self._items: deque[T] = deque()
    
    def enqueue(self, item: T) -> None:
        """Add item to rear of queue."""
        self._items.append(item)
    
    def dequeue(self) -> Optional[T]:
        """Remove and return front item."""
        return self._items.popleft() if self._items else None
    
    def front(self) -> Optional[T]:
        """View front item without removing."""
        return self._items[0] if self._items else None
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Return number of items in queue."""
        return len(self._items)
    
    def __repr__(self) -> str:
        return f"Queue({list(self._items)})"
```

---

## 🚀 Bonus: Bridge to Cloud Engineering

### **Conceptual Connections:**

1. **Stack → AWS CloudFormation:**
   - Stack-based infrastructure deployment
   - LIFO deletion during rollback
   - Nested stacks concept

2. **Queue → AWS SQS:**
   - Message queuing service
   - FIFO vs Standard queues
   - Dead letter queues for failed messages

3. **Task Scheduling → AWS EventBridge/Lambda:**
   - Event-driven architecture
   - Asynchronous processing
   - Serverless task execution

4. **System Monitoring → AWS CloudWatch:**
   - Metrics collection
   - Alert thresholds
   - Dashboard visualization

---

## ✅ Success Criteria

By end of Day 3, you should have:

- [✅] Working stack implementation (list-based class)
- [✅] Command history manager (Project 1) complete
- [✅] Balanced brackets checker solved
- [✅] All code documented with docstrings
- [✅] Comprehensive test suite with 18+ tests passing
- [✅] Git commits with clear messages
- [✅] Updated README.md with Day 3 progress
- [ ] Working queue implementation using deque
- [ ] Priority queue implementation using heapq
- [ ] Task queue simulator (Project 2) complete
- [x] System monitor with Bash integration (Project 4) complete
- [ ] Unit tests for queue operations

**Current Progress: 58% Complete** (7/12 criteria met)

---

## 📖 Resources

### **Python Documentation:**
- [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)
- [heapq - Priority Queue](https://docs.python.org/3/library/heapq.html)
- [subprocess - System Commands](https://docs.python.org/3/library/subprocess.html)
- [typing - Type Hints](https://docs.python.org/3/library/typing.html)

### **System Integration:**
- Bash scripting basics (you already know this! 🐧)
- Systemd service files
- Cron syntax
- Linux /proc filesystem

### **Algorithm Resources:**
- Stack and Queue visualizations
- Time complexity analysis
- Real-world queue applications

---

## 🎯 Next Steps (Day 4 Preview)

**Day 4: Web Scraping + API Development**
- Build REST API with Flask
- Scrape system metrics
- Create dashboard with real-time updates
- Introduction to HTTP protocols (networking prep)

Or alternatively:

**Day 4: Object-Oriented Design + File System Manager**
- Classes and inheritance
- Linked list implementation
- File system tree traversal
- Preparation for cloud storage concepts (S3)

---

## 💡 Pro Tips

1. **Test on Your Arch System:**
   - You have native access to all Linux tools
   - Test systemd service without sudo (user services)
   - Use `systemctl --user` for testing

2. **Git Workflow:**
   - Branch for each project: `git checkout -b day3-project1`
   - Commit after each feature
   - Merge to main when complete

3. **Performance Testing:**
   - Use `time` command to benchmark
   - Profile with `cProfile` for bottlenecks
   - Compare list vs deque performance

4. **Documentation:**
   - Write usage examples as you code
   - Document edge cases you discover
   - Keep notes on stack vs queue decisions

5. **Cloud Mindset:**
   - Think about scalability (what if 1M commands?)
   - Consider fault tolerance (what if process crashes?)
   - Plan for monitoring (how to debug in production?)

---

## 📝 Deliverables

**Completed Files:**

```
day3/
├── ✅ README.md                      (this file - updated!)
├── ✅ command_history.py             (Stack project - COMPLETE with CLI!)
├── ✅ COMMAND_HISTORY_USAGE.md       (Usage guide & examples)
├── ✅ balanced_brackets.py           (Challenge solution - COMPLETE!)
├── ✅ GUIDED_LEARNING.md             (Step-by-step coaching)
├── ✅ PROJECT2_GUIDE.md              (Detailed project roadmap)
├── ✅ LEARNING_NOTES.md              (Your observations)
├── ✅ DATA_STRUCTURES_CHEATSHEET.md  (Quick reference)
├── ✅ QUICK_START.md                 (Getting started guide)
└── ⏳ task_queue.py                  (Queue project - pending)
```

**Pending Files:**
- `system_monitor.py` (Integration project)
- `system_monitor.sh` (Bash wrapper)

---

**Ready to build? Let's make Day 3 count! 🚀**

_"The stack traces you debug today are the skills you'll use in cloud tomorrow."_ 🔧
