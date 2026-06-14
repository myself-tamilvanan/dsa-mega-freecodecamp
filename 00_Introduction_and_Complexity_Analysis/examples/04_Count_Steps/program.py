"""Count Algorithm Steps for Each Complexity"""
import math

def steps_table(ns):
    print(f"{'n':>8} {'O(1)':>6} {'O(log n)':>10} {'O(n)':>8} {'O(n log n)':>12} {'O(n^2)':>10}")
    print("-"*60)
    for n in ns:
        o1 = 1
        ologn = round(math.log2(n))
        on = n
        onlogn = round(n * math.log2(n))
        on2 = n*n
        print(f"{n:>8} {o1:>6} {ologn:>10} {on:>8} {onlogn:>12} {on2:>10}")

if __name__=="__main__":
    print("=== Step Count Table ===\n")
    steps_table([10, 100, 1000, 10000, 100000])
    print("\nAt n=100000:")
    print(f"  O(n log n): {100000*round(math.log2(100000)):,} steps")
    print(f"  O(n²):      {100000**2:,} steps  ← 1 billion times more!")
