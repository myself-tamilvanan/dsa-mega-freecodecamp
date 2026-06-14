# Example 13: Lowest Common Ancestor of BST (LC 235)
## Problem
Find LCA of two nodes in a BST.
## Input
BST root=[6,2,8,0,4,7,9], p=2, q=8 → 6
## Approach
BST property: if both p,q < root → go left; if both > root → go right; else root is LCA.
**Time: O(h)  Space: O(1)**