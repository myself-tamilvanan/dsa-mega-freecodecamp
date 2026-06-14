# Bitwise AND of Numbers Range (LeetCode #201)

## Problem
Given [left, right], return the bitwise AND of all numbers in that range (inclusive).

## Examples
Input: left=5, right=7 → Output: 4 (5=101, 6=110, 7=111 → 100=4)
Input: left=0, right=0 → Output: 0
Input: left=1, right=2147483647 → Output: 0

## Approach
Find common prefix of left and right in binary. Shift both right until equal, then shift back.

## Complexity
- Time: O(log n), Space: O(1)
