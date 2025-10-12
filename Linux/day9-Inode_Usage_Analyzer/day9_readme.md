# Day 9: Filesystems & Disks In-Depth

## 🎯 Goal
Understand the Linux Filesystem Hierarchy Standard (FHS), inodes, links, and disk management concepts by building an Inode Usage Analyzer script.

---

## 📚 Key Concepts Learned

### 1. **Filesystem Hierarchy Standard (FHS)**
Understanding the standard Linux directory structure:
- `/` - Root directory
- `/home` - User home directories
- `/etc` - System configuration files
- `/var` - Variable data (logs, databases)
- `/tmp` - Temporary files
- `/usr` - User programs and data
- `/bin` - Essential command binaries
- `/dev` - Device files

### 2. **Inodes**
An inode is a data structure that stores metadata about a file:
- File type (regular file, directory, symlink)
- Permissions
- Owner (UID) and Group (GID)
- File size
- Timestamps (creation, modification, access)
- Number of hard links
- Pointers to data blocks

**Key Commands:**
```bash
# View inode information
ls -i filename          # Show inode number
stat filename           # Detailed inode info
df -i                   # Show inode usage per filesystem
```

**Important:** You can run out of inodes even if you have disk space left! This happens with many small files.

### 3. **Symbolic vs Hard Links**

**Hard Links:**
- Multiple directory entries pointing to the same inode
- Cannot cross filesystem boundaries
- Cannot link to directories (usually)
```bash
ln original.txt hardlink.txt
```

**Symbolic (Soft) Links:**
- A special file containing the path to another file
- Can cross filesystems
- Can link to directories
- Breaks if original is deleted
```bash
ln -s original.txt symlink.txt
```

### 4. **Disk Partitioning Concepts**

**Tools:**
- `fdisk` - Partition table manipulator
- `lsblk` - List block devices
- `df` - Disk free space
- `du` - Disk usage

**Viewing partitions:**
```bash
lsblk                    # Tree view of block devices
fdisk -l                 # List all partitions
df -h                    # Human-readable disk usage
```

### 5. **LVM (Logical Volume Manager) Basics**

LVM provides flexible disk management:
- **Physical Volume (PV)**: Actual disk or partition
- **Volume Group (VG)**: Pool of PVs
- **Logical Volume (LV)**: Virtual partition from VG

**Benefits:** Easy resizing, snapshots, spanning multiple disks

---

## 🛠️ Project: Inode Usage Analyzer

**File:** `analyze_inodes.sh`

### Features Implemented
✅ Argument validation (requires 1 directory path)  
✅ Directory existence verification  
✅ Recursive directory traversal using `find`  
✅ File counting per subdirectory  
✅ Sorted output (highest to lowest)  
✅ Clear report formatting  
✅ Error messages to stderr  

### Usage
```bash
./analyze_inodes.sh <directory_path>
```

### Examples
```bash
# Analyze your home directory
./analyze_inodes.sh /home/username

# Analyze system directories (may need sudo)
sudo ./analyze_inodes.sh /var

# Analyze current directory
./analyze_inodes.sh .
```

### Output Format
```
Inode Usage Report for '/home/user'
-----------------------------------
250 files in /home/user/Documents
180 files in /home/user/.cache
95 files in /home/user/Downloads
42 files in /home/user/Pictures
...
```

---

## 📝 Code Analysis

### Script Structure

**1. Argument Validation**
```bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 <filesystem> (e.g., /dev/sda1 or /home)" >&2
    exit 1
fi
```
- Checks for exactly one argument
- Provides usage example
- Exits with code 1 if incorrect

**2. Directory Validation**
```bash
if [ ! -d "$DIR_PATH" ]; then
    echo "Error: '$DIR_PATH' is not a valid directory." >&2
    exit 1
fi
```
- Tests if path is a valid directory
- Clear error message if not
- Prevents processing invalid paths

**3. Report Header**
```bash
echo "Inode Usage Report for '$DIR_PATH'"
echo "-----------------------------------"
```
- Visual separation for readability
- Shows which directory is being analyzed

**4. Find and Count Files**
```bash
find "$DIR_PATH" -mindepth 1 -type d | while read -r subdir; do
    count=$(find "$subdir" -maxdepth 1 -type f | wc -l)
    echo "$count files in $subdir"
done | sort -nr
```

**Breaking it down:**
- `find "$DIR_PATH" -mindepth 1 -type d`: Find all subdirectories (skip the root)
  - `-mindepth 1`: Don't include the starting directory itself
  - `-type d`: Only directories
- `while read -r subdir`: Loop through each directory found
  - `-r`: Prevent backslash interpretation
- `find "$subdir" -maxdepth 1 -type f`: Count files in this specific directory
  - `-maxdepth 1`: Don't recurse into subdirectories
  - `-type f`: Only regular files
- `wc -l`: Count the lines (number of files)
- `sort -nr`: Sort numerically in reverse (highest first)
  - `-n`: Numeric sort
  - `-r`: Reverse order

---

## 🧪 Testing

### Test Cases Performed

```bash
# 1. Test with missing argument
./analyze_inodes.sh
# Expected: Usage message + exit 1

# 2. Test with invalid directory
./analyze_inodes.sh /nonexistent/path
# Expected: Error message + exit 1

# 3. Test with valid directory
./analyze_inodes.sh ~/Documents
# Expected: Sorted list of subdirectories with file counts

# 4. Test with current directory
./analyze_inodes.sh .
# Expected: Analysis of current directory

# 5. Test with system directory (requires sudo)
sudo ./analyze_inodes.sh /var/log
# Expected: Analysis of log directories

# 6. Verify sorting order
./analyze_inodes.sh ~/test_dir
# Expected: Highest count first, lowest last
```

