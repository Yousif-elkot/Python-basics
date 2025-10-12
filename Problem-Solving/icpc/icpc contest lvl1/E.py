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
    A = list(map(int, input().strip().split()))

    prefix_even = [0] * n
    prefix_odd = [0] * n

    for i in range(n):
        if i == 0:
            if i % 2 == 0: #even
                prefix_even[i] = A[i]
                prefix_odd[i] = 0
            else: #odd
                prefix_even[i] = 0
                prefix_odd[i] = A[i]
        else:
            if i % 2 == 0: #even
                prefix_even[i] = prefix_even[i - 1] + A[i]
                prefix_odd[i] = prefix_odd[i - 1]
            else: #odd
                prefix_even[i] = prefix_even[i - 1]
                prefix_odd[i] = prefix_odd[i - 1] + A[i]

    q = int(input().strip())
    for _ in range(q):
        l , r = map(int, input().strip().split())

        # get some of the even num in range l to r
        even_sum = prefix_even[r]
        if l > 0:
            even_sum -= prefix_even[l - 1]
        
        # get some of the odd num in range l to r
        odd_sum = prefix_odd[r]
        if l > 0:
            odd_sum -= prefix_odd[l - 1]

        result = even_sum - odd_sum
        print(result)

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()