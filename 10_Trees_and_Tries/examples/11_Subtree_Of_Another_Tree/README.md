# Example 11: Subtree of Another Tree (LC 572)
## Problem
Given two binary trees root and subRoot, return true if subRoot is a subtree of root.
## Input
root=[3,4,5,1,2], subRoot=[4,1,2] → True
## Approach
At each node, check if subtree rooted there equals subRoot using isSameTree.
**Time: O(m×n)  Space: O(h)**