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
    m = int(input().strip())
    a , b = map(int, input().split())

    area_square = m * m
    area_rectangle = a * b
    area_rectangle_total = area_rectangle * n

    if area_square >= area_rectangle_total:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()