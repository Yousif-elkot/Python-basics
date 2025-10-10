"""
V - Visualize & Verify (The "What")

P - Pseudocode (The "How")

C - Code (The "Do")

R - Refine & Reflect (The "Check")
"""

from typing import List, Optional

# (Assuming the TreeNode class is defined here or imported)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_path(root: Optional[TreeNode], target: int) -> List[int]:
    """
    Find path from root to node with value = target.
    """
    
    # We will define a "helper" function inside this one to do the recursion.
    # This is a very common and useful pattern!
    
    def _helper(current_node, target, path):
        # pseudocode: Base Case #1: We've fallen off the tree (a dead end).
        # This path has failed, so return False.
        if current_node is None:
            return False # TODO: Return the correct boolean value

        # pseudocode: Step 1: Add the current node's value to our path.
        # We are "trying out" this node.
        path.append(current_node.val) # TODO: Add the current node's value to the path list

        # pseudocode: Base Case #2: We've found the target!
        # This path is a success, so return True.
        if current_node.val == target:
            return True # TODO: Return the correct boolean value

        # pseudocode: Recursive Step (Left): Explore the left child.
        # If the recursive call on the left child returns True, it means it found a path.
        # We should immediately return True to pass the success signal up.
        if _helper(current_node.left, target, path):
            return True # TODO: Return the correct boolean value

        # pseudocode: Recursive Step (Right): Only explore the right if the left failed.
        # If the recursive call on the right child returns True, it also found a path.
        # We should immediately return True.
        if _helper(current_node.right, target, path):
            return True # TODO: Return the correct boolean value

        # pseudocode: Step 2: Backtracking.
        # If we reach this line, neither the node itself nor its children were the target.
        # This node is part of a failed path. We must "undo" our choice.
        # Remove the current node's value from the path.
        path.pop() # TODO: Remove the last item from the path list

        # pseudocode: After backtracking, report failure for this path.
        return False # TODO: Return the correct boolean value

    # --- This is the main part of the find_path function ---
    
    # pseudocode: Create a list to store the path as we build it.
    path = []
    
    # pseudocode: Call the helper function to start the search from the root.
    found = _helper(root, target, path)

    # pseudocode: If the helper function returned True, our path is now correct.
    if found:
        return path
    # pseudocode: Otherwise, no path was found, so return an empty list.
    else:
        return []