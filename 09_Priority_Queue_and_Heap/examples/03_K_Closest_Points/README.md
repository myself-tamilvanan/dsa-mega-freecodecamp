# Example 03: K Closest Points to Origin (LC 973)

## Problem
Return k points closest to the origin.

## Input
points = [[1,3],[-2,2]], k = 1
## Output
[[-2,2]]

## Approach
Max-heap of size k storing (negative_distance, x, y).
**Time: O(n log k)  Space: O(k)**