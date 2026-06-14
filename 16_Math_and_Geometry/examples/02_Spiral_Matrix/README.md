# Example 02: Spiral Matrix (LC 54)

## Problem
Return all elements of the matrix in spiral order.

## Input
[[1,2,3],[4,5,6],[7,8,9]]
## Output
[1,2,3,6,9,8,7,4,5]

## Approach
Four boundaries (left, right, top, bottom). Shrink after each direction.
**Time: O(m×n)  Space: O(1)**