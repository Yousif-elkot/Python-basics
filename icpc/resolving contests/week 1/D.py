# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

input = sys.stdin.readline

def close_enough(x, y):
    """Check if two floating point numbers are close enough"""
    return abs(x - y) <= 1e-9 * max(1.0, max(abs(x), abs(y)))

def solve():
    # Read as floats to handle decimal inputs like 4.5
    a, b, c = map(float, input().split())
    v = [a, b, c]
    
    ok = False
    
    # Check all combinations: v[i]^v[j] = v[k] where i, j, k are all different
    for i in range(3):
        if ok:
            break
        for j in range(3):
            if ok:
                break
            for k in range(3):
                if i != j and i != k and j != k:
                    # Check if v[i]^v[j] = v[k]
                    # Using logarithms: v[j] * log(v[i]) = log(v[k])
                    if v[i] > 0 and v[j] > 0 and v[k] > 0:
                        try:
                            lhs = v[j] * math.log(v[i])
                            rhs = math.log(v[k])
                            if close_enough(lhs, rhs):
                                ok = True
                                break
                        except:
                            pass
    
    # Check self-power condition: v[i]^v[i] = v[j] where i != j
    for i in range(3):
        if ok:
            break
        for j in range(3):
            if i != j and v[i] > 0 and v[j] > 0:
                try:
                    lhs = v[i] * math.log(v[i])
                    rhs = math.log(v[j])
                    if close_enough(lhs, rhs):
                        ok = True
                        break
                except:
                    pass
    
    print("YES" if ok else "NO")

if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()