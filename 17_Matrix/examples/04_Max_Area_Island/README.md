# Example 04: Max Area of Island (LC 695)

## Problem
Find the maximum area of an island (group of connected 1s).

## Input
[[0,0,1,0,0],[0,1,1,0,1],[0,1,0,0,1]]
## Output
4

## Approach
DFS flood fill. Count cells in each island, track max.
**Time: O(m×n)  Space: O(m×n)**