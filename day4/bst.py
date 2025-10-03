#!/usr/bin/env python3
"""
Binary Search Tree Implementation
Day 4 - Project 1

A Binary Search Tree (BST) is a tree data structure where:
- Each node has at most 2 children (left and right)
- Left subtree contains only nodes with values LESS than parent
- Right subtree contains only nodes with values GREATER than parent
- Both left and right subtrees are also BSTs

This property makes searching very efficient: O(log n) for balanced trees!
"""

from collections import deque
from typing import Optional, List, Any


class TreeNode:
    """
    Represents a single node in the Binary Search Tree.
    
    Each node contains:
    - value: The data stored in the node
    - left: Reference to left child (smaller values)
    - right: Reference to right child (larger values)
    """
    
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
    
    def __repr__(self):
        return f"TreeNode({self.value})"


class BinarySearchTree:
    """
    Binary Search Tree implementation with common operations.
    """
    
    def __init__(self):
        self.root: Optional[TreeNode] = None
    
    def insert(self, value: Any) -> None:
        """Insert a new value into the BST."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: TreeNode, value: Any) -> TreeNode:
        """Recursive helper for insert operation."""
        if value == node.value:
            return node
        
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
        return node        

    def search(self, value: Any) -> bool:
        """Search for a value in the BST. Returns True if found."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Optional[TreeNode], value: Any) -> bool:
        """Recursive helper for search operation."""
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def inorder(self) -> List[Any]:
        """Inorder traversal: Left → Root → Right. Returns sorted values."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Recursive helper for inorder traversal."""
        if node is None:
            return
        self._inorder_recursive(node.left, result)
        result.append(node.value)
        self._inorder_recursive(node.right, result)

    def preorder(self) -> List[Any]:
        """Preorder traversal: Root → Left → Right."""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Recursive helper for preorder traversal."""
        if node is None:
            return
        result.append(node.value)
        self._preorder_recursive(node.left, result)
        self._preorder_recursive(node.right, result)
    
    def postorder(self) -> List[Any]:
        """Postorder traversal: Left → Right → Root."""
        result = []
        self._postorder_recursive(self.root, result)
        return result
        
    def _postorder_recursive(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Recursive helper for postorder traversal."""
        if node is None:
            return
        self._postorder_recursive(node.left, result)
        self._postorder_recursive(node.right, result)
        result.append(node.value)

    def level_order(self) -> List[Any]:
        """Level-order traversal (BFS). Processes tree level by level."""
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
    
    def count_nodes(self) -> int:
        """Count total number of nodes in the tree."""
        return self._count_recursive(self.root)
    
    def _count_recursive(self, node: Optional[TreeNode]) -> int:
        """Recursive helper for counting nodes."""
        if node is None:
            return 0
        return 1 + self._count_recursive(node.left) + self._count_recursive(node.right)

    def height(self) -> int:
        """Calculate height of the tree (longest path from root to leaf)."""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node: Optional[TreeNode]) -> int:
        """Recursive helper for calculating tree height."""
        if node is None:
            return -1
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

    def find_min(self) -> Optional[Any]:
        """Find minimum value in BST (leftmost node)."""
        if self.root is None:
            return None
        
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self) -> Optional[Any]:
        """Find maximum value in BST (rightmost node)."""
        if self.root is None:
            return None
        
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value
    
    def display(self) -> None:
        """Display the tree structure visually."""
        if not self.root:
            print("Empty tree")
            return
        
        print("\nBinary Search Tree Structure:")
        print("=" * 40)
        self._display_recursive(self.root, "", True)
        print("=" * 40)
    
    def _display_recursive(self, node: Optional[TreeNode], prefix: str, is_tail: bool) -> None:
        """Recursive helper for tree visualization."""
        if node is None:
            return
        
        print(prefix + ("└── " if is_tail else "├── ") + str(node.value))
        
        if node.left or node.right:
            if node.left:
                self._display_recursive(
                    node.left,
                    prefix + ("    " if is_tail else "│   "),
                    False if node.right else True
                )
            
            if node.right:
                self._display_recursive(
                    node.right,
                    prefix + ("    " if is_tail else "│   "),
                    True
                )


def test_bst():
    """Test the BST implementation with various operations."""
    print("=" * 60)
    print("🧪 Testing Binary Search Tree")
    print("=" * 60)
    
    bst = BinarySearchTree()
    
    # Test 1: Insert
    print("\n1️⃣ Testing INSERT:")
    print("-" * 40)
    values = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserting values: {values}")
    for val in values:
        bst.insert(val)
    print("✅ Insert complete!")
    bst.display()
    
    # Test 2: Search
    print("\n2️⃣ Testing SEARCH:")
    print("-" * 40)
    for val in [40, 100, 20]:
        found = bst.search(val)
        status = "✅ Found" if found else "❌ Not found"
        print(f"Search {val}: {status}")
    
    # Test 3: Traversals
    print("\n3️⃣ Testing TRAVERSALS:")
    print("-" * 40)
    print(f"Inorder (sorted):    {bst.inorder()}")
    print(f"Preorder:            {bst.preorder()}")
    print(f"Postorder:           {bst.postorder()}")
    print(f"Level-order:         {bst.level_order()}")
    
    # Test 4: Helpers
    print("\n4️⃣ Testing HELPER METHODS:")
    print("-" * 40)
    print(f"Total nodes:         {bst.count_nodes()}")
    print(f"Tree height:         {bst.height()}")
    print(f"Minimum value:       {bst.find_min()}")
    print(f"Maximum value:       {bst.find_max()}")
    
    print("\n" + "=" * 60)
    print("✅ All tests complete!")
    print("=" * 60)


if __name__ == "__main__":
    test_bst()
