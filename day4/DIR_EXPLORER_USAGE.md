# Directory Tree Explorer - Usage Guide

## Overview

The **Directory Tree Explorer** is a command-line tool for visualizing and analyzing directory structures. It displays directories as beautiful ASCII trees (similar to the Unix `tree` command) and provides detailed statistics about file counts and sizes.

**Key Features:**
- 🌳 **ASCII Tree Visualization** - Beautiful tree structure with box-drawing characters
- 📊 **Directory Statistics** - Count files, directories, and calculate total sizes
- 🔍 **Depth Control** - Limit how deep to scan
- 🚫 **Ignore Patterns** - Skip unwanted directories (.git, node_modules, etc.)
- ⚡ **Fast & Lightweight** - Uses only Python standard library
- 🛡️ **Safe** - Handles permission errors gracefully

## Installation

**Requirements:**
- Python 3.7 or higher
- No external dependencies (uses standard library only)

**Setup:**
```bash
# Navigate to the tool directory
cd day4/Directory\ Tree\ Explorer/

# Make executable (optional)
chmod +x dir_explorer.py

# Test it works
python dir_explorer.py --help
```

## Quick Start

```bash
# Show directory tree for current directory
python dir_explorer.py show .

# Show with depth limit
python dir_explorer.py show . --depth 2

# Show directory statistics
python dir_explorer.py stats .

# Explore a specific project
python dir_explorer.py show /path/to/project --depth 3
```

## Commands Reference

### 1. `show` - Display Directory Tree

Displays a visual tree representation of the directory structure.

**Syntax:**
```bash
python dir_explorer.py show <path> [--depth N] [--ignore PATTERN ...]
```

**Arguments:**
- `<path>` - Directory path to display (required)
  - Use `.` for current directory
  - Use `..` for parent directory
  - Use absolute paths like `/home/user/project`
  - Use relative paths like `../../my-project`

**Options:**
- `--depth N` - Maximum depth to display (default: unlimited)
  - `--depth 1` shows only immediate children
  - `--depth 2` shows 2 levels deep
  - No limit if omitted
  
- `--ignore PATTERN [PATTERN ...]` - Patterns to ignore
  - Space-separated list of directory/file names
  - Default: `.git __pycache__ .venv node_modules`

**Examples:**

```bash
# Basic usage
python dir_explorer.py show .
```
Output:
```
Directory Tree for: .
└── ./
   ├── dir_explorer.py
   ├── README.md
   └── tests/
      ├── test_basic.py
      └── test_advanced.py

Total size: 45.3 KB
```

```bash
# Limit depth to 2 levels
python dir_explorer.py show /home/user/projects --depth 2
```

```bash
# Ignore specific patterns
python dir_explorer.py show . --ignore .git __pycache__ node_modules build dist
```

```bash
# Show parent directory
python dir_explorer.py show ../. --depth 3
```

### 2. `stats` - Show Directory Statistics

Analyzes directory and displays statistics about file counts and sizes.

**Syntax:**
```bash
python dir_explorer.py stats <path> [--ignore PATTERN ...]
```

**Arguments:**
- `<path>` - Directory path to analyze (required)

**Options:**
- `--ignore PATTERN [PATTERN ...]` - Patterns to ignore (same as `show`)

**Examples:**

```bash
# Get statistics for current directory
python dir_explorer.py stats .
```
Output:
```
============================================================
📊 Statistics for: .
============================================================
Files:       42
Directories: 8
Total Size:  2.3 MB
============================================================
```

```bash
# Analyze a project folder
python dir_explorer.py stats /home/user/my-project
```

```bash
# Ignore build artifacts
python dir_explorer.py stats . --ignore .git node_modules build dist __pycache__
```

## Common Use Cases

### 1. **Explore New Project Structure**
When you clone a new project and want to understand its structure:

```bash
# Quick overview (2 levels)
python dir_explorer.py show /path/to/new-project --depth 2

# See everything
python dir_explorer.py show /path/to/new-project
```

### 2. **Find Large Directories**
Check which directories are taking up space:

```bash
# Get total size
python dir_explorer.py stats ~/Downloads

# Explore subdirectories
python dir_explorer.py show ~/Downloads --depth 2
```

### 3. **Document Project Structure**
Generate tree structure for documentation:

```bash
# Create tree diagram (redirect output)
python dir_explorer.py show . --depth 3 > project_structure.txt
```

### 4. **Clean Development Folders**
Identify what's in your project before cleaning:

```bash
# See everything (including build artifacts)
python dir_explorer.py stats .

# See everything except build artifacts
python dir_explorer.py stats . --ignore build dist node_modules __pycache__ .git
```

### 5. **Compare Directory Sizes**
Check size before and after operations:

