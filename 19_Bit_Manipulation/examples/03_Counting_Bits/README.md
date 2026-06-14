# Example 03: Counting Bits (LC 338)

## Problem
For every number 0..n, count its set bits. Return as array.

## Input
n = 5
## Output
[0,1,1,2,1,2]

## Key DP Relation
dp[i] = dp[i >> 1] + (i & 1)
(right shift = divide by 2; add 1 if odd)
**Time: O(n)  Space: O(n)**