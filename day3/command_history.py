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

# CLI Interface
def main():
    """Command-line interface for the command history manager."""
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(
        description='Professional Command History Manager with Undo/Redo',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s add "git status" -e 0          Add successful command
  %(prog)s add "make build" -e 1          Add failed command
  %(prog)s list                           Show all history
  %(prog)s list -n 10                     Show last 10 commands
  %(prog)s search git                     Search for 'git' commands
  %(prog)s undo                           Undo last command
  %(prog)s redo                           Redo undone command
  %(prog)s stats                          Show statistics
  %(prog)s save history.json              Save to file
  %(prog)s load history.json              Load from file
        '''
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a command to history')
    add_parser.add_argument('cmd', help='Command to add')
    add_parser.add_argument('-e', '--exit-code', type=int, default=0, help='Exit code (default: 0)')
    add_parser.add_argument('-f', '--file', default='command_history.json', help='History file')
    
    # List commands
    list_parser = subparsers.add_parser('list', help='List command history')
    list_parser.add_argument('-n', '--number', type=int, help='Number of recent commands to show')
    list_parser.add_argument('-f', '--file', default='command_history.json', help='History file')
    
    # Search commands
    search_parser = subparsers.add_parser('search', help='Search command history')
    search_parser.add_argument('query', help='Search query')
    search_parser.add_argument('-f', '--file', default='command_history.json', help='History file')
    
    # Undo command
    undo_parser = subparsers.add_parser('undo', help='Undo last command')
    undo_parser.add_argument('-f', '--file', default='command_history.json', help='History file')
    
    # Redo command
    redo_parser = subparsers.add_parser('redo', help='Redo undone command')
    redo_parser.add_argument('-f', '--file', default='command_history.json', help='History file')
    
    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Show statistics')
    stats_parser.add_argument('-f', '--file', default='command_history.json', help='History file')
    
    # Save command
    save_parser = subparsers.add_parser('save', help='Save history to file')
    save_parser.add_argument('output', help='Output file path')
    save_parser.add_argument('-f', '--file', default='command_history.json', help='Current history file')
    
    # Load command
    load_parser = subparsers.add_parser('load', help='Load history from file')
    load_parser.add_argument('input', help='Input file path')
    load_parser.add_argument('-f', '--file', default='command_history.json', help='History file to save to')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Create/load stack
    stack = CommandStack(max_size=1000)
    import os
    if os.path.exists(args.file):
        stack.load_from_json(args.file)
    
    # Execute command
    if args.command == 'add':
        cmd = Command(
            command=args.cmd,
            timestamp=datetime.now(),
            executed=True,
            exit_code=args.exit_code
        )
        stack.push(cmd)
        stack.save_to_json(args.file)
        print(f"✅ Added: {cmd}")
    
    elif args.command == 'list':
        if stack.is_empty():
            print("📭 No commands in history")
        else:
            commands = list(reversed(stack._history))  # Most recent first
            if args.number:
                commands = commands[:args.number]
            
            print(f"📜 Command History ({len(commands)} commands):")
            print("=" * 80)
            for i, cmd in enumerate(commands, 1):
                print(f"{i:3}. {cmd}")
    
    elif args.command == 'search':
        results = stack.search(args.query)
        if not results:
            print(f"🔍 No commands found matching '{args.query}'")
        else:
            print(f"🔍 Found {len(results)} commands matching '{args.query}':")
            print("=" * 80)
            for i, cmd in enumerate(results, 1):
                print(f"{i:3}. {cmd}")
    
    elif args.command == 'undo':
        undone = stack.undo()
        if undone:
            stack.save_to_json(args.file)
            print(f"↩️  Undone: {undone}")
        else:
            print("⚠️  Nothing to undo")
    
    elif args.command == 'redo':
        redone = stack.redo()
        if redone:
            stack.save_to_json(args.file)
            print(f"↪️  Redone: {redone}")
        else:
            print("⚠️  Nothing to redo")
    
    elif args.command == 'stats':
        if stack.is_empty():
            print("📭 No commands in history")
        else:
            stats = stack.get_statistics()
            print("📊 Command History Statistics:")
            print("=" * 80)
            print(f"  Total commands:       {stats['total']}")
            print(f"  Executed:             {stats['executed']}")
            print(f"  Not executed:         {stats['not_executed']}")
            print(f"  Most common command:  {stats['most_common_command']}")
            print(f"  Occurrences:          {stats['most_common_count']}")
            
            if stats['time_span_seconds'] > 0:
                hours = stats['time_span_seconds'] / 3600
                print(f"  Time span:            {hours:.2f} hours")
    
    elif args.command == 'save':
        if stack.save_to_json(args.output):
            print(f"💾 Saved history to {args.output}")
        else:
            print(f"❌ Failed to save to {args.output}")
    
    elif args.command == 'load':
        if stack.load_from_json(args.input):
            stack.save_to_json(args.file)
            print(f"📂 Loaded history from {args.input}")
            print(f"   Total commands: {stack.size()}")
        else:
            print(f"❌ Failed to load from {args.input}")


if __name__ == "__main__":
    main()