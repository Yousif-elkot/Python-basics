# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def get_prime_factors(n):

        if n == 1:
            return []
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors

def solve():
    s = input().strip()
    n = len(s)

    prime_factors = get_prime_factors(n)

    if not prime_factors:
        print("NO")
        return

    pos = 0
    is_task_string = True

    for prime in prime_factors:
        if pos + prime > n:
            break
        substring = s[pos: pos + prime]
        # convert b to d
        decimal_value = int(substring, 2)

        if decimal_value > prime:
            is_task_string = False
            break
        pos += prime
    print("YES" if is_task_string else "NO")
    
if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()