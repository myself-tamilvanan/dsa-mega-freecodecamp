# Example 06: Remove Duplicates From Sorted Array (LC 26)

## Problem
Remove duplicates in-place from sorted array. Return new length k. First k elements must be unique.

## Input
nums = [0,0,1,1,1,2,2,3,3,4]
## Output
5 (nums = [0,1,2,3,4,...])

## Approach
Slow/fast two pointers. slow tracks last unique position.
**Time: O(n)  Space: O(1)**