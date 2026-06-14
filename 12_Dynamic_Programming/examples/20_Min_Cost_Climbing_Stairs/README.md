# Min Cost Climbing Stairs (LeetCode #746)

## Problem
Given cost array where cost[i] is cost of step i, return minimum cost to reach top. You can start from step 0 or 1, and take 1 or 2 steps.

## Examples
Input: cost=[10,15,20] → Output: 15 (start at index 1, pay 15, jump to top)
Input: cost=[1,100,1,1,1,100,1,1,100,1] → Output: 6

## Approach
DP: dp[i] = min cost to reach step i. dp[i] = cost[i] + min(dp[i-1], dp[i-2]).

## Complexity
- Time: O(n), Space: O(1)
