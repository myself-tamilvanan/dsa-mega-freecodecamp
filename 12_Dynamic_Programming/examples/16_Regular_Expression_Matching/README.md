# Regular Expression Matching (LeetCode #10)

## Problem
Given input string s and pattern p, implement regular expression matching with '.' and '*'.
'.' matches any single character. '*' matches zero or more of the preceding element.

## Examples
Input: s="aa", p="a" → Output: false
Input: s="aa", p="a*" → Output: true
Input: s="ab", p=".*" → Output: true

## Approach
2D DP: dp[i][j] = does s[:i] match p[:j]? Handle '*' by checking zero occurrences (dp[i][j-2]) or one+ occurrences.

## Complexity
- Time: O(m*n), Space: O(m*n)
