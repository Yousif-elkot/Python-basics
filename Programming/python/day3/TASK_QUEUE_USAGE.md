# Task Queue Manager - Usage Guide

A production-ready CLI tool for managing tasks using Queue (FIFO) and Priority Queue data structures.

## 🚀 Quick Start

```bash
# Add a high-priority task
python task_queue.py add "Fix critical bug" --type CPU --priority 1

# List all tasks
python task_queue.py list

# Get next task to work on
python task_queue.py next --start

# Mark task as complete
python task_queue.py complete

# Show statistics
python task_queue.py stats
```

## 📋 Commands

### 1. Add Task

Add a new task to the queue.

```bash
python task_queue.py add "<task_description>" [options]
```

**Options:**
- `--type {CPU,IO,NETWORK}` - Task type (default: CPU)
- `--priority {1-5}` - Priority level, 1=highest, 5=lowest (default: 3)
- `--mode {fifo,priority}` - Queue mode (default: priority)

**Examples:**
```bash
# Critical bug fix (highest priority)
python task_queue.py add "Fix login authentication" --type CPU --priority 1

# Medium priority code review
python task_queue.py add "Review PR #456" --type CPU --priority 3

# Low priority documentation update
python task_queue.py add "Update API docs" --type IO --priority 5

# Network task
python task_queue.py add "Deploy to staging" --type NETWORK --priority 2
```

### 2. List Tasks

Display all pending tasks in the queue.

```bash
python task_queue.py list [--mode {fifo,priority}]
```

**Example Output:**
```
📋 Pending Tasks (4) - Mode: PRIORITY
============================================================
  [1] Fix login authentication (CPU, Priority: High) - PENDING ⏳
  [3] Deploy to staging (NETWORK, Priority: High) - PENDING ⏳
  [2] Review PR #456 (CPU, Priority: Medium) - PENDING ⏳
  [4] Update API docs (IO, Priority: Low) - PENDING ⏳
```

**Note:** In priority mode, tasks are automatically sorted by priority (lowest number = highest urgency).

### 3. Get Next Task

Retrieve the next task to work on.

```bash
# Get and remove next task
python task_queue.py next

# Peek at next task without removing it
python task_queue.py next --peek

# Get next task and mark as started
python task_queue.py next --start
```

**Examples:**
```bash
# Start working on next task
python task_queue.py next --start
🎯 Got next task:
  [1] Fix login authentication (CPU, Priority: High) - PENDING ⏳
  ▶️  Started at 14:30:25

# Just see what's next without removing it
python task_queue.py next --peek
🎯 Next task (not removed):
  [1] Fix login authentication (CPU, Priority: High) - PENDING ⏳
```

### 4. Complete Task

Mark the next task as completed.

```bash
python task_queue.py complete [--mode {fifo,priority}]
```

**Example:**
```bash
python task_queue.py complete
✅ Task completed: [1] Fix login authentication (CPU, Priority: High) - COMPLETED ✅
```

### 5. Show Statistics

Display queue statistics and metrics.

```bash
python task_queue.py stats [--mode {fifo,priority}]
```

**Example Output:**
```
📊 Task Queue Statistics - Mode: PRIORITY
============================================================
  Total tasks: 8
  Pending: 5
  Completed: 3

  Task Types:
    CPU: 3
    NETWORK: 1
    IO: 1

  Priority Stats:
    Average: 2.80
    Range: 1-5

  Avg Execution Time: 45.23s
```

### 6. Clear Queue

Remove all pending tasks from the queue.

```bash
python task_queue.py clear [--mode {fifo,priority}]
```

**Example:**
```bash
python task_queue.py clear
🗑️  Cleared 5 pending tasks!
```

## 🔄 Queue Modes

### Priority Mode (Default)

Tasks are processed by priority level:
- **Priority 1-2**: High (Critical/Urgent)
- **Priority 3**: Medium (Normal)
- **Priority 4-5**: Low (Can wait)

Lower number = higher priority. Tasks with same priority are processed FIFO.

```bash
python task_queue.py add "Critical fix" --priority 1  # Processed first
python task_queue.py add "Normal task" --priority 3   # Processed second
python task_queue.py add "Low priority" --priority 5  # Processed last
```

### FIFO Mode

Tasks are processed in the order they were added (First In, First Out).

