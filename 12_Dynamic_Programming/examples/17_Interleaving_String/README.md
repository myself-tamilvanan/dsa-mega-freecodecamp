# Interleaving String (LeetCode #97)

## Problem
Given s1, s2, s3, return true if s3 is formed by interleaving s1 and s2.

## Examples
Input: s1="aabcc", s2="dbbca", s3="aadbbcbcac" → Output: true
Input: s1="aabcc", s2="dbbca", s3="aadbbbaccc" → Output: false

## Approach
2D DP: dp[i][j] = can s3[:i+j] be formed by interleaving s1[:i] and s2[:j].

## Complexity
- Time: O(m*n), Space: O(m*n)
