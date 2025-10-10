# 🗺️ Day 4 Implementation Roadmap

**Detailed step-by-step guide for implementing all Day 4 projects**

---

## 📋 Project 1: Binary Search Tree (BST)

### Phase 1: Node Class (15 minutes)

**Step 1.1: Create the TreeNode class**

```python
class TreeNode:
    """A node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return f"TreeNode({self.value})"
```

**What you're learning:**
- Each node stores: data (value), left child pointer, right child pointer
- `None` means no child (leaf node)
- This is the building block for all tree operations

**Test it:**
```python
node = TreeNode(10)
print(node)  # TreeNode(10)
print(node.left)  # None
```

---

### Phase 2: Insert Operation (20 minutes)

**Step 2.1: Implement insert (recursive)**

```python
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper: Insert value starting from node."""
        # If value already exists, do nothing (or update)
        if value == node.value:
            return
        
        # Go left if value is smaller
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        
        # Go right if value is larger
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
```

**Key concepts:**
- **BST Property:** Left < Parent < Right
- **Recursive thinking:** Solve for subtree, then combine
- **Base case:** Reached empty spot, create new node
- **Recursive case:** Keep going left or right

**Test it:**
```python
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# Tree structure:
#        50
#       /  \
#      30   70
#     / \   / \
#    20 40 60 80
```

---

### Phase 3: Search Operation (15 minutes)

**Step 3.1: Implement search**

```python
def search(self, value):
    """Search for a value in the BST."""
    return self._search_recursive(self.root, value)

def _search_recursive(self, node, value):
    """Helper: Search starting from node."""
    # Base case: not found
    if node is None:
        return False
    
    # Base case: found it!
    if value == node.value:
        return True
    
    # Recursive case: go left or right
    if value < node.value:
        return self._search_recursive(node.left, value)
    else:
        return self._search_recursive(node.right, value)
```

**Key concepts:**
- **Binary search:** Eliminate half the tree at each step
- **Time complexity:** O(log n) average, O(n) worst case
- **Three outcomes:** found, go left, go right

**Test it:**
```python
print(bst.search(40))   # True
print(bst.search(100))  # False
print(bst.search(20))   # True
```

---

### Phase 4: Tree Traversals (30 minutes)

**Step 4.1: Inorder Traversal (Left → Root → Right)**

```python
def inorder(self):
    """Return list of values in sorted order."""
    result = []
    self._inorder_recursive(self.root, result)
    return result

def _inorder_recursive(self, node, result):
    """Helper: Inorder traversal."""
    if node is None:
        return
    
    self._inorder_recursive(node.left, result)   # Left
    result.append(node.value)                     # Root
    self._inorder_recursive(node.right, result)  # Right
```

**Step 4.2: Preorder Traversal (Root → Left → Right)**

```python
def preorder(self):
    """Return list of values in preorder."""
    result = []
    self._preorder_recursive(self.root, result)
    return result

def _preorder_recursive(self, node, result):
    """Helper: Preorder traversal."""
    if node is None:
        return
    
    result.append(node.value)                     # Root
    self._preorder_recursive(node.left, result)   # Left
    self._preorder_recursive(node.right, result)  # Right
```

**Step 4.3: Postorder Traversal (Left → Right → Root)**

```python
def postorder(self):
    """Return list of values in postorder."""
    result = []
    self._postorder_recursive(self.root, result)
    return result

def _postorder_recursive(self, node, result):
    """Helper: Postorder traversal."""
    if node is None:
        return
    
    self._postorder_recursive(node.left, result)   # Left
    self._postorder_recursive(node.right, result)  # Right
    result.append(node.value)                      # Root
```

**Step 4.4: Level-order Traversal (BFS)**

```python
from collections import deque

def levelorder(self):
    """Return list of values level by level."""
    if self.root is None:
        return []
    
    result = []
    queue = deque([self.root])
    
    while queue:
        node = queue.popleft()
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result
```

**Test all traversals:**
```python
# Tree:        50
#            /    \
#          30      70
#         / \     / \
#        20 40   60 80

print(bst.inorder())     # [20, 30, 40, 50, 60, 70, 80] - Sorted!
print(bst.preorder())    # [50, 30, 20, 40, 70, 60, 80]
print(bst.postorder())   # [20, 40, 30, 60, 80, 70, 50]
print(bst.levelorder())  # [50, 30, 70, 20, 40, 60, 80]
```

**When to use each:**
- **Inorder:** Get sorted values from BST
- **Preorder:** Copy tree structure, serialize tree
- **Postorder:** Delete tree safely, evaluate expression trees
- **Level-order:** Level-by-level processing, shortest path

---

### Phase 5: Helper Methods (20 minutes)

**Step 5.1: Count nodes**

