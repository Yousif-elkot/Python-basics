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
    l = len(str(n))
    
    #helper function
    def is_prime(l):
        if l < 2:
            return False
        if l == 2:
            return True
        if l % 2 == 0:
            return False
        
        # only check up to sqrt(n)
        sqrt_l = int(math.sqrt(l))
        for i in range(3, sqrt_l + 1, 2):
            if l % i == 0:
                return False
        return True

    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]
    
    if is_prime(l) and is_palindrome(n):
        print("Good palindrome number")
    elif is_palindrome(n) and not is_prime(l):
        print("Bad palindrome number")
    else:
        print("Not palindrome")

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()