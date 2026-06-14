# Example 11: Flatten Binary Tree to Linked List (LC 114)

## Problem
Flatten a binary tree into a linked list in-place following preorder traversal.

## Input
Tree: [1,2,5,3,4,null,6]
## Output
1->2->3->4->5->6

## Approach
For each node: move left subtree between node and node.right, then recurse.
**Time: O(n)  Space: O(1)**