# Binary Tree Zigzag Level Order Traversal (LeetCode #103)

## Problem
Given root of binary tree, return zigzag level order traversal: left-to-right, then right-to-left, alternating.

## Examples
Input: root=[3,9,20,null,null,15,7] → Output: [[3],[20,9],[15,7]]
Input: root=[1] → Output: [[1]]
Input: root=[] → Output: []

## Approach
BFS level by level. Use a flag to reverse direction for alternate levels.

## Complexity
- Time: O(N), Space: O(N)
