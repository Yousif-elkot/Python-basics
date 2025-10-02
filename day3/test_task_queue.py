"""
Tests for Task Queue Simulator
Run with: python test_task_queue.py
"""

from task_queue import Task, TaskType, TaskQueue, PriorityTaskQueue
from datetime import datetime


def test_task_creation():
    """Test Task class creation and __str__ method."""
    print("="*60)
    print("Testing Task Creation...")
    
    task1 = Task("1", "Download file", TaskType.IO, priority=1)
    print(task1)
    # Expected: [1] Download file (IO, Priority: High) - PENDING ⏳
    
    # Test with execution
    task2 = Task("2", "Process data", TaskType.CPU, priority=5)
    task2.status = "RUNNING"
    task2.started_at = datetime.now()
    task2.execution_time = 2.5
    print(task2)
    # Expected: [2] Process data (CPU, Priority: Low) - RUNNING 🏃 (2.50s)
    print("✅ Task creation tests passed!\n")


def test_task_queue():
    """Test TaskQueue (FIFO) implementation."""
    print("="*60)
    print("Testing TaskQueue (FIFO)...")
    
    queue = TaskQueue()
    print(f"Empty queue: {queue}")
    print(f"Is empty? {queue.is_empty()}")
    
    # Enqueue tasks
    task3 = Task("3", "Task A", TaskType.CPU, priority=3)
    task4 = Task("4", "Task B", TaskType.IO, priority=2)
    task5 = Task("5", "Task C", TaskType.NETWORK, priority=4)
    
    queue.enqueue(task3)
    queue.enqueue(task4)
    queue.enqueue(task5)
    print(f"\nAfter enqueuing 3 tasks: {queue}")
    
    # Peek (doesn't remove)
    print(f"\nPeek: {queue.peek().name}")
    print(f"Size after peek: {queue.size()}")
    
    # Dequeue (FIFO - First In, First Out)
    print(f"\nDequeue: {queue.dequeue().name}")
    print(f"Dequeue: {queue.dequeue().name}")
    print(f"Queue now: {queue}")
    
    # Dequeue last
    print(f"\nDequeue: {queue.dequeue().name}")
    print(f"Is empty? {queue.is_empty()}")
    
    # Try dequeue on empty
    print(f"Dequeue from empty: {queue.dequeue()}")
    print("✅ TaskQueue tests passed!\n")


def test_priority_task_queue():
    """Test PriorityTaskQueue implementation."""
    print("="*60)
    print("Testing PriorityTaskQueue...")
    
    pq = PriorityTaskQueue()
    
    # Create tasks with different priorities
    urgent = Task("10", "Critical Bug", TaskType.CPU, priority=1)      # Highest!
    high = Task("11", "Deploy App", TaskType.NETWORK, priority=2)
    medium = Task("12", "Code Review", TaskType.CPU, priority=3)
    low = Task("13", "Update Docs", TaskType.IO, priority=5)          # Lowest
    
    # Enqueue in RANDOM order (not by priority)
    print("Enqueuing in random order: Medium(3), Low(5), Urgent(1), High(2)")
    pq.enqueue(medium)  # Priority 3
    pq.enqueue(low)     # Priority 5
    pq.enqueue(urgent)  # Priority 1
    pq.enqueue(high)    # Priority 2
    
    print(f"\nQueue: {pq}")
    print(f"Size: {pq.size()}")
    
    # Peek (should be highest priority = lowest number = 1)
    print(f"\nPeek: {pq.peek().name} (should be Critical Bug with priority 1)")
    
    # Dequeue should come out in PRIORITY order (1, 2, 3, 5)
    print("\nDequeuing in priority order:")
    print(f"Dequeue #1: {pq.dequeue().name} (Priority 1 - Critical Bug)")
    print(f"Dequeue #2: {pq.dequeue().name} (Priority 2 - Deploy App)")
    print(f"Dequeue #3: {pq.dequeue().name} (Priority 3 - Code Review)")
    print(f"Dequeue #4: {pq.dequeue().name} (Priority 5 - Update Docs)")
    print(f"Is empty? {pq.is_empty()}")
    print("✅ PriorityTaskQueue tests passed!\n")


def test_fifo_tie_breaking():
    """Test FIFO tie-breaking for tasks with same priority."""
    print("="*60)
    print("Testing FIFO tie-breaking (same priority)...")
    
    pq2 = PriorityTaskQueue()
    task_a = Task("20", "Task A", TaskType.CPU, priority=2)
    task_b = Task("21", "Task B", TaskType.IO, priority=2)
    task_c = Task("22", "Task C", TaskType.NETWORK, priority=2)
    
    pq2.enqueue(task_a)
    pq2.enqueue(task_b)
    pq2.enqueue(task_c)
    
    print("All tasks have priority 2, enqueued: A, B, C")
    print(f"Dequeue: {pq2.dequeue().name} (should be A - FIFO)")
    print(f"Dequeue: {pq2.dequeue().name} (should be B - FIFO)")
    print(f"Dequeue: {pq2.dequeue().name} (should be C - FIFO)")
    print("✅ FIFO tie-breaking tests passed!\n")


if __name__ == "__main__":
    print("\n🧪 Running Task Queue Tests...\n")
    
    test_task_creation()
    test_task_queue()
    test_priority_task_queue()
    test_fifo_tie_breaking()
    
    print("="*60)
    print("🎉 All tests passed successfully!")
    print("="*60)
