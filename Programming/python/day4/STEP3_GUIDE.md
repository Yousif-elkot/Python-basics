# 🎨 Step 3: Display Tree - Beautiful ASCII Visualization

## 🎯 Goal
Display the directory tree with beautiful ASCII art, just like the Unix `tree` command!

---

## 📊 Expected Output

```
day4/
├── bst.py
├── learn_recursion.py
├── PROJECT2_PLAN.md
├── ROADMAP.md
└── Directory Tree Explorer/
    └── dir_explorer.py
```

---

## 🧠 Understanding the Recursion

This is **EXACTLY** like the `display()` method from your BST! Same logic, same ASCII characters.

### **The Pattern:**

```
display_tree(node, prefix="", is_last=True):
  1. Print: prefix + connector + node.name
  2. For each child:
     - Calculate new_prefix (add continuation lines)
     - Recursively display child
```

### **Visual Example:**

```
display_tree(day4/, prefix="", is_last=True):
  Print: "day4/"
  
  Children: [bst.py, learn_recursion.py, Directory Tree Explorer/]
  
  Child 1: bst.py (not last)
    ├── Print: "├── bst.py"
    ├── No children, done
  
  Child 2: learn_recursion.py (not last)
    ├── Print: "├── learn_recursion.py"
    ├── No children, done
  
  Child 3: Directory Tree Explorer/ (IS last)
    ├── Print: "└── Directory Tree Explorer/"
    └── Recursively display its children with new prefix
```

---

## 🎨 ASCII Characters

| Character | When to Use | Example |
|-----------|-------------|---------|
| `└── `    | Last child  | `└── file.txt` |
| `├── `    | Middle child | `├── file.py` |
| `│   `    | Continuation (not last) | Used in prefix |
| `    `    | Spacing (is last) | Used in prefix |

---

## 📝 Method 1: `display_tree()`

### **Parameters:**
- `node` - The DirectoryNode to display (default to root if None)
- `prefix` - String to print before the node name (builds up recursively)
- `is_last` - Is this the last child of its parent?

### **Algorithm:**

```python
def display_tree(self, node=None, prefix="", is_last=True):
    # 1. Print current node
    if prefix == "":  # Root node
        print(node.name + ("/" if node.is_directory else ""))
    else:
        connector = "└── " if is_last else "├── "
        print(prefix + connector + node.name + ("/" if node.is_directory else ""))
    
    # 2. If directory with children, display them
    if node.is_directory and node.children:
        # Sort children for consistent display
        children = sorted(node.children, key=lambda x: x.name)
        
        for i, child in enumerate(children):
            # Is this the last child?
            is_last_child = (i == len(children) - 1)
            
            # Build new prefix for child
            if prefix == "":
                new_prefix = ""
            else:
                new_prefix = prefix + ("    " if is_last else "│   ")
            
            # RECURSION!
            self.display_tree(child, new_prefix, is_last_child)
```

### **Key Points:**

1. **Root node** (prefix == "") has no connector
2. **Last child** uses `└── ` and adds `    ` to prefix
3. **Middle child** uses `├── ` and adds `│   ` to prefix
4. **Directories** get a `/` suffix
5. **Sort children** for consistent, alphabetical display

---

## 📝 Method 2: `format_size()`

Convert bytes to human-readable format.

### **Algorithm:**

```python
def format_size(self, size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} bytes"
    elif size_bytes < 1024 * 1024:
        kb = size_bytes / 1024
        return f"{kb:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        mb = size_bytes / (1024 * 1024)
        return f"{mb:.1f} MB"
    else:
        gb = size_bytes / (1024 * 1024 * 1024)
        return f"{gb:.1f} GB"
```

### **Examples:**
- 500 → "500 bytes"
- 2048 → "2.0 KB"
- 1536000 → "1.5 MB"
- 10737418240 → "10.0 GB"

---

## 🎓 Comparing to BST

### **BST display:**
```python
def _display_recursive(self, node, prefix, is_tail):
    print(prefix + ("└── " if is_tail else "├── ") + str(node.value))
    
    if node.left or node.right:
        if node.left:
            self._display_recursive(node.left, prefix + (...), ...)
        if node.right:
            self._display_recursive(node.right, prefix + (...), True)
```

### **Directory display:**
```python
def display_tree(self, node, prefix, is_last):
    print(prefix + ("└── " if is_last else "├── ") + node.name)
    
    if node.children:
        for i, child in enumerate(node.children):
            is_last_child = (i == len(children) - 1)
            self.display_tree(child, prefix + (...), is_last_child)
```

**The difference?**
- BST: Max 2 children (left, right)
- Directory: ANY number of children (loop through list)

---

## 🐛 Common Pitfalls

### **1. Forgetting the continuation:**
```python
# WRONG: No continuation line
new_prefix = prefix + "    "

# CORRECT: Add continuation for non-last children
new_prefix = prefix + ("    " if is_last else "│   ")
```

### **2. Wrong connector:**
```python
# WRONG: Always uses same connector
connector = "├── "

# CORRECT: Check if last child
connector = "└── " if is_last else "├── "
```

### **3. Not handling root:**
```python
# WRONG: Root gets a connector too
print(prefix + connector + node.name)

# CORRECT: Special case for root (empty prefix)
if prefix == "":
    print(node.name)
else:
    print(prefix + connector + node.name)
```

---

## ✅ Testing Strategy

1. **Test with simple tree** - Few files, one level deep
2. **Test with nested folders** - Multiple levels
3. **Test with many children** - See if connectors work
4. **Test format_size** - Various byte sizes
5. **Compare to Unix `tree` command** - Should look similar!

---

## 🎯 Success Criteria

After implementing, you should see:
- ✅ Beautiful ASCII tree display
- ✅ Proper connectors (├── and └──)
- ✅ Proper continuation lines (│)
- ✅ Directories with `/` suffix
- ✅ Human-readable file sizes
- ✅ Sorted alphabetically

---

## 💡 Bonus Ideas (Optional)

- Add colors (directories in blue, files in white)
- Show file sizes next to names: `file.txt (1.2 KB)`
- Add file type icons: 📁 for folders, 📄 for files
- Limit display to first N files per directory

---

## 🚀 Ready to Code!

Implement the 2 methods:
1. `display_tree()` - The recursive ASCII art display
2. `format_size()` - Convert bytes to KB/MB/GB

Then run the tests to see beautiful tree output! 🌳✨
