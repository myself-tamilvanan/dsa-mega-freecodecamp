# Example 01: Subsets (LC 78)

## Problem
Return all possible subsets (the power set) of nums.

## Input
nums = [1,2,3]
## Output
[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

## Approach
Backtracking: at each index, choose to include or skip.
**Time: O(2^n × n)  Space: O(n)**