# Example 06: Unique Paths (LC 62)

## Problem
Robot in m×n grid, starts top-left, ends bottom-right. Only right or down moves. Count paths.

## Input
m=3, n=7
## Output
28

## Approach
DP: dp[i][j] = dp[i-1][j] + dp[i][j-1]. Space-optimize to 1D array.
**Time: O(m×n)  Space: O(n)**