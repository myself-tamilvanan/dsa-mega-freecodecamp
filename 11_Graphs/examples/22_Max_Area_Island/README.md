# Max Area of Island (LeetCode #695)

## Problem
Given m x n binary grid (0=water, 1=land), return the maximum area of an island (connected 1s). Return 0 if no island.

## Examples
Input: grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],...] → Output: 6
Input: grid=[[0,0,0,0,0,0,0,0]] → Output: 0

## Constraints
- m == grid.length, n == grid[i].length
- 1 <= m, n <= 50, grid[i][j] is 0 or 1

## Approach
DFS: for each unvisited land cell, DFS to count connected cells and mark visited. Track maximum.

## Complexity
- Time: O(m*n), Space: O(m*n)
