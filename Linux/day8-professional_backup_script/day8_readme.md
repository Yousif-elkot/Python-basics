# Day 8: The Shell & Advanced Scripting

## 🎯 Goal
Transform a basic backup script into a professional-grade tool using functions, command-line options, error handling, and logging.

---

## 📚 Key Concepts Learned

### 1. **Bash Functions**
Functions organize code into reusable blocks:
```bash
function_name() {
    local variable="value"  # Local to function
    echo "$1"  # First argument
}
```

### 2. **Command-Line Options (getopts)**
Parse flags like `-s`, `-d`, `-v`:
```bash
while getopts "s:d:vh" opt; do
    case $opt in
        s) SOURCE="$OPTARG";;
        v) VERBOSE=true;;
    esac
done
```

### 3. **Error Handling**
```bash
set -euo pipefail  # Strict mode
error_exit() {
    echo "ERROR: $1" >&2
    exit "${2:-1}"
}
```

### 4. **Logging**
```bash
log_message() {
    echo "[$TIMESTAMP] $1" | tee -a "$LOG_FILE"
}
```

---

## 🛠️ Project: Professional Backup Script

**File:** `professional_backup.sh`

### Features Implemented
✅ Argument validation (checks for 2 required arguments)  
✅ Directory existence verification  
✅ Automatic destination directory creation  
✅ Timestamped backup files  
✅ Tar archive creation with compression  
✅ Success/failure reporting  
✅ Proper exit codes  
✅ Error messages to stderr  

### Usage
```bash
./professional_backup.sh <source_directory> <backup_directory>
```

### Example
```bash
./professional_backup.sh ~/Documents /tmp/backups
```

### Script Flow
```
[Parse Args] → [Validate Source] → [Check/Create Dest] → [Create Backup] → [Verify] → [Report]
```

### Error Handling
- Exit code 1: Wrong number of arguments
- Exit code 1: Source directory doesn't exist
- Exit code 1: Backup creation failed

---

## 📝 Code Analysis

### Key Sections

**1. Argument Validation**
```bash
if [ $# -ne 2 ]; then
    echo "Usage: $0 <source_directory> <backup_directory>" >&2
    exit 1
fi
```

**2. Directory Checks**
```bash
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Source directory '$SOURCE_DIR' does not exist." >&2
    exit 1
fi
```

**3. Timestamp Generation**
```bash
TIMESTAMP=$(date +"%Y-%m-%d-%H-%M-%S")
FILENAME="backup-$TIMESTAMP.tar.gz"
```

**4. Tar Command**
```bash
tar -czvf "$DEST_DIR/$FILENAME" "$SOURCE_DIR"
```
- `-c`: Create archive
- `-z`: Compress with gzip
- `-v`: Verbose output
- `-f`: Specify filename

**5. Exit Code Checking**
```bash
if [ $? -eq 0 ]; then
    echo "Backup completed successfully."
else
    echo "Backup failed. Please check for errors." >&2
    exit 1
fi
```

---

## 🧪 Testing

### Test Cases Performed
```bash
# 1. Test with missing arguments
./professional_backup.sh
# Expected: Usage message + exit 1

# 2. Test with non-existent source
./professional_backup.sh /fake/path /tmp/backup
# Expected: Error message + exit 1

# 3. Test successful backup
./professional_backup.sh ~/test_dir /tmp/backups
# Expected: Creates backup-YYYY-MM-DD-HH-MM-SS.tar.gz

# 4. Test with non-existent destination
./professional_backup.sh ~/test_dir /tmp/new_backup_dir
# Expected: Creates directory + backup

# 5. Verify backup integrity
tar -tzf /tmp/backups/backup-*.tar.gz
# Expected: Lists all files in archive
```

---

## 📊 Skills Demonstrated

| Skill | Implementation |
|-------|----------------|
| **Argument handling** | `$1`, `$2`, `$#` validation |
| **Error messages** | Redirected to stderr with `>&2` |
| **Conditional logic** | `if [ condition ]; then` |
| **Directory operations** | `-d` test, `mkdir -p` |
| **Date formatting** | `date +"%Y-%m-%d-%H-%M-%S"` |
| **Command execution** | `tar` with error checking |
| **Exit codes** | Proper use of `exit 0` and `exit 1` |
| **Variable quoting** | `"$VARIABLE"` to prevent word splitting |

---

## 🔧 Tools Used

- **bash**: Shell interpreter
- **tar**: Archive creation
- **date**: Timestamp generation
- **mkdir**: Directory creation
- **shellcheck**: (recommended) Script linting

---

## 💡 Best Practices Applied

✅ **Shebang line**: `#!/bin/bash`  
✅ **Comments**: Explain each section  
✅ **Variable quoting**: Prevent word splitting  
✅ **Error output to stderr**: `>&2`  
✅ **Meaningful exit codes**: 0 for success, 1 for errors  
✅ **Input validation**: Check before processing  
✅ **User feedback**: Clear status messages  

---

## 🚀 Potential Enhancements (Future Iterations)

These features could be added in advanced versions:

1. **Functions**: Organize code into reusable blocks
2. **Getopts**: Named flags like `-s source -d dest -v`
3. **Logging**: Write to log file
4. **Backup rotation**: Keep only N newest backups
5. **Integrity verification**: `tar -t` to test archive
6. **Verbose mode**: Optional detailed output
7. **Compression options**: Choose gzip, bzip2, xz
8. **Exclude patterns**: Skip certain files/folders
9. **Email notifications**: Send results via email
10. **Remote backups**: SCP/rsync to remote server

---

## 📁 File Location

```
cloud-engineer-plan/
└── linux/
    └── scripts/
        └── day8-professional_backup_script/
            ├── professional_backup.sh
            └── README.md (this file)
```

---

## ✅ Day 8 Completion Checklist

- [x] Understand bash script structure
- [x] Implement argument validation
- [x] Handle directory operations
- [x] Create timestamped backups
- [x] Use tar for compression
- [x] Check command exit codes
- [x] Provide user feedback
- [x] Write error messages to stderr
- [x] Test multiple scenarios
- [x] Document the script

---

## 🎓 Key Takeaways

1. **Always validate inputs** before processing
2. **Check command success** with `$?` or `if command; then`
3. **Use meaningful variable names** (SOURCE_DIR vs $1)
4. **Provide clear error messages** to help users
5. **Quote variables** to prevent issues with spaces
6. **Exit with appropriate codes** for automation/scripting
7. **Test edge cases** (missing dirs, wrong args, etc.)

---

## 📖 Resources Referenced

- Bash manual: `man bash`
- Tar documentation: `man tar`
- Date formatting: `man date`
- File test operators: `help test`

---

**Status:** ✅ Day 8 Complete  
**Next:** Day 9 - Filesystems & Disks In-Depth (Inode Usage Analyzer)  
**Time Spent:** ~4 hours (learning + implementation + testing)

---

*This script serves as the foundation for understanding professional bash scripting practices. The concepts learned here will be expanded in future days with functions, advanced error handling, and more complex automation tasks.*
