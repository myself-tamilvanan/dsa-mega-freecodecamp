# Example 03: Validate Binary Search Tree (LC 98)

## Problem
Determine if a binary tree is a valid BST.

## Input
Tree: [2,1,3]
## Output
True

## Approach
Pass valid range (min, max) at each node. DFS with bounds.
**Time: O(n)  Space: O(h)**