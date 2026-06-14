# Decode Ways (LeetCode #91)

## Problem
A message is encoded to numbers: 'A'→1, 'B'→2, ..., 'Z'→26. Given encoded string s, return the number of ways to decode it.

## Examples
Input: s="12" → Output: 2 (AB or L)
Input: s="226" → Output: 3 (BZ, VF, BBF)
Input: s="06" → Output: 0

## Approach
DP: dp[i] = ways to decode s[:i]. Single digit (1-9) adds dp[i-1]. Two digits (10-26) adds dp[i-2].

## Complexity
- Time: O(n), Space: O(n)