```python
def count_nodes(self):
    """Return total number of nodes."""
    return self._count_recursive(self.root)

def _count_recursive(self, node):
    if node is None:
        return 0
    return 1 + self._count_recursive(node.left) + self._count_recursive(node.right)
```

**Step 5.2: Get height**

```python
def height(self):
    """Return height of tree (longest path from root to leaf)."""
    return self._height_recursive(self.root)

def _height_recursive(self, node):
    if node is None:
        return -1  # Empty tree has height -1
    
    left_height = self._height_recursive(node.left)
    right_height = self._height_recursive(node.right)
    
    return 1 + max(left_height, right_height)
```

**Step 5.3: Find min and max**

```python
def find_min(self):
    """Find minimum value (leftmost node)."""
    if self.root is None:
        return None
    
    node = self.root
    while node.left is not None:
        node = node.left
    return node.value

def find_max(self):
    """Find maximum value (rightmost node)."""
    if self.root is None:
        return None
    
    node = self.root
    while node.right is not None:
        node = node.right
    return node.value
```

**Step 5.4: Check if balanced**

```python
def is_balanced(self):
    """Check if tree is height-balanced."""
    return self._is_balanced_recursive(self.root) != -1

def _is_balanced_recursive(self, node):
    """Return height if balanced, -1 if unbalanced."""
    if node is None:
        return 0
    
    left_height = self._is_balanced_recursive(node.left)
    if left_height == -1:
        return -1
    
    right_height = self._is_balanced_recursive(node.right)
    if right_height == -1:
        return -1
    
    # Check if difference is more than 1
    if abs(left_height - right_height) > 1:
        return -1
    
    return 1 + max(left_height, right_height)
```

---

### Phase 6: Delete Operation (30 minutes) - CHALLENGING!

**Step 6.1: Understand 3 cases**

1. **Node is a leaf** (no children) → Simply remove it
2. **Node has one child** → Replace node with its child
3. **Node has two children** → Replace with inorder successor (or predecessor)

**Step 6.2: Implement delete**

```python
def delete(self, value):
    """Delete a value from the BST."""
    self.root = self._delete_recursive(self.root, value)

def _delete_recursive(self, node, value):
    """Helper: Delete value from subtree rooted at node."""
    if node is None:
        return None
    
    # Find the node to delete
    if value < node.value:
        node.left = self._delete_recursive(node.left, value)
    elif value > node.value:
        node.right = self._delete_recursive(node.right, value)
    else:
        # Found the node to delete!
        
        # Case 1: Leaf node (no children)
        if node.left is None and node.right is None:
            return None
        
        # Case 2a: Only right child
        if node.left is None:
            return node.right
        
        # Case 2b: Only left child
        if node.right is None:
            return node.left
        
        # Case 3: Two children
        # Find inorder successor (min value in right subtree)
        successor = self._find_min_node(node.right)
        node.value = successor.value
        node.right = self._delete_recursive(node.right, successor.value)
    
    return node

def _find_min_node(self, node):
    """Find node with minimum value in subtree."""
    while node.left is not None:
        node = node.left
    return node
```

**Test delete:**
```python
bst.delete(20)  # Delete leaf
bst.delete(30)  # Delete node with two children
bst.delete(50)  # Delete root
```

---

### Phase 7: Visualization (15 minutes)

**Step 7.1: Simple tree printer**

```python
def print_tree(self):
    """Print tree structure."""
    if self.root is None:
        print("Empty tree")
        return
    
    self._print_recursive(self.root, "", True)

def _print_recursive(self, node, prefix, is_tail):
    """Helper: Print tree with ASCII art."""
    if node is None:
        return
    
    print(prefix + ("└── " if is_tail else "├── ") + str(node.value))
    
    if node.left or node.right:
        if node.left:
            self._print_recursive(node.left, prefix + ("    " if is_tail else "│   "), False if node.right else True)
        if node.right:
            self._print_recursive(node.right, prefix + ("    " if is_tail else "│   "), True)
```

**Output example:**
```
└── 50
    ├── 30
    │   ├── 20
    │   └── 40
    └── 70
        ├── 60
        └── 80
```

---

## 📋 Project 2: Directory Tree Explorer

### Phase 1: Basic Directory Traversal (20 minutes)

**Step 1.1: List directory contents**

```python
import os

def list_directory(path):
    """List all files and folders in path."""
    try:
        entries = os.listdir(path)
        for entry in entries:
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                print(f"📁 {entry}/")
            else:
                print(f"📄 {entry}")
    except PermissionError:
        print(f"❌ Permission denied: {path}")
```

**Step 1.2: Recursive directory traversal**

