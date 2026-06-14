# Example 04: Container With Most Water (LC 11)

## Problem
Find two lines that hold the most water together.

## Input
height = [1,8,6,2,5,4,8,3,7]
## Output
49

## Approach
Two pointers. Always move the shorter side inward (moving taller never helps).
**Time: O(n)  Space: O(1)**