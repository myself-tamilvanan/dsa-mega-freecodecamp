# Middle of the Linked List (LeetCode #876)

## Problem
Given head of singly linked list, return the middle node. If two middle nodes, return the second one.

## Examples
Input: [1,2,3,4,5] → Output: node 3 ([3,4,5])
Input: [1,2,3,4,5,6] → Output: node 4 ([4,5,6])

## Constraints
- 1 <= number of nodes <= 100
- 1 <= Node.val <= 100

## Approach
Fast & slow pointer: fast moves 2 steps, slow moves 1 step. When fast reaches end, slow is at middle.

## Complexity
- Time: O(n), Space: O(1)
