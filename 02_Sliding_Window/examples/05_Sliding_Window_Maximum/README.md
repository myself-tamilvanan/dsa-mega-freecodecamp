# Example 05: Sliding Window Maximum (LC 239)

## Problem
Return max of every contiguous subarray of size k.

## Input
nums = [1,3,-1,-3,5,3,6,7], k = 3
## Output
[3,3,5,5,6,7]

## Approach
Monotonic deque: maintain indices in decreasing order of values.
**Time: O(n)  Space: O(k)**