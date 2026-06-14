# Longest Common Subsequence (LeetCode #1143)

## Problem
Given two strings text1 and text2, return the length of their longest common subsequence. If none, return 0.

## Examples
Input: text1="abcde", text2="ace" → Output: 3 (LCS: "ace")
Input: text1="abc", text2="abc" → Output: 3
Input: text1="abc", text2="def" → Output: 0

## Constraints
- 1 <= text1.length, text2.length <= 1000
- Only lowercase English characters

## Approach
2D DP: dp[i][j] = LCS of text1[:i] and text2[:j]. If chars match, dp[i][j] = dp[i-1][j-1]+1, else max of dp[i-1][j], dp[i][j-1].

## Complexity
- Time: O(m*n), Space: O(m*n)
