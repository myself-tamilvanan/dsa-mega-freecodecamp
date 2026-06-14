# Example 07: Roman to Integer (LC 13)

## Problem
Convert a Roman numeral string to an integer.

## Roman Numeral Rules
- I=1, V=5, X=10, L=50, C=100, D=500, M=1000
- If a smaller value precedes a larger one, subtract it (IV=4, IX=9, XL=40, etc.)

## Input
s = "MCMXCIV"
## Output
1994

## Approach
Iterate right to left. If current value < previous, subtract; else add.
**Time: O(1) — bounded by 15 chars  Space: O(1)**