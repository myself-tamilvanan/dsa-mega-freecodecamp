# Word Break (LeetCode #139)

## Problem
Given string s and list wordDict, return true if s can be segmented into space-separated sequence of dictionary words.

## Examples
Input: s="leetcode", wordDict=["leet","code"] → Output: true
Input: s="applepenapple", wordDict=["apple","pen"] → Output: true
Input: s="catsandog", wordDict=["cats","dog","sand","and","cat"] → Output: false

## Constraints
- 1 <= s.length <= 300, 1 <= wordDict.length <= 1000

## Approach
DP: dp[i] = can s[:i] be segmented. dp[0]=True. For each i, check if dp[j] and s[j:i] in wordSet.

## Complexity
- Time: O(n^2), Space: O(n)