```bash
python task_queue.py add "Task A" --mode fifo  # Processed first
python task_queue.py add "Task B" --mode fifo  # Processed second
python task_queue.py add "Task C" --mode fifo  # Processed third
```

## 💾 Persistence

Tasks are automatically saved to `tasks.json` and persist between sessions.

**File location:** `tasks.json` in the current directory

**What's saved:**
- All pending tasks in the queue
- Completed tasks with execution times
- Queue mode and settings
- Task metadata (created, started, completed timestamps)

## 🎯 Task Types

### CPU Tasks
Computational work, calculations, data processing.
```bash
python task_queue.py add "Process user analytics" --type CPU
```

### IO Tasks
File operations, database queries, reading/writing data.
```bash
python task_queue.py add "Import CSV data" --type IO
```

### NETWORK Tasks
API calls, deployments, external service interactions.
```bash
python task_queue.py add "Deploy to production" --type NETWORK
```

## 📊 Task Status

- **PENDING ⏳** - Task is in queue, not started
- **RUNNING 🏃** - Task is currently being worked on
- **COMPLETED ✅** - Task is finished
- **FAILED ❌** - Task encountered an error

## 🔧 Advanced Usage

### Workflow Example: Sprint Planning

```bash
# Add all sprint tasks
python task_queue.py add "Fix security vulnerability" --type CPU --priority 1
python task_queue.py add "Implement OAuth login" --type CPU --priority 2
python task_queue.py add "Add unit tests" --type CPU --priority 3
python task_queue.py add "Update changelog" --type IO --priority 4
python task_queue.py add "Deploy to staging" --type NETWORK --priority 2

# Check what's pending
python task_queue.py list

# Start working (highest priority first)
python task_queue.py next --start

# Complete and move to next
python task_queue.py complete
python task_queue.py next --start

# Check progress
python task_queue.py stats
```

### Workflow Example: Bug Triage

```bash
# Critical bugs get priority 1
python task_queue.py add "Database connection failing" --type CPU --priority 1
python task_queue.py add "Payment processing broken" --type NETWORK --priority 1

# Important bugs get priority 2
python task_queue.py add "Search returns wrong results" --type CPU --priority 2

# Minor bugs get priority 4-5
python task_queue.py add "Button alignment issue" --type CPU --priority 4

# See what to work on first
python task_queue.py list
```

### Daily Standup Report

```bash
# What's pending?
python task_queue.py list

# What's our workload?
python task_queue.py stats
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
python test_task_queue.py
```

This tests:
- Task creation and attributes
- FIFO queue operations
- Priority queue operations
- Tie-breaking with same priorities
- All data structure correctness

## 🎓 What You're Learning

This tool demonstrates:
- **Queue (FIFO)**: First In, First Out - `collections.deque`
- **Priority Queue**: Min-heap with `heapq` module
- **CLI Development**: `argparse` for professional interfaces
- **Data Persistence**: JSON serialization
- **Dataclasses**: Modern Python class definitions
- **Enums**: Type-safe constants
- **Type Hints**: Professional code documentation

## 🚀 Performance

- **Queue Operations**: O(1) for enqueue/dequeue with `deque`
- **Priority Queue**: O(log n) for enqueue/dequeue with `heapq`
- **Peek**: O(1) for both queue types
- **List**: O(n) to display all tasks

## 💡 Tips

1. **Use priority mode** for task management where urgency matters
2. **Use FIFO mode** for simple job queues where order matters
3. **Check stats regularly** to understand your workload
4. **Use --peek** to plan without removing tasks
5. **Mark tasks as started** with `--start` for time tracking

## 🐛 Troubleshooting

**Tasks not persisting?**
- Check that you have write permissions in the current directory
- Look for `tasks.json` file

**Wrong queue mode?**
- Always specify `--mode` flag to ensure correct queue
- Check your `tasks.json` for current mode

**Can't find a task?**
- Use `python task_queue.py list` to see all pending tasks
- Completed tasks are stored but not shown in list

## 📖 Related Projects

- **Balanced Brackets** - Stack (LIFO) data structure
- **Command History** - Two-stack undo/redo pattern
- **Task Queue** - Queue (FIFO) and Priority Queue (Heap)

---

**Project:** Day 3 - Data Structures & Algorithms  
**Author:** Python Learning Journey  
**Date:** October 2, 2025
