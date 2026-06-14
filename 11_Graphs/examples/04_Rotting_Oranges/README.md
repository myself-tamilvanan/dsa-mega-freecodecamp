# Example 04: Rotting Oranges (LC 994)

## Problem
Find minimum minutes until all fresh oranges are rotten. -1 if impossible.

## Input
grid = [[2,1,1],[1,1,0],[0,1,1]]
## Output
4

## Approach
Multi-source BFS starting from all rotten oranges simultaneously.
**Time: O(m×n)  Space: O(m×n)**