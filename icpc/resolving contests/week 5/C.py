# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Method 1: Using Counter (recommended - efficient and clean)
    freq = Counter(arr)
    
    # Count numbers that appear exactly once
    unique_count = 0
    for count in freq.values():
        if count == 1:
            unique_count += 1
    
    print(unique_count)

if __name__ == "__main__":
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()