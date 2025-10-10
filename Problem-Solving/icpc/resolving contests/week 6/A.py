# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    t = int(input().strip())
    for _ in range(t):
        n, m = map(int, input().split())
        
        # Count how many numbers from 1 to n are divisible by m
        # Numbers divisible by m: m, 2m, 3m, ..., km where km <= n
        # So count = n // m (floor division)
        count_divisible = n // m
        
        # Probability = count_divisible / n
        # Simplify the fraction using GCD
        numerator = count_divisible
        denominator = n
        
        # Find GCD and simplify
        gcd = math.gcd(numerator, denominator)
        numerator //= gcd
        denominator //= gcd
        
        print(f"{numerator}/{denominator}")


if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()
