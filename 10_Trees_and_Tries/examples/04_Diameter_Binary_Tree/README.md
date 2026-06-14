# Example 04: Diameter of Binary Tree (LC 543)

## Problem
Return the length of the longest path between any two nodes.

## Input
Tree: [1,2,3,4,5]
## Output
3 (path: 4->2->1->3 or 5->2->1->3)

## Key Insight
At each node: diameter candidate = left_depth + right_depth.
**Time: O(n)  Space: O(h)**