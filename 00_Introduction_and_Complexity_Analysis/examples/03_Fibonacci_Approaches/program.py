"""Fibonacci - 4 Approaches"""
from functools import lru_cache
import time

def fib_naive(n):
    if n<=1: return n
    return fib_naive(n-1)+fib_naive(n-2)

@lru_cache(maxsize=None)
def fib_memo(n):
    if n<=1: return n
    return fib_memo(n-1)+fib_memo(n-2)

def fib_bottom_up(n):
    if n<=1: return n
    dp = [0]*(n+1); dp[1]=1
    for i in range(2,n+1): dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

def fib_optimal(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

if __name__=="__main__":
    methods = [
        ("Naive O(2^n)    ", fib_naive, 30),
        ("Memoized O(n)   ", fib_memo, 40),
        ("Bottom-Up O(n)  ", fib_bottom_up, 40),
        ("Optimal O(1)spc ", fib_optimal, 40),
    ]
    for name, fn, n in methods:
        t = time.perf_counter()
        r = fn(n)
        print(f"{name} fib({n})={r}  ({time.perf_counter()-t:.5f}s)")
