# Combination Sum II (LeetCode #40)

## Problem
Given candidates (may have duplicates) and target, find all unique combinations that sum to target. Each number may only be used once.

## Examples
Input: candidates=[10,1,2,7,6,1,5], target=8 → Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
Input: candidates=[2,5,2,1,2], target=5 → Output: [[1,2,2],[5]]

## Approach
Sort + backtracking. Skip duplicates at same level. Add each candidate at most once per branch.

## Complexity
- Time: O(2^n), Space: O(n)
