# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

def solve():
    data = sys.stdin.read().split()

    index = 0
    t = int(data[index])
    index += 1
    for _ in range(t):
        n = int(data[index])
        q = int(data[index + 1])
        index += 2

        a = []
        for i in range(n):
            a.append(int(data[index + i]))
        index += n

        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + math.log10(a[i - 1])

        for _ in range(q):
            l = int(data[index])
            r = int(data[index + 1])
            index += 2

            left = min(l, r) - 1
            right = max(l, r) - 1

            log_sum = prefix[right + 1] - prefix[left]
            digits = math.floor(log_sum) + 1
            print(digits)

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()