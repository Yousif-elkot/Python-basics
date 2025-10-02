# 📋 Command History Manager - Quick Reference

## 🚀 One-Line Examples

```bash
# Add commands
python3 command_history.py add "git status" -e 0
python3 command_history.py add "make build" -e 127

# View
python3 command_history.py list
python3 command_history.py list -n 10

# Search
python3 command_history.py search git

# Undo/Redo
python3 command_history.py undo
python3 command_history.py redo

# Stats
python3 command_history.py stats

# Save/Load
python3 command_history.py save backup.json
python3 command_history.py load backup.json
```

## ⚡ With Aliases (after running setup_aliases.sh)

```bash
# Shorter commands
ch-add "git status" -e 0
ch-list
ch-search git
ch-undo
ch-redo
ch-stats

# Track last command
git status
ch-t  # Tracks "git status" with its exit code
```

## 🎯 Common Workflows

**Track as you work:**
```bash
git status && ch-t
make build || ch-t
npm test && ch-t
```

**Review your day:**
```bash
ch-list              # All commands
ch-stats             # Statistics
ch-search git        # Find git commands
```

**Fix mistakes:**
```bash
ch-undo              # Remove wrong entry
ch-list              # Verify
ch-redo              # Restore if needed
```

## 📁 File Locations

- Default: `command_history.json` (current directory)
- Custom: Use `-f filename.json` flag
- Example: `ch-list -f ~/work_history.json`

## 🎨 Status Symbols

- `[✓ 0]` = Success
- `[✗ 127]` = Failed
- `[○ -]` = Not executed

## 🔧 Setup (One-Time)

```bash
cd /home/kot/projects/git/day3
./setup_aliases.sh
source ~/.bashrc  # or ~/.zshrc
```

## 💡 Pro Tips

1. **Separate histories per project**: Use `-f .history.json` in each project
2. **Daily backups**: `ch save ~/backups/cmd_$(date +%Y%m%d).json`
3. **Search tips**: Search is case-insensitive substring match
4. **Undo/Redo**: Adding new command clears redo stack
5. **Max size**: Default 1000 commands, oldest auto-removed

---

**See COMMAND_HISTORY_USAGE.md for detailed documentation**
