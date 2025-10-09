# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def solve():
    # Read input
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    n = int(input().strip())
    
    # Read all obstacles
    obstacles = []
    for _ in range(n):
        xi, yi = map(int, input().split())
        obstacles.append((xi, yi))
    
    # Prime checking using Sieve of Eratosthenes
    MAX_N = 10**6 + 1
    is_prime = [True] * MAX_N
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(MAX_N**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX_N, i):
                is_prime[j] = False
    
    # Helper function to check if obstacle is on path
    def is_on_path(xi, yi):
        # Cross product for collinearity check
        cross = (y2 - y1) * (xi - x1) - (yi - y1) * (x2 - x1)
        # Check if on line segment
        return cross == 0 and x1 <= xi <= x2 and y1 <= yi <= y2
    
    # Process obstacles with power tracking
    power = 0
    for xi, yi in obstacles:
        if is_on_path(xi, yi):
            # Check if bonus (both coordinates are prime) or minus
            if is_prime[xi] and is_prime[yi]:  # Bonus obstacle
                power += 1
            else:  # Minus obstacle
                if power >= 1:
                    power -= 1
                else:
                    print("Not reached!")
                    return
    
    # If we processed all obstacles successfully
    print("Target reached!")

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()