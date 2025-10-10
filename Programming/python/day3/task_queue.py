from enum import Enum
import heapq
from collections import deque
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

class TaskType(Enum):
    CPU = "CPU"
    IO = "IO"
    NETWORK = "NETWORK"

@dataclass
class Task:
    id: str 
    name: str
    task_type: TaskType
    priority: int
    status: str = "PENDING"  # PENDING, RUNNING, COMPLETED, FAILED
    created_at: datetime = None              # When task was created
    started_at: Optional[datetime] = None    # When it started running (None until it runs)
    completed_at: Optional[datetime] = None  # When it finished (None until done)
    execution_time: Optional[float] = None   # How long it took in seconds

    def __post_init__(self):
        """Set created_at automatically when task is created."""
        if self.created_at is None:
            self.created_at = datetime.now()

    def __str__(self):
        if self.priority <= 2:
            priority_str = "High"
        elif self.priority <= 4:
            priority_str = "Medium"
        else:
            priority_str = "Low"

        status_icons = {
        "PENDING": "⏳",
        "RUNNING": "🏃",
        "COMPLETED": "✅",
        "FAILED": "❌"
      }
        status_display = f"{self.status} {status_icons.get(self.status, '')}"

        result = f"[{self.id}] {self.name} ({self.task_type.value}, Priority: {priority_str}) - {status_display}  "

        if self.execution_time is not None:
            result += f" - Execution Time: ({self.execution_time:.2f}s)"

        return result
    

class TaskQueue:
    """FIFO Queue using deque - First In, First Out"""
    def __init__(self):
        # Use deque for O(1) operations
        self.queue = deque()

    def is_empty(self) -> bool:
        # Check if queue is empty
        return not self.queue
        
    def enqueue(self, task: Task):
        # Add task to the back of queue
        self.queue.append(task)
        
    def dequeue(self) -> Optional[Task]:
        # Remove and return task from front
        # Return None if empty
        if self.is_empty():
            return None
        return self.queue.popleft()
        
    def peek(self) -> Optional[Task]:
        # Look at front task without removing
        if self.is_empty():
            return None
        return self.queue[0]

    def size(self) -> int:
        # Return number of tasks
        return len(self.queue)
    
    #str method for debugging
    def __str__(self) -> str:
        """String representation for debugging."""
        if self.is_empty():
            return "TaskQueue(empty)"
        task_names = [t.name for t in self.queue]
        return f"TaskQueue(size={self.size()}, tasks={task_names})"

class PriorityTaskQueue:
    """Priority Queue using heapq - Lower priority number = Higher urgency"""
    def __init__(self):
        """Initialize empty priority queue."""
        self._heap = []        # The heap (min-heap by default)
        self._counter = 0      # For tie-breaking (FIFO for same priority)

    def is_empty(self) -> bool:
        """Check if priority queue is empty."""
        # TODO: Return True if _heap is empty
        return not self._heap

    def size(self) -> int:
        """Return number of tasks in queue."""
        # TODO: Return length of _heap
        return len(self._heap)

    def enqueue(self, task: Task) -> None:
        """Add task to priority queue. Lower priority = higher urgency."""
        # heapq uses tuples: (priority, counter, task)
        # - priority: Task's priority (1=urgent, 5=low)
        # - counter: Prevents comparison of Task objects (FIFO tie-breaker)
        # - task: The actual Task object

        # TODO: 
        # 1. Increment self._counter
        # 2. Create entry: (task.priority, self._counter, task)
        # 3. heapq.heappush(self._heap, entry)

        self._counter += 1
        entry = (task.priority, self._counter, task)
        heapq.heappush(self._heap, entry)

    def dequeue(self) -> Optional[Task]:
        """Remove and return highest priority task (lowest number)."""
        # TODO:
        # 1. Check if empty (return None)
        # 2. heapq.heappop(self._heap) returns (priority, counter, task)
        # 3. Extract and return just the task
        if self.is_empty():
            return None

        priority, counter, task = heapq.heappop(self._heap)
        return task

    def peek(self) -> Optional[Task]:
        """Look at highest priority task without removing."""
        # TODO:
        # 1. Check if empty (return None)
        # 2. self._heap[0] is (priority, counter, task)
        # 3. Extract and return just the task
        if self.is_empty():
            return None
        priority, counter, task = self._heap[0]
        return task

    def __str__(self) -> str:
        """String representation for debugging."""
        # TODO: Similar to TaskQueue but show priorities
        if self.is_empty():
            return "PriorityTaskQueue(empty)"
        # Extract task names and priorities
        tasks_info = [(priority, task.name) for priority, counter, task in self._heap]
        return f"PriorityTaskQueue(size={self.size()}, tasks={tasks_info})"