```bash
# Before cleanup
python dir_explorer.py stats ~/my-project

# After cleanup
python dir_explorer.py stats ~/my-project
```

## Understanding the Output

### Tree Symbols
The ASCII tree uses these box-drawing characters:

```
└── Last item in a directory
├── Middle item in a directory
│   Vertical line for deeper levels
   Space for last branch
```

**Example:**
```
./
├── folder1/          ← Middle item
│  ├── file1.txt     ← Middle item in folder1
│  └── file2.txt     ← Last item in folder1
└── folder2/          ← Last item in root
   └── file3.txt     ← Last item in folder2
```

### Size Format
Sizes are displayed in human-readable format:

- **bytes** - For very small files (< 1 KB)
- **KB** - Kilobytes (1,024 bytes)
- **MB** - Megabytes (1,024 KB)
- **GB** - Gigabytes (1,024 MB)

Examples:
- `500 bytes`
- `15.4 KB`
- `2.3 MB`
- `1.5 GB`

### Directory Markers
Directories are shown with a trailing `/`:
- `folder/` - Directory
- `file.txt` - File

## Tips & Best Practices

### Performance Tips

1. **Use Depth Limits for Large Directories**
   ```bash
   # Fast overview of deep structure
   python dir_explorer.py show /large/directory --depth 3
   ```

2. **Ignore Build Artifacts**
   ```bash
   # Much faster when ignoring node_modules, etc.
   python dir_explorer.py show . --ignore node_modules .git build dist
   ```

3. **Start Small**
   ```bash
   # Test with current directory first
   python dir_explorer.py show . --depth 1
   
   # Then go deeper
   python dir_explorer.py show . --depth 3
   ```

### Common Ignore Patterns

**Python Projects:**
```bash
python dir_explorer.py show . --ignore __pycache__ .venv .git .pytest_cache dist build *.egg-info
```

**JavaScript/Node Projects:**
```bash
python dir_explorer.py show . --ignore node_modules .git build dist .next .cache
```

**General Development:**
```bash
python dir_explorer.py show . --ignore .git .venv .env node_modules build dist __pycache__
```

### Permission Errors
The tool handles permission errors gracefully:
- Inaccessible directories are skipped silently
- No crashes or error messages for permission issues
- Continues scanning remaining directories

### Output Redirection
Save output to file for documentation:

```bash
# Save tree structure
python dir_explorer.py show . --depth 3 > docs/structure.txt

# Save statistics
python dir_explorer.py stats . > stats_report.txt
```

## Troubleshooting

### "Path does not exist"
**Problem:** Error message says path doesn't exist

**Solutions:**
- Check spelling of the path
- Use absolute paths to avoid confusion
- Use quotes for paths with spaces: `"path/with spaces"`

### No Output or Truncated Tree
**Problem:** Tree seems incomplete

**Solutions:**
- Check if depth limit is too low (`--depth`)
- Verify directory isn't empty
- Check if patterns are ignoring too much (`--ignore`)

### Performance Issues
**Problem:** Tool is slow on large directories

**Solutions:**
- Add depth limit: `--depth 3`
- Ignore large directories: `--ignore node_modules .git`
- Start with smaller subdirectories

### Size Calculation Seems Wrong
**Problem:** Total size doesn't match expectations

**Solutions:**
- Check if you're ignoring directories with `--ignore`
- Remember symbolic links aren't followed
- Inaccessible files (permission denied) count as 0 bytes

## Technical Details

### How It Works

**Recursive Directory Scanning:**
1. Start at root path
2. Create node for current item
3. If it's a directory, scan all children
4. Recursively process each child
5. Build tree structure from bottom up

**Size Calculation:**
- Files: `os.path.getsize()` for actual size
- Directories: Sum of all children sizes (recursive)
- Inaccessible files: Count as 0 bytes

**Tree Display Algorithm:**
1. Start at root node
2. Print current node with appropriate connector
3. Recursively print all children
4. Track depth with prefix strings
5. Use different connectors for last vs middle items

### Recursion Patterns Used

This project demonstrates three key recursion patterns:

1. **Tree Building** (`scan_directory`)
   - Base case: File or max depth reached
   - Recursive case: Process all children

2. **Tree Traversal** (`display_tree`)
   - Base case: Node is None
   - Recursive case: Display node, then children

3. **Aggregation** (`get_total_size`)
   - Base case: File size
   - Recursive case: Sum of all children

### Limitations

- **Symbolic Links:** Not followed (avoids infinite loops)
- **Hidden Files:** Shown unless explicitly ignored
- **Permissions:** Can't access protected directories
- **Large Directories:** May be slow without depth limits
- **Cross-Platform:** Path handling may vary on Windows

