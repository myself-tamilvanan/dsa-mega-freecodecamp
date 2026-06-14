# Longest Increasing Path in a Matrix (LeetCode #329)

## Problem
Given an m x n integers matrix, return the length of the longest increasing path. 
From each cell, you can move in 4 directions. You may NOT move diagonally or outside the boundary.

## Examples
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]] → Output: 4 (path: 1→2→6→9)
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]] → Output: 4 (path: 3→4→5→6)

## Constraints
- m == matrix.length, n == matrix[i].length
- 1 <= m, n <= 200
- 0 <= matrix[i][j] <= 2^31 - 1

## Approach
DFS + memoization. For each cell, DFS to find the longest increasing path starting from it. Cache results.

## Complexity
- Time: O(m*n) with memoization
- Space: O(m*n)
