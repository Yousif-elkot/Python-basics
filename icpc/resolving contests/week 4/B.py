# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():    
    #sanad's position
    x1, y1 = map(int, input().split())
    #target's position
    x2, y2 = map(int, input().split())
    #number of obstacles
    n = int(input().strip())
    for _ in range(n):
        xi, yi = map(int, input().split())
        
        # Check if obstacle is on the line segment between (x1,y1) and (x2,y2)
        # 1. Collinearity check using cross product
        # Cross product = 0 means points are collinear
        cross_product = (y2 - y1) * (xi - x1) - (yi - y1) * (x2 - x1)
        
        if cross_product == 0:
            # Points are collinear, now check if obstacle is between start and target
            if x1 <= xi <= x2 and y1 <= yi <= y2:
                # Obstacle blocks the path
                print("Not reached!")
                return
    
    # No obstacles block the path
    print("Target reached!")

    

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()