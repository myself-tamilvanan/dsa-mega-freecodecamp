# Example 03: Combination Sum (LC 39)

## Problem
Find all combinations that sum to target. Same number can be used multiple times.

## Input
candidates = [2,3,6,7], target = 7
## Output
[[2,2,3],[7]]

## Approach
Backtracking. Start index stays at i (allow reuse), not i+1.
**Time: O(n^(t/m))  Space: O(t/m)**