# Example 04: Word Search (LC 79)

## Problem
Find if word exists in 2D grid of characters.

## Input
board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCED"
## Output
True

## Approach
DFS + backtracking. Mark cell visited by replacing with '#', restore after.
**Time: O(m×n×4^L)  Space: O(L)**