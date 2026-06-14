# Maximal Square (LeetCode #221)

## Problem
Given an m x n binary matrix, find the largest square containing only 1s and return its area.

## Examples
Input: matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] → Output: 4
Input: matrix=[["0","1"],["1","0"]] → Output: 1

## Approach
DP: dp[i][j] = side length of largest square with bottom-right at (i,j).
If matrix[i][j]=='1': dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

## Complexity
- Time: O(m*n), Space: O(m*n)
