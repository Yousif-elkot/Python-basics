#!/usr/bin/env python3
"""
Directory Tree Explorer
Day 4 - Project 2

A command-line tool for exploring directory structures.
Displays directories as beautiful ASCII trees, similar to the Unix 'tree' command.

Usage:
    python dir_explorer.py show <path> [--depth N] [--ignore PATTERN ...]
    python dir_explorer.py stats <path> [--ignore PATTERN ...]
    
Examples:
    python dir_explorer.py show . --depth 2
    python dir_explorer.py show /path/to/project --ignore .git __pycache__
    python dir_explorer.py stats .
"""

import os
import argparse
import sys
from typing import List, Optional


class DirectoryNode:
    """
    Represents a file or directory in the file system tree.
    
    Attributes:
        name (str): File or directory name
        path (str): Full path to the file or directory
        is_directory (bool): True if directory, False if file
        size (int): File size in bytes (0 for directories)
        children (List[DirectoryNode]): Child nodes (for directories)
    """
    
    def __init__(self, name: str, path: str, is_directory: bool):
        """Initialize a DirectoryNode with name, path, and type."""
        self.name = name
        self.path = path
        self.is_directory = is_directory
        self.children: List['DirectoryNode'] = []
        
        if is_directory:
            self.size = 0
        else:
            try:
                self.size = os.path.getsize(path)
            except OSError:
                self.size = 0

    def add_child(self, child_node: 'DirectoryNode') -> None:
        """Add a child node to this directory."""
        if self.is_directory:
            self.children.append(child_node)

    def get_total_size(self) -> int:
        """Calculate total size of this node and all children (recursive)."""
        total = self.size
        for child in self.children:
            total += child.get_total_size()
        return total

    def __repr__(self) -> str:
        """String representation for debugging."""
        node_type = 'directory' if self.is_directory else 'file'
        return f"DirectoryNode({self.name}, {node_type})"


class DirectoryExplorer:
    """
    Main engine for scanning directories and building trees.
    
    Provides methods to:
    - Recursively scan directories
    - Build DirectoryNode trees
    - Display trees with ASCII art
    - Format file sizes
    """
    
    def __init__(self, ignore_patterns: Optional[List[str]] = None):
        """Initialize the DirectoryExplorer with optional ignore patterns."""
        self.ignore_patterns = ignore_patterns or []
    
    def _should_ignore(self, name: str) -> bool:
        """Check if a file or folder should be ignored."""
        return name in self.ignore_patterns
    
    def scan_directory(
        self,
        path: str,
        current_depth: int = 0,
        max_depth: Optional[int] = None
    ) -> DirectoryNode:
        """
        Recursively scan a directory and build a tree of DirectoryNodes.
        
        Args:
            path: Path to scan
            current_depth: Current recursion depth (starts at 0)
            max_depth: Maximum depth to scan (None = unlimited)
            
        Returns:
            DirectoryNode: Root node of the scanned tree
        """
        name = os.path.basename(path) or path
        is_directory = os.path.isdir(path)
        node = DirectoryNode(name, path, is_directory)
        
        # Base case 1: max depth reached
        if max_depth is not None and current_depth >= max_depth:
            return node
        
        # Base case 2: it's a file
        if not is_directory:
            return node
        
        # Recursive case: scan directory
        try:
            for item in os.listdir(path):
                if self._should_ignore(item):
                    continue
                
                full_path = os.path.join(path, item)
                child_node = self.scan_directory(
                    full_path,
                    current_depth + 1,
                    max_depth
                )
                node.add_child(child_node)
        except OSError as e:
            pass  # Silently skip inaccessible directories
        
        return node
    
    def display_tree(
        self,
        node: Optional[DirectoryNode] = None,
        prefix: str = "",
        is_last: bool = True
    ) -> None:
        """
        Display the directory tree with beautiful ASCII art.
        
        Args:
            node: Node to display
            prefix: String prefix for indentation
            is_last: Whether this is the last child
        """
        if node is None:
            return
        
        # Print current node
        connector = "└── " if is_last else "├── "
        suffix = "/" if node.is_directory else ""
        print(f"{prefix}{connector}{node.name}{suffix}")
        
        # Print children
        if node.is_directory and node.children:
            new_prefix = prefix + ("   " if is_last else "│  ")
            for i, child in enumerate(node.children):
                is_last_child = (i == len(node.children) - 1)
                self.display_tree(child, new_prefix, is_last_child)
    
    def format_size(self, size_bytes: int) -> str:
        """
        Format size in bytes to human-readable format.
        
        Args:
            size_bytes: Size in bytes
            
        Returns:
            Formatted string (e.g., "1.5 MB", "500 bytes")
        """
        if size_bytes < 1024:
            return f"{size_bytes} bytes"
        elif size_bytes < 1024 ** 2:
            return f"{size_bytes / 1024:.1f} KB"
        elif size_bytes < 1024 ** 3:
            return f"{size_bytes / (1024 ** 2):.1f} MB"
        else:
            return f"{size_bytes / (1024 ** 3):.1f} GB"


