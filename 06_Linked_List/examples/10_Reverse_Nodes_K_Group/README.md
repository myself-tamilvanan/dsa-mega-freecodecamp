# Example 10: Reverse Nodes in K-Group (LC 25)

## Problem
Reverse every k nodes in the linked list. Remaining nodes (< k) stay as-is.

## Input
head=[1,2,3,4,5], k=2
## Output
[2,1,4,3,5]

## Approach
Count k nodes, reverse them, connect to recursively processed rest.
**Time: O(n)  Space: O(n/k) recursion**