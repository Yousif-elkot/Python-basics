# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    
    # The formula: S(n) = sum(2k^2 - k + 1/6) - sum(k - 1/6) for k=1 to n
    # Direct calculation with floating point
    sum1 = sum(2*k**2 - k + 1/6 for k in range(1, n+1))
    sum2 = sum(k - 1/6 for k in range(1, n+1))
    result = sum1 - sum2
    
    # Print floor of result
    print(int(result))
if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()