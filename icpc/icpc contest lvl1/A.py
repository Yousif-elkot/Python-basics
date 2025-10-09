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

    #book types stack
    stacks = {
        1: deque(),
        2: deque(),
        3: deque()
    }

    # n queries
    for minute in range(1, n + 1):
        query = input().strip().split()
        action = query[0]
        book_type = int(query[1])

        if action == '+':
            stacks[book_type].append(minute)
        else:
            if stacks[book_type]:
                book_id = stacks[book_type].pop()
                print(book_id)
            else:
                print(-1)

                
if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()