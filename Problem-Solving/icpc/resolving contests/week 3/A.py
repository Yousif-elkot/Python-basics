# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    t = int(input())
    
    for _ in range(t):
        s = input().strip()  # Read as string, not split by spaces
        
        # Count 0s and 1s
        ones = s.count('1')
        zeros = s.count('0')
        
        # Check conditions:
        # 1. Both counts must be divisible by 2 (even)
        # 2. Must have BOTH types of flowers (not all 0s or all 1s)
        if ones > 0 and zeros > 0 and ones % 2 == 0 and zeros % 2 == 0:
            print("The Magic Sparkles!")
        else:
            print("The Gate Remains Closed.")


if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()