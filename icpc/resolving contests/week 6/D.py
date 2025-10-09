# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    
    def generate(current, open_count, close_count):
        # Base case: if we've used all brackets, print the sequence
        if open_count == n and close_count == n:
            print(current)
            return
        
        # Add opening bracket if we haven't used all open brackets
        if open_count < n:
            generate(current + '(', open_count + 1, close_count)
        
        # Add closing bracket if we have more open than close brackets
        if close_count < open_count:
            generate(current + ')', open_count, close_count + 1)
    
    # Start with empty string and 0 open, 0 close
    generate('', 0, 0)

if __name__ == "__main__":
    solve()
