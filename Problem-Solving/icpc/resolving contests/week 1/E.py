# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    x, y = map(int, input().split())
    distance = math.sqrt(x**2 + y**2)
    if distance == int(distance):  # Check if it's a whole number
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