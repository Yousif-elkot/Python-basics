"""
V - Visualize & Verify (The "What")

P - Pseudocode (The "How")

C - Code (The "Do")

R - Refine & Reflect (The "Check")
"""

import sys
from collections import deque, Counter, defaultdict
from functools import lru_cache
import heapq
import bisect
import math
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers, return indices of two numbers 
    that add up to target. You can assume exactly one solution exists.
    
    Example:
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]  # Because nums[0] + nums[1] = 2 + 7 = 9
    """
    #pseudocode: initialize a hash table to store numbers and their indices
    seen_nums = {}
    #pseudocode: the loop: for each number in the array: for i number in enumerate(nums):
    for i, number in enumerate(nums):
        #pseudocode: calculate complement = target - number
        complement = target - number
        #pseudocode: if complement in hash table: return [hash_table[complement], i]
        if complement in seen_nums:
            return [seen_nums[complement], i]
        #pseudocode: else: store number and its index in hash table:
        seen_nums[number] = i