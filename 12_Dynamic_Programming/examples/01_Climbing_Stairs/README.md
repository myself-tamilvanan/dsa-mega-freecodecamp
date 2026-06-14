# Example 01: Climbing Stairs (LC 70)

## Problem
You can climb 1 or 2 steps at a time. How many ways to reach step n?

## Input
n = 5
## Output
8

## Pattern
Fibonacci! dp[n] = dp[n-1] + dp[n-2]

## Variations
- Can climb 1,2,3 steps: dp[n] = dp[n-1]+dp[n-2]+dp[n-3]
- With cost (LC 746)
**Time: O(n)  Space: O(1)**