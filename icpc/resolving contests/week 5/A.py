# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    t = int(input().strip())
    total_sum = 0
    for _ in range(t):
        n = int(input().strip())
        total_sum = n + total_sum

    print(total_sum)
    if total_sum >= 10000:
        print("Lucky you!")
    else:
        print("What a pity!")

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()