### Creating Test Data
```bash
# Create test directory structure
mkdir -p ~/inode_test/{dir1,dir2,dir3}
touch ~/inode_test/dir1/file{1..100}.txt
touch ~/inode_test/dir2/file{1..50}.txt
touch ~/inode_test/dir3/file{1..10}.txt

# Run analyzer
./analyze_inodes.sh ~/inode_test

# Expected output (sorted):
# 100 files in /home/user/inode_test/dir1
# 50 files in /home/user/inode_test/dir2
# 10 files in /home/user/inode_test/dir3
```

---

## 📊 Skills Demonstrated

| Skill | Implementation |
|-------|----------------|
| **Argument validation** | Single argument check with usage message |
| **Directory testing** | `-d` test operator |
| **Find command** | Recursive directory traversal |
| **Pipes** | Chaining commands with `\|` |
| **While loops** | Reading find output line by line |
| **Subshells** | `$()` for command substitution |
| **Sorting** | `sort -nr` for numerical reverse sort |
| **File counting** | `wc -l` for line counting |
| **Error handling** | stderr redirection with `>&2` |

---

## 🔧 Commands & Tools Used

### Find Command Options
```bash
-mindepth N    # Descend at least N levels
-maxdepth N    # Descend at most N levels
-type d        # Match only directories
-type f        # Match only regular files
-name pattern  # Match filename pattern
```

### Useful Inode Commands
```bash
# Check inode usage
df -i

# Find files by inode number
find / -inum 12345

# Show inode information
stat filename

# List with inode numbers
ls -i
```

---

## 💡 Best Practices Applied

✅ **Shebang line**: `#!/usr/bin/bash` (bash-specific features)  
✅ **Argument validation**: Check before processing  
✅ **Meaningful variable names**: `DIR_PATH` instead of `$1`  
✅ **Error messages to stderr**: Using `>&2`  
✅ **Proper quoting**: `"$variable"` to handle spaces  
✅ **Clear output formatting**: Headers and separators  
✅ **Sorted results**: Most useful information first  
✅ **Comments**: Explain each section  

---

## 🚀 Potential Enhancements

Future versions could add:

1. **Threshold alerts**: Warn when directories exceed a certain file count
2. **Multiple directory support**: Analyze several paths at once
3. **Depth control**: `-d` flag to control recursion depth
4. **Output formats**: JSON, CSV, or table output
5. **Color coding**: Highlight high-usage directories
6. **Size reporting**: Show disk space alongside file counts
7. **Exclude patterns**: Skip certain directories (like `.git`)
8. **Total summary**: Show overall statistics
9. **Compare mode**: Compare two directories
10. **Export to file**: Save report to a file

---

## 🎓 Real-World Use Cases

### When to Use This Script

1. **Troubleshooting "No space left on device" errors** when `df` shows free space
   - You've run out of inodes, not disk space!
   
2. **Identifying directories with too many small files**
   - Email spools, cache directories, log files
   
3. **System cleanup planning**
   - Find which directories to target for cleanup
   
4. **Backup planning**
   - Understand which directories have the most files
   
5. **Application monitoring**
   - Watch for applications creating excessive files

### Example Scenario
```bash
# Server showing errors but disk seems fine
df -h
# Output: 45% used - plenty of space!

df -i
# Output: 100% inodes used - problem found!

# Find the culprit
sudo ./analyze_inodes.sh /var
# Output shows: 500,000 files in /var/spool/mail

# Solution: Clean up old mail or restructure storage
```

---

## 📁 File Location

```
cloud-engineer-plan/
└── linux/
    └── scripts/
        └── day9-inode_analyzer/
            ├── analyze_inodes.sh
            └── README.md (this file)
```

---

## ✅ Day 9 Completion Checklist

- [x] Understand the Filesystem Hierarchy Standard (FHS)
- [x] Learn what inodes are and why they matter
- [x] Differentiate between hard links and symbolic links
- [x] Use `find` command with various options
- [x] Implement directory traversal with `while read`
- [x] Count files using `wc -l`
- [x] Sort output with `sort -nr`
- [x] Create a practical system administration tool
- [x] Test with multiple directory types
- [x] Document the script thoroughly

---

## 🎓 Key Takeaways

1. **Inodes are limited resources** - You can run out even with free disk space
2. **The `find` command is powerful** - Master its options for system administration
3. **Pipes are essential** - Chain commands to build complex functionality
4. **Sorting improves usability** - Present data in useful order
5. **System administration requires understanding filesystem internals**
6. **Small files can cause big problems** - Monitor inode usage on production systems

---

## 📖 Resources Referenced

- `man find` - Find command manual
- `man df` - Disk free manual (check `-i` option)
- `man stat` - File statistics
- `man ln` - Link command (hard vs symbolic)
- [Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)

---

## 🔗 Related Concepts

- **Disk quotas**: Limiting user disk/inode usage
- **Filesystem types**: ext4, xfs, btrfs (different inode handling)
- **LVM**: Logical volume management for flexible storage
- **RAID**: Redundant storage configurations
- **Mount points**: Understanding filesystem boundaries

---

**Status:** ✅ Day 9 Complete  
**Previous:** Day 8 - Professional Backup Script  
**Next:** Day 10 - Process Management & systemd  
**Time Spent:** ~4 hours (learning + implementation + testing)

---

*Understanding filesystems and inodes is crucial for system administration. This script provides practical experience with a common real-world problem: running out of inodes on production servers.*
