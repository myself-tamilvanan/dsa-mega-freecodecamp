# Example 01: Number of Islands (LC 200)

## Problem
Count the number of islands (connected groups of '1's) in a 2D binary grid.

## Input
grid = [["1","1","0"],["0","1","0"],["0","0","1"]]
## Output
2

## Approach
BFS/DFS flood fill. Mark visited cells as '0'.
**Time: O(m×n)  Space: O(m×n)**