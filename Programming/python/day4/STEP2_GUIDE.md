# 📂 Step 2: DirectoryExplorer - scan_directory() Method

## 🎯 Goal
Build a tree of DirectoryNodes by recursively scanning a real directory on your file system.

---

## 🧠 Understanding the Recursion

### **The Big Picture:**
```
scan_directory("/home/user/project"):
  ├─ Creates DirectoryNode for "project"
  ├─ Lists all items in "project" folder
  └─ For EACH item:
      ├─ If it's a file → Create DirectoryNode, return it
      ├─ If it's a folder → Recursively scan it!
      └─ Add the result as a child
```

### **Visual Example:**

```
Initial call: scan_directory("project/", depth=0, max=2)

Step 1: Create node for "project/"
Step 2: List contents: ["src/", "README.md", "main.py"]

Step 3: Process each item:
  
  Item 1: "src/" (directory)
    → Recursive call: scan_directory("project/src/", depth=1, max=2)
      → Create node for "src/"
      → List contents: ["utils.py", "config.py"]
      → Process "utils.py": scan_directory("project/src/utils.py", depth=2, max=2)
          → Is file, return node
      → Process "config.py": scan_directory("project/src/config.py", depth=2, max=2)
          → Is file, return node
      → Return "src/" node with 2 children
    → Add "src/" node as child of "project/"
  
  Item 2: "README.md" (file)
    → Recursive call: scan_directory("project/README.md", depth=1, max=2)
      → Is file, return node
    → Add "README.md" node as child of "project/"
  
  Item 3: "main.py" (file)
    → Recursive call: scan_directory("project/main.py", depth=1, max=2)
      → Is file, return node
    → Add "main.py" node as child of "project/"

Step 4: Return "project/" node with all children attached
```

---

## 🔑 Key Concepts

### **1. Base Cases (When to STOP recursing):**

**Base Case 1: Max Depth Reached**
```python
if max_depth is not None and current_depth >= max_depth:
    return node  # Don't scan deeper!
```
Example: If max_depth=1, we only scan the root and its immediate children.

**Base Case 2: Found a File**
```python
if not os.path.isdir(path):
    return node  # Files have no children
```

**Base Case 3: Permission Denied**
```python
try:
    items = os.listdir(path)
except OSError:
    return node  # Can't read directory, stop here
```

---

### **2. Recursive Case (Scan Directory):**

```python
# For a directory we CAN access:
for item in os.listdir(path):
    # Skip ignored patterns
    if self._should_ignore(item):
        continue
    
    # Build full path
    full_path = os.path.join(path, item)
    
    # RECURSIVE CALL (depth increases by 1)
    child_node = self.scan_directory(full_path, current_depth + 1, max_depth)
    
    # Add result as child
    node.add_child(child_node)
```

---

## 📝 Implementation Steps

### **Method 1: `__init__`**
Simple constructor:
```python
self.ignore_patterns = ignore_patterns or []
```

---

### **Method 2: `_should_ignore`**
Check if a name matches any ignore pattern:
```python
for pattern in self.ignore_patterns:
    if pattern == name:  # Simple exact match
        return True
return False
```

---

### **Method 3: `scan_directory`** (THE BIG ONE!)

**Step-by-step implementation:**

```python
def scan_directory(self, path, current_depth=0, max_depth=None):
    # 1. Get just the folder/file name (not full path)
    name = os.path.basename(path)
    
    # 2. Check if it's a directory
    is_dir = os.path.isdir(path)
    
    # 3. Create the node
    node = DirectoryNode(name, path, is_dir)
    
    # 4. BASE CASE: Max depth reached?
    if max_depth is not None and current_depth >= max_depth:
        return node
    
    # 5. BASE CASE: Is it a file?
    if not is_dir:
        return node
    
    # 6. RECURSIVE CASE: It's a directory we can scan
    try:
        items = os.listdir(path)
    except OSError:
        # Permission denied or doesn't exist
        return node
    
    # 7. Process each item in the directory
    for item in items:
        # Skip ignored patterns
        if self._should_ignore(item):
            continue
        
        # Build full path
        full_path = os.path.join(path, item)
        
        # RECURSION! Scan this item (depth increases)
        child_node = self.scan_directory(
            full_path,
            current_depth + 1,
            max_depth
        )
        
        # Add as child
        node.add_child(child_node)
    
    # 8. Return the node with all children
    return node
```

---

## 🎓 Understanding Parameters

### **`path: str`**
The directory or file to scan.
- Example: `"/home/user/project"` or `"./src"`

### **`current_depth: int = 0`**
How deep we are in the recursion.
- Root directory: depth = 0
- Its children: depth = 1
- Their children: depth = 2
- And so on...

### **`max_depth: Optional[int] = None`**
Maximum depth to scan.
- `None` = unlimited (scan everything)
- `0` = only root, no children
- `1` = root + immediate children
- `2` = root + children + grandchildren

---

## 🔍 Real Example

```python
explorer = DirectoryExplorer(ignore_patterns=['.git', '__pycache__'])

# Scan current directory, max depth 2
root = explorer.scan_directory('.', current_depth=0, max_depth=2)

# Result: DirectoryNode tree like this:
# .
# ├── bst.py (file)
# ├── learn_recursion.py (file)
# └── Directory Tree Explorer/
#     └── dir_explorer.py (file)
```

---

## 🐛 Common Pitfalls

### **1. Forgetting to increase depth:**
```python
# WRONG: depth never increases!
child_node = self.scan_directory(full_path, current_depth, max_depth)

# CORRECT: increment depth!
child_node = self.scan_directory(full_path, current_depth + 1, max_depth)
```

### **2. Not handling permissions:**
```python
# WRONG: Can crash on permission denied
items = os.listdir(path)

# CORRECT: Use try/except
try:
    items = os.listdir(path)
except OSError:
    return node  # Can't read, stop here
```

### **3. Forgetting base cases:**
Must check BOTH:
- Max depth reached?
- Is it a file (not directory)?

---

## ✅ Testing Strategy

1. **Test with depth=0**: Should only return root node, no children
2. **Test with depth=1**: Should return root + immediate children
3. **Test with unlimited depth**: Should scan everything
4. **Test ignore patterns**: Should skip .git, __pycache__, etc.
5. **Test on current directory**: Should work on your project folder!

---

## 🎯 Success Criteria

After implementing, you should be able to:
- ✅ Scan any directory on your system
- ✅ Build a complete DirectoryNode tree
- ✅ Limit scanning depth
- ✅ Skip ignored patterns (.git, etc.)
- ✅ Handle permission errors gracefully
- ✅ See total file count and sizes using your DirectoryNode methods!

---

## 🚀 Ready to Code!

Implement the 3 methods:
1. `__init__` - Store ignore patterns
2. `_should_ignore` - Check if name matches ignore pattern
3. `scan_directory` - THE BIG RECURSIVE METHOD

Then run the tests to see it work on real directories! 🌳
