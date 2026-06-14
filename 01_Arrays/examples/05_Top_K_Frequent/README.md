# Example 05: Top K Frequent Elements (LC 347)

## Problem
Given integer array and k, return k most frequent elements.

## Input
nums = [1,1,1,2,2,3], k = 2
## Output
[1, 2]

## Approaches
1. Sort by frequency — O(n log n)
2. Min-heap of size k — O(n log k)
3. Bucket sort — O(n) optimal

**Time: O(n)  Space: O(n)** (bucket sort)