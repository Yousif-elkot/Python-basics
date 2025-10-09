"""
V - Visualize & Verify (The "What")

P - Pseudocode (The "How")

C - Code (The "Do")

R - Refine & Reflect (The "Check")
"""
from collections import deque
from typing import List

# TreeNode class definition would be here
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: TreeNode) -> List[List[int]]:
    """
    Given binary tree root, return level order traversal.
    
    Example:
        3
       / \
      9  20
        /  \
       15   7
    
    Output: [[3], [9, 20], [15, 7]]
    """
    #pseudocode: edge case: if root is None, return []
    if not root:
        return []

    #pseudocode: initialize: result = [], queue = deque([root])
    result = []
    queue = deque([root])
    #pseudocode: main loop:while queue: (as long as there are nodes to process)
    while queue:
        #pseudocode: list to hold current level values: level = [] 
        level_size = len(queue)
        current_level_values = []
        #pseudocode: inner loop that will run as many times as current level size 
        for _ in range(level_size):
            #pseudocode: get a node from queue 
            current_node = queue.popleft()
            #pseudocode: add it's value to level list
            current_level_values.append(current_node.val)
            #pseudocode: check for children, if they exist add them to next_queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        #pseudocode: after inner loop, add level list to result
        result.append(current_level_values)
        
    #pseudocode: return result
    return result

        