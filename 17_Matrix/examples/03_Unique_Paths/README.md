# Example 03: Unique Paths (LC 62)

## Problem
Count paths from top-left to bottom-right in m×n grid (only right/down moves).

## Input
m=3, n=7
## Output
28

## Approach
DP: dp[j] = dp[j] + dp[j-1]. Space-optimize to 1D array.
**Time: O(m×n)  Space: O(n)**