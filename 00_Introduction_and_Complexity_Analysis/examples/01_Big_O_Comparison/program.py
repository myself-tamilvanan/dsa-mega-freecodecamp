"""Big O Runtime Comparison"""
import time, random

def time_it(fn, *args):
    start = time.perf_counter()
    result = fn(*args)
    return time.perf_counter() - start, result

def o1(arr): return arr[0]
def ologn(arr, t):
    l,r=0,len(arr)-1
    while l<=r:
        m=(l+r)//2
        if arr[m]==t: return m
        elif arr[m]<t: l=m+1
        else: r=m-1
    return -1
def on(arr, t): return next((i for i,v in enumerate(arr) if v==t), -1)
def on2(arr): return sum(arr[i]+arr[j] for i in range(len(arr)) for j in range(i+1,len(arr)))
def onlogn(arr): return sorted(arr)

if __name__ == "__main__":
    n = 2000
    arr = list(range(n))
    target = n - 1
    print(f"n = {n}")
    for name, fn, args in [
        ("O(1)     ", o1, (arr,)),
        ("O(log n) ", ologn, (arr, target)),
        ("O(n)     ", on, (arr, target)),
        ("O(n log n)", onlogn, (arr,)),
        ("O(n²)   ", on2, (arr[:200],)),
    ]:
        t, _ = time_it(fn, *args)
        print(f"  {name}: {t:.6f}s")
