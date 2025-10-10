# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    a, b, c = map(int, input().strip().split())
    
    total_sum = 0
    
    # Iterate through all possible x3 values
    for x3 in range(-c, c + 1):
        # Calculate x1 and x2 based on the system of equations:
        # x1 + x2 + x3 = a
        # 2x1 + 3x2 - x3 = b
        # Solution: x1 = 3a - b - 4x3, x2 = b - 2a + 3x3
        x1 = 3 * a - b - 4 * x3
        x2 = b - 2 * a + 3 * x3
        
        # Check if x1 and x2 are within constraints [-c, c]
        if -c <= x1 <= c and -c <= x2 <= c:
            # Add all three values to the total sum
            total_sum += x1 + x2 + x3
    
    print(total_sum)

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()