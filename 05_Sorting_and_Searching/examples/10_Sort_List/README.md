# Example 10: Sort List (LC 148)

## Problem
Sort a linked list in O(n log n) time using O(1) memory.

## Input
head = [4,2,1,3]
## Output
[1,2,3,4]

## Approach
Merge sort: find middle (slow/fast), split, sort halves, merge.
**Time: O(n log n)  Space: O(log n) recursion stack**