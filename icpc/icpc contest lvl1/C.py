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

    #helper function (3lshan mazen bybks)
    def lawi2(n):
        result = (n * (n + 1) * (2 * n + 1)) // 6
        return result
    def lawi(n):
        result = (n * (n + 1)) // 2
        return result
    
    def equation(n):
        upper = (2 * lawi2(n) * pow(lawi(n), 2))
        lower = (2 * lawi2(n) * lawi(n))
        result = upper // lower
        return result
    
    print(equation(n))

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()