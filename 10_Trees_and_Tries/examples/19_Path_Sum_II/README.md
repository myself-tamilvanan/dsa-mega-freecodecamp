# Path Sum II (LeetCode #113)

## Problem
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values equals targetSum.

## Examples
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Input: root = [1,2,3], targetSum = 5
Output: []

## Constraints
- Number of nodes: [0, 5000]
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000

## Approach
DFS backtracking: track current path. When we reach a leaf with remaining sum == 0, record path.

## Complexity
- Time: O(N^2) worst case (copying paths)
- Space: O(N) for recursion stack