```python
def traverse_directory(path, depth=0):
    """Recursively traverse directory tree."""
    indent = "  " * depth
    
    try:
        entries = sorted(os.listdir(path))
        
        for entry in entries:
            full_path = os.path.join(path, entry)
            
            if os.path.isdir(full_path):
                print(f"{indent}📁 {entry}/")
                traverse_directory(full_path, depth + 1)
            else:
                print(f"{indent}📄 {entry}")
    
    except PermissionError:
        print(f"{indent}❌ Permission denied")
```

**Test it:**
```python
traverse_directory("/home/kot/projects/git/day3")
```

---

### Phase 2: Tree Visualization (25 minutes)

**Step 2.1: Create tree structure with lines**

```python
def show_tree(path, prefix="", max_depth=None, current_depth=0):
    """Show directory tree with ASCII art."""
    if max_depth is not None and current_depth >= max_depth:
        return
    
    try:
        entries = sorted(os.listdir(path))
        entries = [e for e in entries if not e.startswith('.')]  # Skip hidden
        
        for i, entry in enumerate(entries):
            is_last = (i == len(entries) - 1)
            full_path = os.path.join(path, entry)
            
            # Choose connector
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{entry}")
            
            # Recurse into directories
            if os.path.isdir(full_path):
                extension = "    " if is_last else "│   "
                show_tree(full_path, prefix + extension, max_depth, current_depth + 1)
    
    except PermissionError:
        pass
```

---

### Phase 3: Statistics (20 minutes)

**Step 3.1: Count files and calculate sizes**

```python
class DirectoryStats:
    def __init__(self):
        self.total_files = 0
        self.total_dirs = 0
        self.total_size = 0
        self.file_types = {}
    
    def scan(self, path):
        """Scan directory and collect statistics."""
        try:
            for entry in os.listdir(path):
                full_path = os.path.join(path, entry)
                
                if os.path.isdir(full_path):
                    self.total_dirs += 1
                    self.scan(full_path)  # Recurse
                else:
                    self.total_files += 1
                    size = os.path.getsize(full_path)
                    self.total_size += size
                    
                    # Track file types
                    ext = os.path.splitext(entry)[1] or 'no extension'
                    self.file_types[ext] = self.file_types.get(ext, 0) + 1
        
        except (PermissionError, OSError):
            pass
    
    def format_size(self, size):
        """Convert bytes to human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} TB"
    
    def display(self):
        """Display statistics."""
        print(f"\n📊 Directory Statistics:")
        print(f"Files: {self.total_files}")
        print(f"Directories: {self.total_dirs}")
        print(f"Total Size: {self.format_size(self.total_size)}")
        print(f"\nFile Types:")
        for ext, count in sorted(self.file_types.items(), key=lambda x: x[1], reverse=True):
            print(f"  {ext}: {count}")
```

---

### Phase 4: CLI Interface (20 minutes)

**Step 4.1: Argparse setup**

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Directory Tree Explorer")
    subparsers = parser.add_subparsers(dest='command')
    
    # show command
    show_parser = subparsers.add_parser('show', help='Show directory tree')
    show_parser.add_argument('path', help='Directory path')
    show_parser.add_argument('--depth', type=int, help='Maximum depth')
    
    # stats command
    stats_parser = subparsers.add_parser('stats', help='Show statistics')
    stats_parser.add_argument('path', help='Directory path')
    
    # search command
    search_parser = subparsers.add_parser('search', help='Search for files')
    search_parser.add_argument('path', help='Directory path')
    search_parser.add_argument('--pattern', help='File pattern (e.g., *.py)')
    
    args = parser.parse_args()
    
    if args.command == 'show':
        print(f"📂 {os.path.abspath(args.path)}")
        show_tree(args.path, max_depth=args.depth)
    
    elif args.command == 'stats':
        stats = DirectoryStats()
        stats.scan(args.path)
        stats.display()
    
    elif args.command == 'search':
        search_files(args.path, args.pattern)
    
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
```

---

## 📋 Project 3: Expression Evaluator

### Phase 1: Expression Tree Node (10 minutes)

```python
class ExpressionNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def is_operator(self):
        return self.value in ['+', '-', '*', '/', '^']
    
    def evaluate(self):
        """Evaluate this subtree recursively."""
        if not self.is_operator():
            return float(self.value)
        
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()
        
        if self.value == '+':
            return left_val + right_val
        elif self.value == '-':
            return left_val - right_val
        elif self.value == '*':
            return left_val * right_val
        elif self.value == '/':
            return left_val / right_val
        elif self.value == '^':
            return left_val ** right_val
```

---

### Phase 2: Build Tree from Postfix (20 minutes)

```python
def build_tree_from_postfix(postfix_tokens):
    """Build expression tree from postfix notation."""
    stack = []
    
    for token in postfix_tokens:
        if token in ['+', '-', '*', '/', '^']:
            right = stack.pop()
            left = stack.pop()
            node = ExpressionNode(token, left, right)
            stack.append(node)
        else:
            node = ExpressionNode(token)
            stack.append(node)
    
    return stack[0]

