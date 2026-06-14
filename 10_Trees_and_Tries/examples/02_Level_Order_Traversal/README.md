# Example 02: Binary Tree Level Order Traversal (LC 102)

## Problem
Return level-order traversal as list of lists.

## Input
Tree: [3,9,20,null,null,15,7]
## Output
[[3],[9,20],[15,7]]

## Approach
BFS with queue. At each level, process all nodes currently in queue.
**Time: O(n)  Space: O(n)**