# Example 05: Edit Distance (LC 72)

## Problem
Minimum operations (insert, delete, replace) to convert word1 to word2.

## Input
word1 = "horse", word2 = "ros"
## Output
3

## Recurrence
- If chars match: dp[i][j] = dp[i-1][j-1]
- Else: dp[i][j] = 1 + min(replace, delete, insert)
**Time: O(m×n)  Space: O(min(m,n))**