# Example 05: N-Queens (LC 51)

## Problem
Place n queens on n×n board so none attacks another. Return all solutions.

## Input
n = 4
## Output
[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

## Approach
Backtrack row by row. Use sets for cols, diagonals to check attacks in O(1).
**Time: O(n!)  Space: O(n)**