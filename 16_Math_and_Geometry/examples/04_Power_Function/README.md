# Example 04: Pow(x, n) (LC 50)

## Problem
Implement pow(x, n) efficiently.

## Input
x=2.0, n=10 → 1024.0
x=2.0, n=-2 → 0.25

## Approach
Fast exponentiation (exponentiation by squaring):
- n even: x^n = (x²)^(n/2)
- n odd:  x^n = x × (x²)^((n-1)/2)
**Time: O(log n)  Space: O(1)**