# ============================================================================
# CLI Interface
# ============================================================================

import argparse
import json
import os
from pathlib import Path


class TaskManager:
    """Manages tasks with both FIFO and Priority queues, includes persistence."""
    
    def __init__(self, filepath: str = "tasks.json", mode: str = "priority"):
        """
        Initialize Task Manager.
        
        Args:
            filepath: Path to JSON file for persistence
            mode: 'fifo' for FIFO queue, 'priority' for priority queue
        """
        self.filepath = filepath
        self.mode = mode
        self._task_counter = 0
        
        if mode == "fifo":
            self.queue = TaskQueue()
        else:
            self.queue = PriorityTaskQueue()
        
        self.completed_tasks = []
        self.load()
    
    def add_task(self, name: str, task_type: str, priority: int) -> Task:
        """Add a new task to the queue."""
        self._task_counter += 1
        task_type_enum = TaskType[task_type.upper()]
        task = Task(
            id=str(self._task_counter),
            name=name,
            task_type=task_type_enum,
            priority=priority
        )
        self.queue.enqueue(task)
        self.save()
        return task
    
    def get_next_task(self) -> Optional[Task]:
        """Get (and remove) the next task from the queue."""
        task = self.queue.dequeue()
        if task:
            self.save()
        return task
    
    def peek_next_task(self) -> Optional[Task]:
        """Look at the next task without removing it."""
        return self.queue.peek()
    
    def complete_task(self, task: Task) -> None:
        """Mark a task as completed and add execution time."""
        task.status = "COMPLETED"
        task.completed_at = datetime.now()
        if task.started_at:
            task.execution_time = (task.completed_at - task.started_at).total_seconds()
        self.completed_tasks.append(task)
        self.save()
    
    def get_all_tasks(self) -> list:
        """Get all pending tasks (doesn't remove them)."""
        if isinstance(self.queue, PriorityTaskQueue):
            # Extract tasks from heap
            return [task for _, _, task in self.queue._heap]
        else:
            # Extract tasks from deque
            return list(self.queue.queue)
    
    def clear_all(self) -> int:
        """Clear all pending tasks."""
        count = self.queue.size()
        if isinstance(self.queue, PriorityTaskQueue):
            self.queue._heap.clear()
        else:
            self.queue.queue.clear()
        self.save()
        return count
    
    def get_statistics(self) -> dict:
        """Get queue statistics."""
        pending_tasks = self.get_all_tasks()
        
        stats = {
            "mode": self.mode,
            "pending_count": len(pending_tasks),
            "completed_count": len(self.completed_tasks),
            "total_count": len(pending_tasks) + len(self.completed_tasks)
        }
        
        if pending_tasks:
            # Task type distribution
            type_counts = {}
            for task in pending_tasks:
                t = task.task_type.value
                type_counts[t] = type_counts.get(t, 0) + 1
            stats["task_types"] = type_counts
            
            # Priority distribution
            priorities = [t.priority for t in pending_tasks]
            stats["avg_priority"] = sum(priorities) / len(priorities)
            stats["min_priority"] = min(priorities)
            stats["max_priority"] = max(priorities)
        
        if self.completed_tasks:
            exec_times = [t.execution_time for t in self.completed_tasks if t.execution_time]
            if exec_times:
                stats["avg_execution_time"] = sum(exec_times) / len(exec_times)
        
        return stats
    
    def save(self) -> None:
        """Save tasks to JSON file."""
        data = {
            "mode": self.mode,
            "task_counter": self._task_counter,
            "pending_tasks": [],
            "completed_tasks": []
        }
        
        # Save pending tasks
        for task in self.get_all_tasks():
            data["pending_tasks"].append({
                "id": task.id,
                "name": task.name,
                "task_type": task.task_type.value,
                "priority": task.priority,
                "status": task.status,
                "created_at": task.created_at.isoformat() if task.created_at else None,
                "started_at": task.started_at.isoformat() if task.started_at else None,
                "completed_at": task.completed_at.isoformat() if task.completed_at else None,
                "execution_time": task.execution_time
            })
        
        # Save completed tasks
        for task in self.completed_tasks:
            data["completed_tasks"].append({
                "id": task.id,
                "name": task.name,
                "task_type": task.task_type.value,
                "priority": task.priority,
                "status": task.status,
                "created_at": task.created_at.isoformat() if task.created_at else None,
                "started_at": task.started_at.isoformat() if task.started_at else None,
                "completed_at": task.completed_at.isoformat() if task.completed_at else None,
                "execution_time": task.execution_time
            })
        
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load(self) -> None:
        """Load tasks from JSON file."""
        if not os.path.exists(self.filepath):
            return
        
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
            
            self.mode = data.get("mode", self.mode)
            self._task_counter = data.get("task_counter", 0)
            
            # Load pending tasks
            for task_data in data.get("pending_tasks", []):
                task = Task(
                    id=task_data["id"],
                    name=task_data["name"],
                    task_type=TaskType[task_data["task_type"]],
                    priority=task_data["priority"],
                    status=task_data["status"],
                    created_at=datetime.fromisoformat(task_data["created_at"]) if task_data.get("created_at") else None,
                    started_at=datetime.fromisoformat(task_data["started_at"]) if task_data.get("started_at") else None,
                    completed_at=datetime.fromisoformat(task_data["completed_at"]) if task_data.get("completed_at") else None,
                    execution_time=task_data.get("execution_time")
                )
                self.queue.enqueue(task)
            
            # Load completed tasks
            for task_data in data.get("completed_tasks", []):
                task = Task(
                    id=task_data["id"],
                    name=task_data["name"],
                    task_type=TaskType[task_data["task_type"]],
                    priority=task_data["priority"],
                    status=task_data["status"],
                    created_at=datetime.fromisoformat(task_data["created_at"]) if task_data.get("created_at") else None,
                    started_at=datetime.fromisoformat(task_data["started_at"]) if task_data.get("started_at") else None,
                    completed_at=datetime.fromisoformat(task_data["completed_at"]) if task_data.get("completed_at") else None,
                    execution_time=task_data.get("execution_time")
                )
                self.completed_tasks.append(task)
        
        except (json.JSONDecodeError, KeyError) as e:
            print(f"⚠️  Warning: Could not load tasks: {e}")


