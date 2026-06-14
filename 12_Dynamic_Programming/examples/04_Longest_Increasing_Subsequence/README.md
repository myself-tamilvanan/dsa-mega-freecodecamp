# Example 04: Longest Increasing Subsequence (LC 300)

## Problem
Find length of longest strictly increasing subsequence.

## Input
nums = [10,9,2,5,3,7,101,18]
## Output
4 ([2,3,7,101] or [2,5,7,101])

## Approaches
1. DP O(n²): dp[i] = max(dp[j]+1) for j<i where nums[j]<nums[i]
2. Patience Sorting O(n log n): binary search on tails array
**Time: O(n log n)  Space: O(n)**