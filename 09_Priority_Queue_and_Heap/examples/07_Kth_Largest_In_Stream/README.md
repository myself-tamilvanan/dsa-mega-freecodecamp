# Example 07: Kth Largest Element in a Stream (LC 703)

## Problem
Design class that finds kth largest in a stream of integers.

## Operations
- KthLargest(k, nums) — constructor
- add(val) — add val to stream, return kth largest

## Approach
Maintain min-heap of size k. Heap top = kth largest.
**Time: O(log k) per add  Space: O(k)**