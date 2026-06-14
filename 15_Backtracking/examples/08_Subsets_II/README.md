# Subsets II (LeetCode #90)

## Problem
Given integer array nums that may contain duplicates, return all possible subsets (no duplicate subsets).

## Examples
Input: nums=[1,2,2] → Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Input: nums=[0] → Output: [[],[0]]

## Approach
Sort + backtracking. Skip duplicate elements at the same recursion level.

## Complexity
- Time: O(n * 2^n), Space: O(n)
