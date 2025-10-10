# Create: ~/icpc/template.py
from operator import mod
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    def Tiny_equation(n):
        result = mod(n, m)
        return result
    
    def Range(n):
        # Base case: any number less than 1 has range = 1
        if n < 1:
            return 1
        
        # Recursive case
        result = Range(n // 2) + Range(Tiny_equation(n) - 1) + Range(Tiny_equation(n) - 3)
        return result

    n, m = map(int, input().split())
    print(Range(n))

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()
