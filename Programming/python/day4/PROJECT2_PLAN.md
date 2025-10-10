# 📁 Project 2: Directory Tree Explorer - Architecture Plan

## 🎯 What We're Building

A command-line tool that recursively scans directories and displays them as a tree structure (like the Unix `tree` command).

**Example Output:**
```
project/
├── src/
│   ├── main.py
│   ├── utils.py
│   └── tests/
│       └── test_main.py
├── README.md
└── setup.py
```

---

## 🏗️ Architecture Overview

### **3 Main Components:**

1. **DirectoryNode Class** - Represents a file/folder in the tree
2. **DirectoryExplorer Class** - Scans directories and builds the tree
3. **CLI Interface** - argparse-based commands for user interaction

---

## 📦 Component 1: DirectoryNode Class

**Purpose:** Represent a single file or directory in our tree structure.

**Attributes:**
```python
class DirectoryNode:
    name: str           # File/folder name (e.g., "main.py")
    path: str           # Full path (e.g., "/home/user/project/main.py")
    is_directory: bool  # True if folder, False if file
    size: int           # File size in bytes (0 for directories)
    children: list      # List of child DirectoryNode objects (empty for files)
```

**Why we need it:**
- Similar to TreeNode in BST, but for the file system
- Each directory can have multiple children (not just 2 like BST)
- Stores metadata (size, type) unlike BST which just stored values

**Methods:**
- `__init__()` - Initialize with name, path, is_directory
- `add_child()` - Add a child node (for directories)
- `get_size()` - Recursive: sum of all children sizes

---

## 🔍 Component 2: DirectoryExplorer Class

**Purpose:** Main engine that scans directories and provides operations.

### **Core Methods:**

#### 1. **`scan_directory(path, max_depth)`**
**What it does:** Recursively scans a directory and builds the tree

**Algorithm:**
```
1. Create DirectoryNode for current path
2. If current depth > max_depth, return node (stop recursion)
3. If path is a file, return node (base case)
4. If path is a directory:
   a. Use os.listdir() to get all items in directory
   b. For each item:
      - Get full path (os.path.join)
      - Recursively call scan_directory()
      - Add result as child
   c. Return node with all children
```

**Recursion pattern:**
- Base case 1: Reached max depth
- Base case 2: Found a file (no children)
- Recursive case: Directory with children to scan

**Key concepts:**
- Uses `os.listdir()` to get directory contents
- Uses `os.path.join()` to build full paths
- Uses `os.path.isdir()` to check if directory or file
- Uses `os.path.getsize()` to get file size

---

#### 2. **`display_tree(node, prefix, is_last)`**
**What it does:** Print the tree with ASCII art (like our BST display)

**ASCII Characters:**
- `├──` for middle children
- `└──` for last child
- `│  ` for vertical line continuation
- `   ` for spacing

**Algorithm:**
```
1. Print current node with proper prefix
2. For each child (except last):
   - Recurse with "├──" prefix
   - Add "│  " to prefix for continuation
3. For last child:
   - Recurse with "└──" prefix
   - Add "   " to prefix (no line continuation)
```

**Why recursive?**
Each subdirectory is itself a tree, so we recursively display it!

---

#### 3. **`calculate_statistics(node)`**
**What it does:** Gather info about the directory tree

**Statistics to collect:**
- Total files count
- Total directories count
- Total size (in bytes, KB, MB)
- File type distribution (e.g., 10 .py files, 3 .txt files)
- Largest files (top 5)

**Algorithm:**
```
1. Initialize counters (files=0, dirs=0, size=0, types={})
2. If node is file:
   - Increment file count
   - Add size
   - Track extension (.py, .txt, etc.)
3. If node is directory:
   - Increment directory count
   - Recursively process all children
   - Sum up their statistics
4. Return statistics dictionary
```

---

#### 4. **`search_files(node, pattern)`**
**What it does:** Find files matching a pattern (e.g., "*.py")

**Algorithm:**
```
1. Create results list
2. If node matches pattern, add to results
3. If node is directory:
   - Recursively search all children
   - Combine all results
4. Return results list
```

**Pattern matching:**
- Use `fnmatch` module for wildcard matching
- Examples: "*.py", "test_*", "*config*"

---

## 🖥️ Component 3: CLI Interface

**Purpose:** User-friendly command-line interface using argparse

### **Commands to implement:**

#### Command 1: `show`
**Usage:** `python dir_explorer.py show /path/to/dir --depth 3`

**What it does:** Display directory tree

**Arguments:**
- `path` (required) - Directory to scan
- `--depth` (optional) - Max depth to scan (default: unlimited)
- `--ignore` (optional) - Patterns to ignore (.git, __pycache__, etc.)

---

#### Command 2: `stats`
**Usage:** `python dir_explorer.py stats /path/to/dir`

**What it does:** Show statistics about directory

**Output:**
```
📊 Directory Statistics for: /path/to/dir
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Files:          127
Directories:    23
Total Size:     2.4 MB

File Types:
  .py:    45 files
  .txt:   12 files
  .md:    8 files
  .json:  5 files

Top 5 Largest Files:
  1. data.json     (450 KB)
  2. model.pkl     (320 KB)
  3. image.png     (180 KB)
  ...
```

