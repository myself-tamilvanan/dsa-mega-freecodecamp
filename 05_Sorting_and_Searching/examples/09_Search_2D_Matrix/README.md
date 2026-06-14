# Example 09: Search a 2D Matrix (LC 74)

## Problem
Matrix where each row is sorted and first element of each row > last of previous row. Search for target.

## Input
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3
## Output
True

## Approach
Treat matrix as flat sorted array. Binary search with row/col conversion.
**Time: O(log(m×n))  Space: O(1)**