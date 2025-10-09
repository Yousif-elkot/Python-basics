# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

def solve():
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    
    # Build prefix sums for even and odd indices
    # prefix_even[i] = sum of A[j] where j is even and j < i
    # prefix_odd[i] = sum of A[j] where j is odd and j < i
    
    prefix_even = [0] * (n + 1)
    prefix_odd = [0] * (n + 1)
    
    for i in range(n):
        prefix_even[i + 1] = prefix_even[i]
        prefix_odd[i + 1] = prefix_odd[i]
        
        if i % 2 == 0:  # even index
            prefix_even[i + 1] += A[i]
        else:  # odd index
            prefix_odd[i + 1] += A[i]
    
    q = int(sys.stdin.readline())
    for _ in range(q):
        l, r = map(int, sys.stdin.readline().split())
        
        # Sum of even indices in range [l, r]
        even_sum = prefix_even[r + 1] - prefix_even[l]
        
        # Sum of odd indices in range [l, r]
        odd_sum = prefix_odd[r + 1] - prefix_odd[l]
        
        # Result: even_sum - odd_sum
        print(even_sum - odd_sum)

if __name__ == "__main__":
    # Single test case
    solve()