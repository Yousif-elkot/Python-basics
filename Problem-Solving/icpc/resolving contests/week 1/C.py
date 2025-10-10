# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    for i in range(5):
        op , x = input().strip().split()
        x = int(x)
        if op == '+':
            n += x
        elif op == '-':
            n -= x
        elif op == '*':
            n *= x
        else:
            return None
    print(n)

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()