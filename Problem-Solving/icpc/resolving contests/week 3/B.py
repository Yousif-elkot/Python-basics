# Create: ~/icpc/template.py
import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math

def solve():
    import sys
    data = sys.stdin.read().split()
    
    if len(data) != 2:
        print("NO")
        return
    
    s = data[0]
    m = data[1]
    
    s_len = len(s)
    m_len = len(m)
    
    if s_len > m_len:
        print("NO")
        return
    
    # Frequency array approach (fast)
    s_freq = [0] * 26
    for c in s:
        s_freq[ord(c) - ord('a')] += 1
    
    # Initialize first window
    window_freq = [0] * 26
    for i in range(s_len):
        window_freq[ord(m[i]) - ord('a')] += 1
    
    # Check first window
    if window_freq == s_freq:
        print("YES")
        return
    
    # Sliding window
    for i in range(s_len, m_len):
        # Add new character (right side)
        window_freq[ord(m[i]) - ord('a')] += 1
        
        # Remove old character (left side)
        window_freq[ord(m[i - s_len]) - ord('a')] -= 1
        
        # Check if current window matches
        if window_freq == s_freq:
            print("YES")
            return
    
    print("NO")


if __name__ == "__main__":
    # Single test case
    solve()
    
    # OR Multiple test cases
    # t = int(input())
    # for _ in range(t):
    #     solve()