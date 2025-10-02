# 🔄 Command History Manager - Usage Guide

A professional command-line tool for tracking, searching, and managing your command history with undo/redo support.

## 📦 Quick Start

```bash
# Navigate to day3 directory
cd /home/kot/projects/git/day3

# Add commands as you execute them
python3 command_history.py add "git status" -e 0
python3 command_history.py add "make build" -e 127

# View your history
python3 command_history.py list
```

---

## 🎯 Available Commands

### ➕ Add Command
Track a command you just executed:

```bash
# Successful command (exit code 0)
python3 command_history.py add "git status" -e 0

# Failed command (exit code 127)
python3 command_history.py add "make build" -e 127

# With custom history file
python3 command_history.py add "ls -la" -e 0 -f my_history.json
```

### 📜 List Commands
View your command history:

```bash
# Show all commands (most recent first)
python3 command_history.py list

# Show last 10 commands
python3 command_history.py list -n 10

# Use custom history file
python3 command_history.py list -f my_history.json
```

### 🔍 Search Commands
Find commands by substring:

```bash
# Search for 'git' commands
python3 command_history.py search git

# Search for 'python' commands
python3 command_history.py search python

# Case-insensitive search
python3 command_history.py search GIT  # finds 'git status', 'git commit', etc.
```

### ↩️ Undo Command
Remove the last command from history:

```bash
# Undo last command
python3 command_history.py undo

# The command is moved to undo stack (can be redone!)
```

### ↪️ Redo Command
Restore an undone command:

```bash
# Redo the last undone command
python3 command_history.py redo

# Note: Adding a new command clears the redo stack
```

### 📊 Statistics
View statistics about your command history:

```bash
python3 command_history.py stats
```

**Output:**
```
📊 Command History Statistics:
================================================================================
  Total commands:       42
  Executed:             42
  Not executed:         0
  Most common command:  git status
  Occurrences:          12
  Time span:            3.45 hours
```

### 💾 Save/Load
Backup and restore your history:

```bash
# Save current history to a backup file
python3 command_history.py save backup_$(date +%Y%m%d).json

# Load history from a file
python3 command_history.py load backup_20251002.json
```

---

## 🚀 Real-World Usage

### 1. Track Your Daily Commands

Add this to your `.bashrc` or `.zshrc`:

```bash
# Function to automatically track commands
track_cmd() {
    local exit_code=$?
    local last_cmd=$(history 1 | sed 's/^[ ]*[0-9]*[ ]*//')
    python3 /home/kot/projects/git/day3/command_history.py add "$last_cmd" -e $exit_code 2>/dev/null
}

# Call after each command (optional - can be noisy)
# PROMPT_COMMAND="track_cmd"
```

### 2. Manual Tracking Workflow

```bash
# Execute a command
git push origin main

# Track it
python3 command_history.py add "git push origin main" -e $?

# Or combine them
git push origin main && python3 command_history.py add "git push origin main" -e 0
```

### 3. Debug Failed Commands

```bash
# Track a failed command
make build
python3 command_history.py add "make build" -e $?

# Later, search for failed commands
python3 command_history.py list | grep "✗"
```

### 4. Project-Specific History

```bash
# Keep separate history per project
cd /home/kot/projects/my-app
python3 /path/to/command_history.py add "npm test" -e 0 -f .command_history.json

# View project-specific history
python3 /path/to/command_history.py list -f .command_history.json
```

### 5. Daily Backup

```bash
# Add to cron or systemd timer
0 23 * * * python3 /home/kot/projects/git/day3/command_history.py save ~/backups/commands_$(date +\%Y\%m\%d).json
```

---

## 🎨 Status Icons

- `[✓ 0]` - Successful command (exit code 0)
- `[✗ 127]` - Failed command (with exit code)
- `[○ -]` - Not executed yet (pending)

---

## 📂 File Storage

**Default file:** `command_history.json` (in current directory)

**Format:** JSON with structure:
```json
{
  "history": [
    {
      "command": "git status",
      "timestamp": "2025-10-02T08:16:18.123456",
      "executed": true,
      "exit_code": 0
    }
  ],
  "undo_stack": [],
  "max_size": 1000
}
```

---

## 🔧 Advanced Tips

### Alias for Quick Access

Add to `.bashrc`:
```bash
alias ch='python3 /home/kot/projects/git/day3/command_history.py'

# Now you can use:
ch add "git status" -e 0
ch list
ch search git
ch stats
```

### Search with Grep

```bash
# Find all git commands
python3 command_history.py list | grep git

# Find failed commands
python3 command_history.py list | grep "✗"

# Count total commands
python3 command_history.py list | wc -l
```

### Export to Shell History

```bash
# Extract just the commands (for bash history format)
python3 command_history.py list | awk -F'| ' '{print $2}' > exported_history.txt
```

---

## 🎯 Use Cases

1. **Debugging** - Track which commands failed and when
2. **Audit Trail** - Keep record of system administration tasks
3. **Learning** - Review commands you've used to remember syntax
4. **Automation** - Extract common commands to create scripts
5. **Documentation** - Generate command lists for documentation
6. **Team Sharing** - Share command sequences with team members

---

## 🤝 Integration Ideas

### Git Pre-commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit
python3 /path/to/command_history.py add "git commit" -e 0 -f .git_history.json
```

### Make Target
```makefile
.PHONY: track
track:
	@python3 /path/to/command_history.py add "make $(MAKECMDGOALS)" -e $? -f .make_history.json
```

### Systemd Service (Monitor specific commands)
```ini
[Unit]
Description=Command History Tracker

[Service]
ExecStart=/usr/bin/python3 /path/to/command_history.py add "%I" -e 0

[Install]
WantedBy=multi-user.target
```

---

## 🎓 What You Learned

- **Stack (LIFO)** - History stored in last-in-first-out order
- **Two-stack pattern** - Undo/redo using separate stacks
- **CLI design** - `argparse` for professional command-line interfaces
- **Data persistence** - JSON serialization with datetime handling
- **Error handling** - Exit codes for success/failure tracking

---

## 🚀 Next Steps

1. **Add bash integration** - Auto-track all commands
2. **Add filtering** - Filter by date, exit code, etc.
3. **Add export formats** - Export to CSV, Markdown, HTML
4. **Add tagging** - Tag commands by project/category
5. **Add analytics** - Command frequency graphs, time analysis

---

**Made with Stack (LIFO) data structure! 🔄**