---

#### Command 3: `search`
**Usage:** `python dir_explorer.py search /path/to/dir --pattern "*.py"`

**What it does:** Find files matching pattern

**Output:**
```
🔍 Found 45 files matching "*.py":

  ./src/main.py
  ./src/utils.py
  ./src/config.py
  ./tests/test_main.py
  ...
```

---

## 🧩 How It All Fits Together

### **Data Flow:**

```
User runs command
    ↓
CLI parses arguments (argparse)
    ↓
Create DirectoryExplorer instance
    ↓
Call scan_directory() → Builds DirectoryNode tree recursively
    ↓
Call display_tree() / calculate_statistics() / search_files()
    ↓
Format and print results
```

### **File Structure:**

```python
# dir_explorer.py structure:

1. Imports (os, argparse, fnmatch, etc.)

2. DirectoryNode class
   - __init__
   - add_child
   - get_size

3. DirectoryExplorer class
   - scan_directory (recursive)
   - display_tree (recursive)
   - calculate_statistics (recursive)
   - search_files (recursive)
   - Helper methods (format_size, etc.)

4. CLI Functions
   - cmd_show()
   - cmd_stats()
   - cmd_search()

5. Main function
   - Setup argparse
   - Create subcommands
   - Call appropriate function

6. if __name__ == "__main__": main()
```

---

## 🎓 Key Concepts You'll Practice

### **Recursion Patterns:**

1. **Tree Building** (scan_directory):
   ```python
   def scan(path):
       node = create_node(path)
       if is_directory:
           for child_path in list_directory:
               child_node = scan(child_path)  # Recursive!
               node.add_child(child_node)
       return node
   ```

2. **Tree Traversal** (display_tree):
   ```python
   def display(node, prefix):
       print(prefix + node.name)
       for child in node.children:
           display(child, prefix + "  ")  # Recursive!
   ```

3. **Aggregation** (calculate_statistics):
   ```python
   def stats(node):
       if is_file:
           return {files: 1, size: node.size}
       
       # Combine results from all children
       total = {files: 0, size: 0}
       for child in node.children:
           child_stats = stats(child)  # Recursive!
           total.files += child_stats.files
           total.size += child_stats.size
       return total
   ```

4. **Search** (search_files):
   ```python
   def search(node, pattern):
       results = []
       if matches(node, pattern):
           results.append(node)
       
       for child in node.children:
           child_results = search(child, pattern)  # Recursive!
           results.extend(child_results)
       
       return results
   ```

---

## 🔨 Implementation Order

### **Phase 1: Core Structure (30 min)**
1. Create DirectoryNode class
2. Implement basic scan_directory() without recursion (just one level)
3. Test with simple directory

### **Phase 2: Recursive Scanning (20 min)**
4. Add recursion to scan_directory()
5. Add depth limiting
6. Test with nested directories

### **Phase 3: Visualization (20 min)**
7. Implement display_tree() with ASCII art
8. Handle edge cases (empty dirs, single files)
9. Test with real directory structure

### **Phase 4: Statistics (30 min)**
10. Implement calculate_statistics()
11. Add file type tracking
12. Add size formatting (KB, MB, GB)
13. Find largest files

### **Phase 5: Search (15 min)**
14. Implement search_files()
15. Add pattern matching with fnmatch
16. Format search results

### **Phase 6: CLI (20 min)**
17. Set up argparse with subcommands
18. Implement cmd_show()
19. Implement cmd_stats()
20. Implement cmd_search()
21. Add --ignore flag for common patterns

---

## 💡 Real-World Connections

**This tool teaches you to:**
- Navigate file systems (critical for DevOps)
- Build CLI tools (like Docker, git, aws)
- Process hierarchical data (like AWS S3 buckets, CloudFormation resources)
- Aggregate statistics (like disk usage analyzers)
- Implement search (like `find` command)

**Similar to:**
- `tree` command in Unix
- `du` (disk usage) command
- `find` command
- VS Code's file explorer
- Docker's layer visualization

---

## 🎯 Success Criteria

By the end, you should be able to:
- ✅ Scan any directory recursively
- ✅ Display it as a pretty tree
- ✅ Calculate statistics (files, size, types)
- ✅ Search for files by pattern
- ✅ Limit depth to avoid huge scans
- ✅ Ignore common patterns (.git, __pycache__)
- ✅ Use it as a command-line tool

---

## 🚀 Ready to Build?

Now that you understand the architecture, we'll implement it step by step:

1. **First:** DirectoryNode class (simple data structure)
2. **Second:** Basic scan_directory() - just files/folders, no recursion
3. **Third:** Add recursion to scan_directory()
4. **Fourth:** display_tree() with ASCII art
5. **Fifth:** calculate_statistics() with aggregation
6. **Sixth:** search_files() with pattern matching
7. **Finally:** CLI interface with argparse

Each step builds on the previous one, and you'll test as you go!

**Let's start with DirectoryNode! 🌳**
