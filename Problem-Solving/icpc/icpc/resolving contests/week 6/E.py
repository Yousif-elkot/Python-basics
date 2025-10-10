# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    a , b = map(int, input().split())
    if a > b:
        print("Second Army")
    elif a < b:
        print("First Army")
    else:
        print("can't be determined")

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()
