# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    s = input().strip()
    n = len(s)
    s = list(s)  # Convert to list

    left, right = 0, n - 1 # Two pointers

    while left < right:
        if s[left] == '?' and s[right] == '?':
            s[left] = 'a'
            s[right] = 'a'
        elif s[left] == '?':
            s[left] = s[right]
        elif s[right] == '?':
            s[right] = s[left]
        else:
            if s[left] != s[right]:
                print(-1)
                return
        left += 1
        right -= 1

    if n % 2 == 1:  # odd length here was the problem
        middle = n // 2
        if s[middle] == '?':
            s[middle] = 'a'

    result = ''.join(s)
    print(result)

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()