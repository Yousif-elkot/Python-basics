# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    n, k = map(int, input().strip().split())
    
    # Key insight: sum of k odd numbers is:
    # - odd if k is odd
    # - even if k is even
    
    # Also need n >= k (minimum k odd numbers = k*1 = k)
    
    if n < k:
        print("NO")
        return
    
    # Check if n and k have the same parity
    if n % 2 == k % 2:
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