# Example:
postfix = ['3', '4', '2', '*', '+']  # 3 + 4 * 2
tree = build_tree_from_postfix(postfix)
print(tree.evaluate())  # 11
```

---

### Phase 3: Infix to Postfix Conversion (30 minutes)

```python
def infix_to_postfix(expression):
    """Convert infix to postfix using Shunting Yard algorithm."""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    operator_stack = []
    
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    
    for token in tokens:
        if token.isdigit() or '.' in token:
            output.append(token)
        
        elif token == '(':
            operator_stack.append(token)
        
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()  # Remove '('
        
        elif token in precedence:
            while (operator_stack and 
                   operator_stack[-1] != '(' and
                   operator_stack[-1] in precedence and
                   precedence[operator_stack[-1]] >= precedence[token]):
                output.append(operator_stack.pop())
            operator_stack.append(token)
    
    while operator_stack:
        output.append(operator_stack.pop())
    
    return output
```

---

## 📋 Project 4: Duplicate File Finder

### Phase 1: File Hashing (15 minutes)

```python
import hashlib

def calculate_hash(filepath, algorithm='md5'):
    """Calculate hash of file content."""
    hash_obj = hashlib.new(algorithm)
    
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except (IOError, OSError):
        return None
```

---

### Phase 2: Scan for Duplicates (25 minutes)

```python
from collections import defaultdict

class DuplicateFinder:
    def __init__(self):
        self.file_hashes = defaultdict(list)
        self.total_files = 0
    
    def scan_directory(self, path, min_size=0):
        """Scan directory for files and calculate hashes."""
        for root, dirs, files in os.walk(path):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for filename in files:
                if filename.startswith('.'):
                    continue
                
                filepath = os.path.join(root, filename)
                
                try:
                    size = os.path.getsize(filepath)
                    
                    if size < min_size:
                        continue
                    
                    file_hash = calculate_hash(filepath)
                    
                    if file_hash:
                        self.file_hashes[file_hash].append({
                            'path': filepath,
                            'size': size
                        })
                        self.total_files += 1
                
                except (OSError, IOError):
                    continue
    
    def get_duplicates(self):
        """Return groups of duplicate files."""
        duplicates = {}
        
        for file_hash, files in self.file_hashes.items():
            if len(files) > 1:
                duplicates[file_hash] = files
        
        return duplicates
    
    def display_duplicates(self):
        """Display duplicate file groups."""
        duplicates = self.get_duplicates()
        
        if not duplicates:
            print("✅ No duplicates found!")
            return
        
        print(f"\n🔍 Found {len(duplicates)} groups of duplicates:\n")
        
        total_wasted = 0
        
        for i, (file_hash, files) in enumerate(duplicates.items(), 1):
            size = files[0]['size']
            wasted = size * (len(files) - 1)
            total_wasted += wasted
            
            print(f"Group {i} ({len(files)} files, {self.format_size(size)} each):")
            for file_info in files:
                print(f"  - {file_info['path']}")
            print()
        
        print(f"💾 Potential space savings: {self.format_size(total_wasted)}")
    
    def format_size(self, size):
        """Convert bytes to human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} TB"
```

---

## 🎓 Learning Checklist

After completing each project, verify you can:

### Project 1 (BST):
- [ ] Explain tree terminology (root, leaf, height, etc.)
- [ ] Insert values maintaining BST property
- [ ] Search efficiently using BST property
- [ ] Implement all 4 traversal algorithms
- [ ] Delete nodes (all 3 cases)
- [ ] Calculate tree properties (height, count, balanced)
- [ ] Visualize tree structure

### Project 2 (Directory Explorer):
- [ ] Traverse directories recursively
- [ ] Handle permission errors gracefully
- [ ] Visualize tree structure with ASCII art
- [ ] Calculate directory statistics
- [ ] Search for files by pattern
- [ ] Build professional CLI interface

### Project 3 (Expression Evaluator):
- [ ] Build expression trees from postfix
- [ ] Evaluate trees recursively
- [ ] Convert infix to postfix (Shunting Yard)
- [ ] Handle operator precedence
- [ ] Visualize expression trees

### Project 4 (Duplicate Finder):
- [ ] Calculate file hashes efficiently
- [ ] Scan directories recursively
- [ ] Group files by hash value
- [ ] Display human-readable sizes
- [ ] Handle file I/O errors

---

## 💡 Tips for Success

1. **Draw trees on paper first** - Visualize before coding
2. **Test incrementally** - Don't write too much before testing
3. **Use print statements** - Debug recursive calls
4. **Start simple, add features** - Get basic version working first
5. **Take breaks** - Recursion can be mentally taxing
6. **Ask for help** - I'm here to guide you through tricky parts!

---

**Ready to build? Let's grow some trees! 🌳✨**
