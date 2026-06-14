# Example 02: Kth Largest Element in an Array (LC 215)

## Problem
Find the kth largest element (not kth distinct).

## Input
nums = [3,2,1,5,6,4], k = 2
## Output
5

## Approaches
1. Min-heap of size k → O(n log k)
2. QuickSelect → O(n) average

**Time: O(n log k)  Space: O(k)**