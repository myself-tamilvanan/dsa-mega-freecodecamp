"""
Chapter 00: Introduction & Complexity Analysis
=============================================
Demonstrates each Big O complexity class with concrete examples.
"""

import time


def constant(arr):
    """O(1) - always same time regardless of input size."""
    return arr[0] if arr else None


def logarithmic(arr, target):
    """O(log n) - binary search halves search space."""
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target: return m
        elif arr[m] < target: l = m + 1
        else: r = m - 1
    return -1


def linear(arr, target):
    """O(n) - scans every element."""
    for i, v in enumerate(arr):
        if v == target: return i
    return -1


def quadratic(arr):
    """O(n²) - nested loops compare all pairs."""
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pairs.append((arr[i], arr[j]))
    return pairs


def merge_sort(arr):
    """O(n log n) - divide and conquer."""
    if len(arr) <= 1: return arr
    m = len(arr) // 2
    L, R = merge_sort(arr[:m]), merge_sort(arr[m:])
    res, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]: res.append(L[i]); i += 1
        else: res.append(R[j]); j += 1
    return res + L[i:] + R[j:]


def fib_exponential(n):
    """O(2^n) - each call branches into two more."""
    if n <= 1: return n
    return fib_exponential(n-1) + fib_exponential(n-2)


def fib_linear(n):
    """O(n) - memoized / iterative."""
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a


if __name__ == "__main__":
    data = list(range(1, 1001))
    print("O(1)  first element:", constant(data))
    print("O(log n) binary search 500:", logarithmic(data, 500))
    print("O(n)  linear search 500:", linear(data, 500))
    print("O(n log n) merge sort [5,3,8,1]:", merge_sort([5,3,8,1]))
    print("O(2^n) fib(10):", fib_exponential(10))
    print("O(n)  fib(10) linear:", fib_linear(10))
