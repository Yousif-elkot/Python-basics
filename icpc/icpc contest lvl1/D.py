# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve(n):
    memory = {}

    def count_ways(pos, remaining_sum):
        #pos : for position
        #remaining_sum : for remaining sum ( msh mestahla y3ny)
        if pos == 0:
            return 1 if remaining_sum == 0 else 0
        
        if remaining_sum <= 0:
            return 0
        if (pos, remaining_sum) in memory:
            return memory[(pos, remaining_sum)]
        
        result = 0
        for val in range(1, 7):
            if remaining_sum - val >= 0:
                result += count_ways(pos - 1, remaining_sum - val)

        memory[(pos, remaining_sum)] = result
        return result
    return count_ways(n, 8)

n = int(input().strip())
print(solve(n))

if __name__ == "__main__":
    # Single test case
    solve(n)