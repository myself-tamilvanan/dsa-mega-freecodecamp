# Example 09: Merge K Sorted Lists (LC 23)

## Problem
Merge k sorted linked lists into one sorted list.

## Input
lists=[[1,4,5],[1,3,4],[2,6]]
## Output
[1,1,2,3,4,4,5,6]

## Approaches
1. Min-heap of (val, list_index) — O(n log k)
2. Divide and conquer merge pairs — O(n log k)
**Time: O(n log k)  Space: O(k)**