def cmd_show(args):
    """Handle the 'show' command - Display directory tree."""
    ignore = args.ignore if args.ignore else ['.git', '__pycache__', '.venv', 'node_modules']
    explorer = DirectoryExplorer(ignore_patterns=ignore)
    
    if not os.path.exists(args.path):
        print(f"Error: Path '{args.path}' does not exist.")
        return
    
    print(f"\nScanning directory: {args.path}...\n")
    root = explorer.scan_directory(args.path, max_depth=args.depth)
    
    print(f"Directory Tree for: {args.path}\n")
    explorer.display_tree(root)
    
    total_size = root.get_total_size()
    print(f"\nTotal size: {explorer.format_size(total_size)}\n")


def cmd_stats(args):
    """Handle the 'stats' command - Show directory statistics."""
    ignore = args.ignore if args.ignore else ['.git', '__pycache__', '.venv', 'node_modules']
    explorer = DirectoryExplorer(ignore_patterns=ignore)
    
    if not os.path.exists(args.path):
        print(f"Error: Path '{args.path}' does not exist.")
        return
    
    print(f"Analyzing {args.path}...\n")
    root = explorer.scan_directory(args.path)
    
    # Count files and directories
    def count_nodes(node):
        if not node.is_directory:
            return 1, 0  # 1 file, 0 dirs
        
        files = 0
        dirs = 1  # Count this directory
        for child in node.children:
            f, d = count_nodes(child)
            files += f
            dirs += d
        return files, dirs
    
    files, dirs = count_nodes(root)
    total_size = root.get_total_size()
    
    # Display statistics
    print("\n" + "=" * 60)
    print(f"📊 Statistics for: {args.path}")
    print("=" * 60)
    print(f"Files:       {files}")
    print(f"Directories: {dirs}")
    print(f"Total Size:  {explorer.format_size(total_size)}")
    print("=" * 60 + "\n")


def main():
    """Main CLI entry point using argparse."""
    parser = argparse.ArgumentParser(
        description='Directory Tree Explorer - Visualize directory structures',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s show . --depth 2
  %(prog)s show /path/to/project --ignore .git __pycache__
  %(prog)s stats .
  %(prog)s stats /path/to/project
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # 'show' command
    show_parser = subparsers.add_parser(
        'show',
        help='Display directory tree with ASCII art'
    )
    show_parser.add_argument('path', help='Directory path to display')
    show_parser.add_argument(
        '--depth',
        type=int,
        default=None,
        help='Maximum depth to display (default: unlimited)'
    )
    show_parser.add_argument(
        '--ignore',
        nargs='+',
        help='Patterns to ignore (e.g., .git __pycache__)'
    )
    
    # 'stats' command
    stats_parser = subparsers.add_parser(
        'stats',
        help='Show directory statistics'
    )
    stats_parser.add_argument('path', help='Directory path to analyze')
    stats_parser.add_argument(
        '--ignore',
        nargs='+',
        help='Patterns to ignore'
    )
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == 'show':
        cmd_show(args)
    elif args.command == 'stats':
        cmd_stats(args)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("🧪 No arguments provided. Use --help for usage information.\n")
        print("Examples:")
        print("  python dir_explorer.py show . --depth 2")
        print("  python dir_explorer.py stats .")
        print()
    else:
        main()
