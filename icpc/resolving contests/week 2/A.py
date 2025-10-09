# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect

input = sys.stdin.readline

def solve():
    s = input().strip()
    
    # Build compressed string
    compressed = []
    i = 0
    n = len(s)
    
    while i < n:
        current_char = s[i]
        count = 1
        
        # Count consecutive occurrences
        while i + count < n and s[i + count] == current_char:
            count += 1
        
        # Add character and count to compressed string
        compressed.append(current_char + str(count))
        i += count
    
    compressed_str = ''.join(compressed)

    # Return the shorter string (or original if equal)
    if len(compressed_str) < len(s):
        print(compressed_str)
    else:
        print(s)

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()