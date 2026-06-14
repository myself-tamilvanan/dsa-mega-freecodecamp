# Maximal Rectangle (LeetCode #85)

## Problem
Given rows x cols binary matrix filled with 0s and 1s, find the largest rectangle containing only 1s and return its area.

## Examples
Input: matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6

## Approach
For each row, compute height of consecutive 1s. Apply "Largest Rectangle in Histogram" on each row's heights.

## Complexity
- Time: O(m*n), Space: O(n)
