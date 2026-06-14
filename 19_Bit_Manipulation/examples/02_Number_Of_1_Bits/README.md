# Example 02: Number of 1 Bits / Hamming Weight (LC 191)

## Problem
Count the number of '1' bits in the binary representation.

## Input
n = 11 (binary: 1011)
## Output
3

## Tricks
- n & (n-1) removes the lowest set bit
- Python: bin(n).count('1') — but understand the manual way!
**Time: O(k) where k=set bits  Space: O(1)**