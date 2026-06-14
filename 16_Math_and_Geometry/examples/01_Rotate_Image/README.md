# Example 01: Rotate Image (LC 48)

## Problem
Rotate n×n matrix 90° clockwise in-place.

## Input
[[1,2,3],[4,5,6],[7,8,9]]
## Output
[[7,4,1],[8,5,2],[9,6,3]]

## Trick
Step 1: Transpose (swap matrix[i][j] with matrix[j][i]).
Step 2: Reverse each row.
**Time: O(n²)  Space: O(1)**