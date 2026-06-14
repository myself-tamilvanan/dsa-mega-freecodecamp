# Example 12: Count Good Nodes in Binary Tree (LC 1448)
## Problem
A node X is good if no node on path from root to X has value greater than X.val.
## Input
[3,1,4,3,null,1,5] → 4
## Approach
DFS passing max value seen so far. Count node if node.val >= max_so_far.
**Time: O(n)  Space: O(h)**