def cmd_add(args):
    """Add a new task."""
    manager = TaskManager(mode=args.mode)
    task = manager.add_task(args.name, args.type, args.priority)
    print(f"✅ Task added: {task}")


def cmd_list(args):
    """List all pending tasks."""
    manager = TaskManager(mode=args.mode)
    tasks = manager.get_all_tasks()
    
    if not tasks:
        print("📭 No pending tasks!")
        return
    
    print(f"\n📋 Pending Tasks ({len(tasks)}) - Mode: {manager.mode.upper()}")
    print("=" * 60)
    for task in tasks:
        print(f"  {task}")
    print()


def cmd_next(args):
    """Get the next task."""
    manager = TaskManager(mode=args.mode)
    
    if args.peek:
        task = manager.peek_next_task()
        action = "Next task (not removed)"
    else:
        task = manager.get_next_task()
        action = "Got next task"
    
    if task:
        print(f"🎯 {action}:")
        print(f"  {task}")
        
        if not args.peek and args.start:
            task.status = "RUNNING"
            task.started_at = datetime.now()
            manager.save()
            print(f"  ▶️  Started at {task.started_at.strftime('%H:%M:%S')}")
    else:
        print("📭 No tasks in queue!")


def cmd_complete(args):
    """Mark current task as complete."""
    manager = TaskManager(mode=args.mode)
    
    # This is simplified - in a real app, you'd track "current" task
    # For now, we complete the next task
    task = manager.get_next_task()
    if task:
        if not task.started_at:
            task.started_at = datetime.now()
        manager.complete_task(task)
        print(f"✅ Task completed: {task}")
    else:
        print("📭 No tasks to complete!")


