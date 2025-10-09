# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect

input = sys.stdin.readline

def solve():
    n, m = map(int, input().strip().split())
    
    # Count soldiers and thieves
    soldiers = 0
    thieves = 0
    
    for _ in range(n):
        row = input().strip()
        soldiers += row.count('*')
        thieves += row.count('.')
    
    # Special case: no thieves to surround
    if thieves == 0:
        print("Mission complete!")
        return
    
   
    if soldiers >= (thieves * 2) +2:
        print("Mission complete!")
    else:
        print("Mission failed.")

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()