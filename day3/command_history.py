from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
import json

@dataclass
class Command:
    command:str
    timestamp: datetime
    executed: bool  # True if executed, False if pending
    exit_code: Optional[int] = None  # None if not executed yet

    def __str__(self) -> str:
        """String representation of command"""
        if not self.executed:
            status_icon = "○"  # Pending
            exit_code_str = "-"
        elif self.exit_code == 0:
            status_icon = "✓"  # Success
            exit_code_str = "0"
        else:
            status_icon = "✗"  # Failure
            exit_code_str = str(self.exit_code)

        time_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{status_icon} {exit_code_str:3}] {time_str} | {self.command}"
    
    def to_dict(self) -> dict:
        return {
            'command': self.command,
            'timestamp': self.timestamp.isoformat(),  # Convert to string!
            'executed': self.executed,
            'exit_code': self.exit_code
        }
    
    @classmethod  # ← Added th  
    def from_dict(cls, data: dict) -> 'Command':
        return cls(
            command = data['command'],
            timestamp = datetime.fromisoformat(data['timestamp']),  # Convert string back to datetime
            executed = data.get('executed', False),
            exit_code = data.get('exit_code')
        )
    
class CommandStack:
    """"Stack-based command history manager with undo/redo support."""

    def __init__(self, max_size: int = 100):
        """Initialize command stack.
        Args:
            max_size: Maximum number of commands to store
        """
        self._max_size = max_size
        self._history: List[Command] = []  # Main stack
        self._undo_stack: List[Command] = []  # For redo functionality

    def push(self, command: Command) -> bool:
        """Add command to history stack.
        args:
            command: Command to add

        Returns:
            True if successful, False if failed
        """
        self._undo_stack.clear()  # Clear undo stack on new command

        if len(self._history) >= self._max_size:
            self._history.pop(0)  # Remove oldest command
        
        self._history.append(command)  # Always add the new command
        
        return True
    
    def pop(self) -> Optional[Command]:
        """Remove and return most recent command.
        
        Returns:
            Most recent Command or None if empty
        """
        if not self._history:
            return None
        
        cmd = self._history.pop()
        return cmd
    
    def peek(self) -> Optional[Command]:
        """
        View most recent command without removing.
        
        Returns:
            Most recent Command or None if empty
        """
        return self._history[-1] if self._history else None

    def size(self) -> int:
        """Return number of commands in history."""
        return len(self._history)

    def is_empty(self) -> bool:
        """Check if history is empty."""
        return len(self._history) == 0 
    
    def undo(self) -> Optional[Command]:
        """Undo the most recent command.
        
        Returns:
            The undone Command or None if nothing to undo
        """
        if not self._history:
            return None  # Nothing to undo
        
        cmd = self._history.pop()
        self._undo_stack.append(cmd)
        return cmd
    
    def redo(self) -> Optional[Command]:
        """Redo the most recently undone command.
        
        Returns:
            The redone Command or None if nothing to redo
        """
        if not self._undo_stack:
            return None  # Nothing to redo
        
        cmd = self._undo_stack.pop()
        self._history.append(cmd)
        return cmd
    
    def search(self, query: str) -> List[Command]:
        """Search command history for commands containing query.
        
        Args:
            query: Substring to search for (case-insensitive)

        Returns:
            List of matching Command objects (most recent first)
        """
        return [cmd for cmd in reversed(self._history) if query.lower() in cmd.command.lower()]
    
    def get_statistics(self) -> dict:
        """Get statistics about command history.
        
        Returns:
            Dictionary with total, successful, failed, pending counts
        """
        if not self._history:
            return {'total': 0}
        
        #count total
        total = len(self._history)

        #count executed vs not executed
        executed = sum(1 for cmd in self._history if cmd.executed)

        #find most common command
        from collections import Counter
        command_counts = Counter(cmd.command for cmd in self._history)
        most_common = command_counts.most_common(1)[0] if command_counts else ( None, 0)

        #time span
        oldest = self._history[0].timestamp
        newest = self._history[-1].timestamp
        time_span = (newest - oldest).total_seconds()

        return {
            'total': total,
            'executed': executed,
            'not_executed': total - executed,
            'most_common_command': most_common[0],
            'most_common_count': most_common[1],
            'time_span_seconds': time_span
        }
    
    def save_to_json(self, filename: str) -> None:
        """
        Save command history to JSON file.
        
        Args:  
            filepath: Path to JSON file
        
        Returns:
            True if successful, False otherwise

        """
        try:
            data = {
                'history': [cmd.to_dict() for cmd in self._history],
                'undo_stack': [cmd.to_dict() for cmd in self._undo_stack],
                'max_size': self._max_size
            }

            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)

            return True
        except Exception as e:
            print(f"Error saving to JSON: {e}")
            return False

    def load_from_json(self, filename: str) -> bool:
        """
        Load command history from JSON file.
        
        Args:
            filename: Path to JSON file    

        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)

                # restore history
                self._history = [Command.from_dict(cmd) for cmd in data.get('history', [])]

                # restore undo stack
                self._undo_stack = [Command.from_dict(cmd) for cmd in data.get('undo_stack', [])]

                # restore max size
                self._max_size = data.get('max_size', 100)
            
            return True
        except FileNotFoundError:
            print(f"File not found: {filename}")
            return False
        except Exception as e:
            print(f"Error loading from JSON: {e}")
            return False

# Testing code
if __name__ == "__main__":
    print("Testing Command class...")
    print("=" * 60)
    
    # Test 1: Create a command
    cmd1 = Command("git status", datetime.now(), True, 0)
    print("Test 1 - Successful command:")
    print(cmd1)
    print()
    
    # Test 2: Failed command
    cmd2 = Command("make build", datetime.now(), True, 127)
    print("Test 2 - Failed command:")
    print(cmd2)
    print()
    
    # Test 3: Not executed yet
    cmd3 = Command("ls -la", datetime.now(), executed=False)
    print("Test 3 - Not executed:")
    print(cmd3)
    print()
    
    # Test 4: to_dict and from_dict
    print("Test 4 - JSON serialization:")
    cmd_dict = cmd1.to_dict()
    print(f"Dictionary: {cmd_dict}")
    
    cmd_restored = Command.from_dict(cmd_dict)
    print(f"Restored: {cmd_restored}")
    print(f"Match: {cmd1.command == cmd_restored.command}")
    print()
    
    print("✅ All tests complete!")
    print("\n" + "=" * 60)
        
    print("Testing CommandStack...")
    print("=" * 60)
    
    # Create stack
    stack = CommandStack(max_size=3)
    
    # Test push
    print("\n1. Testing push:")
    stack.push(Command("ls", datetime.now(), True, 0))
    stack.push(Command("cd /tmp", datetime.now(), True, 0))
    stack.push(Command("pwd", datetime.now(), True, 0))
    print(f"Stack size: {stack.size()}")
    
    # Test peek
    print("\n2. Testing peek:")
    top = stack.peek()
    print(f"Top command: {top.command if top else 'None'}")
    print(f"Size after peek: {stack.size()}")  # Should still be 3
    
    # Test pop
    print("\n3. Testing pop:")
    popped = stack.pop()
    print(f"Popped: {popped.command if popped else 'None'}")
    print(f"Size after pop: {stack.size()}")  # Should be 2
    
    # Test max size
    print("\n4. Testing max size (limit=3):")
    stack.push(Command("git status", datetime.now(), True, 0))
    stack.push(Command("git commit", datetime.now(), True, 0))  # This should remove oldest!
    print(f"Size: {stack.size()}")  # Should still be 3
    
    print("\n5. Testing undo/redo:")
    print("Initial history:")
    stack = CommandStack()
    stack.push(Command("ls", datetime.now(), True, 0))
    stack.push(Command("cd /tmp", datetime.now(), True, 0))
    stack.push(Command("pwd", datetime.now(), True, 0))
    print(f"  Size: {stack.size()}")
    
    # Undo
    print("\nAfter undo:")
    undone = stack.undo()
    print(f"  Undone: {undone.command if undone else 'None'}")
    print(f"  History size: {stack.size()}")
    
    # Undo again
    print("\nAfter second undo:")
    undone = stack.undo()
    print(f"  Undone: {undone.command if undone else 'None'}")
    print(f"  History size: {stack.size()}")
    
    # Redo
    print("\nAfter redo:")
    redone = stack.redo()
    print(f"  Redone: {redone.command if redone else 'None'}")
    print(f"  History size: {stack.size()}")
    
    # Add new command (should clear undo stack!)
    print("\nAfter adding new command:")
    stack.push(Command("git status", datetime.now(), True, 0))
    print(f"  History size: {stack.size()}")
    print(f"  Can redo? {stack.redo() is not None}")  # Should be False!
    
    print("\n✅ Undo/Redo tests complete!")

    print("\n6. Testing search:")
    stack = CommandStack()
    stack.push(Command("git status", datetime.now(), True, 0))
    stack.push(Command("git commit", datetime.now(), True, 0))
    stack.push(Command("ls -la", datetime.now(), True, 0))
    stack.push(Command("git push", datetime.now(), True, 0))
    
    results = stack.search("git")
    print(f"  Found {len(results)} commands with 'git':")
    for cmd in results:
        print(f"    - {cmd.command}")
    
    print("\n7. Testing statistics:")
    stats = stack.get_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n✅ Search & Stats tests complete!")

    print("\n8. Testing JSON save/load:")
    
    # Create and populate a stack
    stack1 = CommandStack()
    stack1.push(Command("ls -la", datetime.now(), True, 0))
    stack1.push(Command("cd /tmp", datetime.now(), True, 0))
    stack1.push(Command("pwd", datetime.now(), True, 0))
    stack1.undo()  # Put one in undo stack
    
    print(f"  Original stack size: {stack1.size()}")
    print(f"  Original history: {[cmd.command for cmd in stack1._history]}")
    
    # Save to file
    filename = "test_history.json"
    if stack1.save_to_json(filename):
        print(f"  ✅ Saved to {filename}")
    
    # Create new stack and load
    stack2 = CommandStack()
    if stack2.load_from_json(filename):
        print(f"  ✅ Loaded from {filename}")
        print(f"  Loaded stack size: {stack2.size()}")
        print(f"  Loaded history: {[cmd.command for cmd in stack2._history]}")
        
        # Test that undo stack was restored
        redone = stack2.redo()
        print(f"  Can redo? {redone is not None}")
        if redone:
            print(f"  Redone command: {redone.command}")
    
    # Clean up
    import os
    if os.path.exists(filename):
        os.remove(filename)
        print(f"  🗑️  Cleaned up {filename}")
    
    print("\n✅ JSON save/load tests complete!")