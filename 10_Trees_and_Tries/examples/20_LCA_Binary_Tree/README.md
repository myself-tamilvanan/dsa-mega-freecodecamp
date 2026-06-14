# Lowest Common Ancestor of a Binary Tree (LeetCode #236)

## Problem
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p and q.
LCA is the lowest node that has both p and q as descendants (a node can be a descendant of itself).

## Examples
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 → Output: 3
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4 → Output: 5

## Constraints
- 2 <= number of nodes <= 10^5
- All Node.val are unique
- p != q, both p and q exist in the tree

## Approach
Recursive DFS: if current node is p or q, return it. If both children return non-null, current node is LCA. Otherwise return the non-null child.

## Complexity
- Time: O(N)
- Space: O(N) recursion stack