## Examples Gallery

### Example 1: Python Project
```bash
$ python dir_explorer.py show ~/my-python-project --depth 2

Directory Tree for: ~/my-python-project
└── my-python-project/
   ├── README.md
   ├── setup.py
   ├── requirements.txt
   ├── src/
   │  ├── __init__.py
   │  ├── main.py
   │  └── utils.py
   ├── tests/
   │  ├── __init__.py
   │  └── test_main.py
   └── docs/
      ├── index.md
      └── api.md

Total size: 145.2 KB
```

### Example 2: Statistics Report
```bash
$ python dir_explorer.py stats ~/large-project

============================================================
📊 Statistics for: ~/large-project
============================================================
Files:       1,247
Directories: 183
Total Size:  523.4 MB
============================================================
```

### Example 3: Filtered View
```bash
$ python dir_explorer.py show . --depth 2 --ignore .git node_modules build

Directory Tree for: .
└── ./
   ├── src/
   │  ├── components/
   │  └── utils/
   ├── public/
   │  └── images/
   ├── package.json
   └── README.md

Total size: 2.1 MB
```

## Advanced Usage

### Create Alias for Quick Access
Add to your `~/.bashrc` or `~/.zshrc`:

```bash
# Tree with depth 2
alias tree2='python ~/projects/git/day4/Directory\ Tree\ Explorer/dir_explorer.py show . --depth 2'

# Tree with common ignores
alias treec='python ~/projects/git/day4/Directory\ Tree\ Explorer/dir_explorer.py show . --ignore .git node_modules __pycache__ build dist'

# Quick stats
alias treestat='python ~/projects/git/day4/Directory\ Tree\ Explorer/dir_explorer.py stats .'
```

Then use:
```bash
tree2           # Show 2 levels
treec           # Show with common ignores
treestat        # Quick statistics
```

### Integration with Other Tools

**Pipe to grep:**
```bash
python dir_explorer.py show . | grep ".py$"
```

**Pipe to less for large outputs:**
```bash
python dir_explorer.py show /large/directory | less
```

**Count files by type:**
```bash
python dir_explorer.py show . | grep ".py$" | wc -l
```

## Comparison with Other Tools

| Feature | dir_explorer.py | Unix `tree` | `ls -R` |
|---------|----------------|-------------|---------|
| ASCII Art | ✅ | ✅ | ❌ |
| Statistics | ✅ | Limited | ❌ |
| Depth Limit | ✅ | ✅ | ❌ |
| Ignore Patterns | ✅ | ✅ | ❌ |
| Cross-Platform | ✅ | Unix only | Unix only |
| No Dependencies | ✅ | ❌ | ✅ |
| Size Info | ✅ | Limited | ✅ |

**Advantages:**
- Works on any platform with Python
- No installation needed (pure Python)
- Customizable ignore patterns
- Detailed statistics mode
- Learning resource (readable code)

**When to use `tree` instead:**
- Already installed on your system
- Need color output
- Want file permissions
- Require advanced filtering

## Related Resources

### Day 4 Learning Materials
- `learn_recursion.py` - Interactive recursion tutorial
- `bst.py` - Binary Search Tree implementation
- `PROJECT2_PLAN.md` - Architecture overview
- `STEP2_GUIDE.md` - Recursive scanning explained
- `STEP3_GUIDE.md` - ASCII visualization guide
- `STEP4_GUIDE.md` - CLI interface guide

### Further Learning
- **Recursion Patterns:** See `learn_recursion.py` lessons
- **Tree Traversal:** Compare with `bst.py` traversals
- **File System APIs:** Python `os` module documentation
- **CLI Design:** Python `argparse` documentation

## Contributing Ideas

Want to extend this tool? Here are some ideas:

1. **File Type Filtering**
   - `--type .py` to show only Python files
   - `--type .js,.ts` for multiple types

2. **Search Functionality**
   - `--search pattern` to find files matching pattern
   - Highlight matches in output

3. **Color Output**
   - Directories in blue
   - Files in default color
   - Large files in red

4. **Export Formats**
   - `--format json` for JSON output
   - `--format html` for HTML report

5. **File Metadata**
   - Show modification dates
   - Show file permissions
   - Show file counts per directory

## Support

**Found a bug?** Check these first:
- Ensure Python 3.7+ is installed
- Try with absolute paths
- Check file permissions
- Test with a simple directory first

**Questions about the code?**
- Read the guides in `day4/` folder
- Study the recursion patterns
- Compare with `bst.py` for similar concepts

---

**Built as part of the 30-Day Python Learning Journey**  
**Day 4: Trees, Recursion & File Systems**  
**Project 2 of 2**

Happy exploring! 🌳