def cmd_stats(args):
    """Show queue statistics."""
    manager = TaskManager(mode=args.mode)
    stats = manager.get_statistics()
    
    print(f"\n📊 Task Queue Statistics - Mode: {stats['mode'].upper()}")
    print("=" * 60)
    print(f"  Total tasks: {stats['total_count']}")
    print(f"  Pending: {stats['pending_count']}")
    print(f"  Completed: {stats['completed_count']}")
    
    if "task_types" in stats:
        print(f"\n  Task Types:")
        for task_type, count in stats["task_types"].items():
            print(f"    {task_type}: {count}")
    
    if "avg_priority" in stats:
        print(f"\n  Priority Stats:")
        print(f"    Average: {stats['avg_priority']:.2f}")
        print(f"    Range: {stats['min_priority']}-{stats['max_priority']}")
    
    if "avg_execution_time" in stats:
        print(f"\n  Avg Execution Time: {stats['avg_execution_time']:.2f}s")
    
    print()


def cmd_clear(args):
    """Clear all pending tasks."""
    manager = TaskManager(mode=args.mode)
    count = manager.clear_all()
    print(f"🗑️  Cleared {count} pending tasks!")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Task Queue Manager - FIFO and Priority Queue",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Add tasks
  python task_queue.py add "Fix login bug" --type CPU --priority 1
  python task_queue.py add "Update docs" --type IO --priority 5

  # List all tasks
  python task_queue.py list

  # Get next task (removes from queue)
  python task_queue.py next

  # Peek at next task (doesn't remove)
  python task_queue.py next --peek

  # Mark task as complete
  python task_queue.py complete

  # Show statistics
  python task_queue.py stats

  # Clear all tasks
  python task_queue.py clear

  # Use FIFO mode instead of priority
  python task_queue.py add "Task" --type CPU --priority 3 --mode fifo
        """
    )
    
    # Global options
    parser.add_argument(
        '--mode',
        choices=['fifo', 'priority'],
        default='priority',
        help='Queue mode: fifo (First In First Out) or priority (Priority-based)'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('name', help='Task name/description')
    parser_add.add_argument('--type', choices=['CPU', 'IO', 'NETWORK'], default='CPU',
                           help='Task type (default: CPU)')
    parser_add.add_argument('--priority', type=int, default=3, choices=range(1, 6),
                           help='Priority 1-5 (1=highest, 5=lowest, default: 3)')
    parser_add.set_defaults(func=cmd_add)
    
    # List command
    parser_list = subparsers.add_parser('list', help='List all pending tasks')
    parser_list.set_defaults(func=cmd_list)
    
    # Next command
    parser_next = subparsers.add_parser('next', help='Get next task')
    parser_next.add_argument('--peek', action='store_true',
                            help='Only peek, don\'t remove task')
    parser_next.add_argument('--start', action='store_true',
                            help='Mark task as started')
    parser_next.set_defaults(func=cmd_next)
    
    # Complete command
    parser_complete = subparsers.add_parser('complete', help='Mark task as complete')
    parser_complete.set_defaults(func=cmd_complete)
    
    # Stats command
    parser_stats = subparsers.add_parser('stats', help='Show statistics')
    parser_stats.set_defaults(func=cmd_stats)
    
    # Clear command
    parser_clear = subparsers.add_parser('clear', help='Clear all pending tasks')
    parser_clear.set_defaults(func=cmd_clear)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    args.func(args)


if __name__ == "__main__":
    main()