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
    last_two_digits = pow(15, n, 100)
    
    # Format as two digits (pad with zero if needed)
    print(f"{last_two_digits:02d}")

if __name__ == "__main__":
    # Single test case
    solve()


