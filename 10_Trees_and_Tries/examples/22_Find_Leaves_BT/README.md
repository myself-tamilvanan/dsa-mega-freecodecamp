# Find Leaves of Binary Tree (LeetCode #366)

## Problem
Given root of binary tree, collect and remove leaves, then repeat until tree is empty. Return all leaf nodes in each step.

## Examples
Input: root=[1,2,3,4,5] → Output: [[4,5,3],[2],[1]]
Input: root=[1] → Output: [[1]]

## Constraints
- 1 <= number of nodes <= 100, -100 <= Node.val <= 100

## Approach
DFS: the "level" of a leaf is 0. For each node, its level = 1 + max(left level, right level).
Group nodes by their computed level.

## Complexity
- Time: O(N), Space: O(N)
