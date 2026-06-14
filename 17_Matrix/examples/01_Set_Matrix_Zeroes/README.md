# Example 01: Set Matrix Zeroes (LC 73)

## Problem
If an element is 0, set its entire row and column to 0. In-place.

## Input
[[1,1,1],[1,0,1],[1,1,1]]
## Output
[[1,0,1],[0,0,0],[1,0,1]]

## Trick
Use first row/column as markers. Track separately if first row/col need zeroing.
**Time: O(m×n)  Space: O(1)**