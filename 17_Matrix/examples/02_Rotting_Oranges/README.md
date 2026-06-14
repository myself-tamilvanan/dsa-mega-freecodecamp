# Example 02: Rotting Oranges (LC 994)

## Problem
All fresh oranges adjacent to rotten become rotten each minute. Find minimum minutes.

## Input
[[2,1,1],[1,1,0],[0,1,1]]
## Output
4

## Approach
Multi-source BFS from ALL rotten oranges simultaneously.
**Time: O(m×n)  Space: O(m×n)**