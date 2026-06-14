# Example 06: Binary Tree Maximum Path Sum (LC 124)

## Problem
Find the maximum path sum. A path can start and end at any node.

## Input
Tree: [-10,9,20,null,null,15,7]
## Output
42 (path: 15 → 20 → 7)

## Key Insight
At each node, best contribution up = node.val + max(left, right, 0).
Best path through node = node.val + max(left,0) + max(right,0).
**Time: O(n)  Space: O(h)**