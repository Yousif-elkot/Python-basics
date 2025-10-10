# 🖥️ Step 4: CLI Interface - Make it a Real Tool!

## 🎯 Goal
Transform your directory explorer into a professional command-line tool using `argparse`.

---

## 📊 What You'll Build

### **Two Commands:**

```bash
# Command 1: Show directory tree
python dir_explorer.py show . --depth 2

# Command 2: Show statistics
python dir_explorer.py stats /home/user/project
```

---

## 🧠 Understanding argparse with Subcommands

### **The Pattern:**

```python
parser = argparse.ArgumentParser(description="...")

# Create subparsers for different commands
subparsers = parser.add_subparsers(dest='command')

# Add 'show' command
show_parser = subparsers.add_parser('show', help='Display directory tree')
show_parser.add_argument('path', help='Directory to scan')
show_parser.add_argument('--depth', type=int, help='Max depth')

# Add 'stats' command
stats_parser = subparsers.add_parser('stats', help='Show statistics')
stats_parser.add_argument('path', help='Directory to scan')

# Parse arguments
args = parser.parse_args()

# Call appropriate function
if args.command == 'show':
    cmd_show(args)
elif args.command == 'stats':
    cmd_stats(args)
```

---

## 📝 Implementation Guide

### **Function 1: `cmd_show(args)`**

Displays the directory tree.

```python
def cmd_show(args):
    """Handle the 'show' command."""
    # 1. Create explorer with ignore patterns
    ignore = args.ignore if args.ignore else ['.git', '__pycache__', '.venv', 'node_modules']
    explorer = DirectoryExplorer(ignore_patterns=ignore)
    
    # 2. Check if path exists
    if not os.path.exists(args.path):
        print(f"Error: Path '{args.path}' does not exist")
        return
    
    # 3. Scan the directory
    print(f"Scanning {args.path}...")
    root = explorer.scan_directory(args.path, max_depth=args.depth)
    
    # 4. Display the tree
    print()
    explorer.display_tree(root)
    
    # 5. Show summary
    total_size = root.get_total_size()
    print(f"\nTotal size: {explorer.format_size(total_size)}")
```

---

### **Function 2: `cmd_stats(args)`**

Shows directory statistics.

```python
def cmd_stats(args):
    """Handle the 'stats' command."""
    # 1. Create explorer
    ignore = args.ignore if args.ignore else ['.git', '__pycache__', '.venv', 'node_modules']
    explorer = DirectoryExplorer(ignore_patterns=ignore)
    
    # 2. Check if path exists
    if not os.path.exists(args.path):
        print(f"Error: Path '{args.path}' does not exist")
        return
    
    # 3. Scan the directory
    print(f"Analyzing {args.path}...")
    root = explorer.scan_directory(args.path)
    
    # 4. Count files and directories
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
    
    # 5. Display statistics
    print("\n" + "=" * 60)
    print(f"📊 Statistics for: {args.path}")
    print("=" * 60)
    print(f"Files:       {files}")
    print(f"Directories: {dirs}")
    print(f"Total Size:  {explorer.format_size(total_size)}")
    print("=" * 60)
```

---

### **Function 3: `main()`**

Sets up argparse and routes commands.

```python
def main():
    """Main CLI entry point."""
    # 1. Create main parser
    parser = argparse.ArgumentParser(
        description='Directory Tree Explorer - Visualize directory structures',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s show . --depth 2
  %(prog)s show /home/user/project --ignore .git __pycache__
  %(prog)s stats .
  %(prog)s stats /home/user/project
        """
    )
    
    # 2. Create subparsers for commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # 3. Add 'show' command
    show_parser = subparsers.add_parser(
        'show',
        help='Display directory tree with ASCII art'
    )
    show_parser.add_argument(
        'path',
        help='Directory path to display'
    )
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
    
    # 4. Add 'stats' command
    stats_parser = subparsers.add_parser(
        'stats',
        help='Show directory statistics'
    )
    stats_parser.add_argument(
        'path',
        help='Directory path to analyze'
    )
    stats_parser.add_argument(
        '--ignore',
        nargs='+',
        help='Patterns to ignore'
    )
    
    # 5. Parse arguments
    args = parser.parse_args()
    
    # 6. Check if command was provided
    if not args.command:
        parser.print_help()
        return
    
    # 7. Route to appropriate function
    if args.command == 'show':
        cmd_show(args)
    elif args.command == 'stats':
        cmd_stats(args)
```

---

## 🔑 Key Concepts

### **1. Subparsers**

Allows multiple commands in one program:
```python
subparsers = parser.add_subparsers(dest='command')
show_parser = subparsers.add_parser('show')
stats_parser = subparsers.add_parser('stats')
```

### **2. Positional Arguments**

Required arguments:
```python
parser.add_argument('path', help='Directory to scan')
```

Usage: `python dir_explorer.py show /path/to/dir`

### **3. Optional Arguments**

Optional flags:
```python
parser.add_argument('--depth', type=int, default=None)
parser.add_argument('--ignore', nargs='+')  # Multiple values
```

Usage: `python dir_explorer.py show . --depth 2 --ignore .git __pycache__`

### **4. Smart Mode Detection**

```python
if len(sys.argv) == 1:
    # No arguments - run tests
    run_tests()
else:
    # Arguments provided - run CLI
    main()
```

---

## 📋 Usage Examples

### **Show Command:**

```bash
# Show current directory (depth 2)
python dir_explorer.py show . --depth 2

# Show project folder (unlimited depth)
python dir_explorer.py show /home/user/myproject

# Show with ignore patterns
python dir_explorer.py show . --ignore .git __pycache__ node_modules
```

### **Stats Command:**

```bash
# Analyze current directory
python dir_explorer.py stats .

# Analyze project folder
python dir_explorer.py stats /home/user/myproject

# Analyze with ignore patterns
python dir_explorer.py stats . --ignore .git .venv
```

### **Help:**

```bash
# General help
python dir_explorer.py --help

# Help for specific command
python dir_explorer.py show --help
python dir_explorer.py stats --help
```

### **Test Mode:**

```bash
# Run tests (no arguments)
python dir_explorer.py
```

---

## ✅ Testing Strategy

1. **Test with no arguments** - Should run tests
2. **Test help** - `python dir_explorer.py --help`
3. **Test show command** - `python dir_explorer.py show .`
4. **Test with depth** - `python dir_explorer.py show . --depth 1`
5. **Test stats command** - `python dir_explorer.py stats .`
6. **Test ignore patterns** - `python dir_explorer.py show . --ignore .git`
7. **Test invalid path** - Should show error message

---

## 🎯 Success Criteria

After implementing, you should be able to:
- ✅ Run tool from command line
- ✅ Use `show` command to display tree
- ✅ Use `stats` command for statistics
- ✅ Specify depth limit
- ✅ Ignore specific patterns
- ✅ See helpful error messages
- ✅ View help documentation
- ✅ Run tests when no arguments provided

---

## 💡 Bonus Features (Optional)

- Add `--size` flag to show file sizes in tree
- Add colors (directories in blue, files in white)
- Add `--sort` option (by name, size, date)
- Save output to file: `--output tree.txt`

---

## 🚀 Ready to Code!

Implement the 3 functions:
1. `cmd_show()` - Display tree command
2. `cmd_stats()` - Statistics command
3. `main()` - Argparse setup and routing

Then test it out:
```bash
python dir_explorer.py show . --depth 2
```

You'll have a real, professional CLI tool! 🛠️
