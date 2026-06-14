# Example 10: Binary Tree Right Side View (LC 199)
## Problem
Return values visible from the right side of the tree (last node at each level).
## Input
[1,2,3,null,5,null,4]
## Output
[1,3,4]
## Approach
BFS level-order: take last element of each level.
**Time: O(n)  Space: O(n)**