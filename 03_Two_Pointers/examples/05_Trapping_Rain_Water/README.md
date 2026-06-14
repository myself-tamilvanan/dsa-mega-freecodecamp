# Example 05: Trapping Rain Water (LC 42)

## Problem
Given elevation map, compute total water trapped.

## Input
height = [0,1,0,2,1,0,1,3,2,1,2,1]
## Output
6

## Approach
Two pointers. Water at position = min(left_max, right_max) - height.
**Time: O(n)  Space: O(1)**