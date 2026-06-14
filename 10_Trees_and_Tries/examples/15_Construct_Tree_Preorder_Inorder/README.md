# Example 15: Construct Binary Tree from Preorder and Inorder (LC 105)
## Problem
Rebuild binary tree given preorder and inorder traversal arrays.
## Input
preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]
## Output
Tree [3,9,20,null,null,15,7]
## Approach
preorder[0] = root. Find root in inorder to split left/right subtrees.
**Time: O(n)  Space: O(n)**