# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect

input = sys.stdin.readline

def solve():
    # Read team name
    name = input().strip()
    # Print welcome message (exact format: "Welcome, <name>")
    print(f"Welcome, {name}!")

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()