# Example 05: Find Median from Data Stream (LC 295)

## Problem
Design a data structure that supports addNum and findMedian.

## Approach
Two heaps:
- small = max-heap (lower half)
- large = min-heap (upper half)

Keep sizes balanced: len(small) == len(large) or len(small) == len(large)+1
**Time: O(log n) add, O(1) findMedian  Space: O(n)**