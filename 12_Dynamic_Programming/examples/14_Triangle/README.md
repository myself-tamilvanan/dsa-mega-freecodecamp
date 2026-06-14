# Triangle (LeetCode #120)

## Problem
Given a triangle array, return the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

## Examples
Input: triangle=[[2],[3,4],[6,5,7],[4,1,8,3]] → Output: 11 (path: 2→3→5→1)
Input: triangle=[[-10]] → Output: -10

## Approach
Bottom-up DP: start from the last row and work upward. dp[j] = min(dp[j], dp[j+1]) + triangle[i][j].

## Complexity
- Time: O(n^2), Space: O(n)
