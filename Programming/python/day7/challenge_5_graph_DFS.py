"""
V - Visualize & Verify (The "What")

P - Pseudocode (The "How")

C - Code (The "Do")

R - Refine & Reflect (The "Check")
"""

from typing import List

def num_islands(grid: List[List[str]]) -> int:
    """
    Given 2D grid of '1' (land) and '0' (water), count number of islands.
    """
    
    # pseudocode: An empty grid has 0 islands.
    if not grid:
        return 0
    
    # pseudocode: Get the dimensions of the grid to use for bounds checking.
    rows, cols = len(grid), len(grid[0])
    
    # pseudocode: Create a variable to hold the count.
    island_count = 0

    def dfs(r, c):
        # pseudocode: Base Cases for stopping the recursion:
        # 1. If the row (r) is out of bounds (less than 0 or >= rows)
        # 2. OR if the column (c) is out of bounds (less than 0 or >= cols)
        # 3. OR if the current cell is water ('0') or already visited ('#')
        # If any of these are true, stop exploring this path.
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return   

        # pseudocode: The "Sinking" Action: Mark the current cell as visited.
        # We'll use '#' to show it's part of a found island.
        grid[r][c] = '#'  

        # pseudocode: The Recursive Exploration: Call dfs on all 4 neighbors.
        dfs(r - 1, c)  
        dfs(r + 1, c)  
        dfs(r, c - 1)  
        dfs(r, c + 1)  

    # pseudocode: Main Logic: Scan the entire grid.
    # pseudocode: Loop through every row index 'r'.
    for r in range(rows):
        # pseudocode: Loop through every column index 'c'.
        for c in range(cols):
            # pseudocode: If you find a '1', you've found a new island.
            if grid[r][c] == '1':
                # pseudocode: Increment the island count.
                island_count += 1  

                # pseudocode: Start the DFS to sink the entire island.
                dfs(r, c)

    # pseudocode: After checking every cell, return the total count.
    return island_count