# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    if n % 4 == 0 or n % 4 == 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()