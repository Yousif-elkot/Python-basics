# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    # Precompute the number of ways for all N up to 27
    # dp[i] = number of ways to make i kg
    MAX_N = 27
    dp = [0] * (MAX_N + 1)
    
    # Base cases
    dp[0] = 1  # 1 way: do nothing
    
    for i in range(1, MAX_N + 1):
        # Add ways ending with 1kg sandwich
        if i >= 1:
            dp[i] += dp[i - 1]
        # Add ways ending with 2kg sandwich  
        if i >= 2:
            dp[i] += dp[i - 2]
        # Add ways ending with 3kg sandwich
        if i >= 3:
            dp[i] += dp[i - 3]
    
    # Read input
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        print(dp[N])

if __name__ == "__main__":
    solve()
