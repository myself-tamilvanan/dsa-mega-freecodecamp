# Example 08: Symmetric Tree (LC 101)
## Problem
Check if a binary tree is a mirror of itself.
## Input
[1,2,2,3,4,4,3] → True
[1,2,2,null,3,null,3] → False
## Approach
Recursively check if left subtree mirrors right subtree.
**Time: O(n)  Space: O(h)**