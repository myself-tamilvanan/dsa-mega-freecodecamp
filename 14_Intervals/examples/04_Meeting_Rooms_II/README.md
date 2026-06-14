# Example 04: Meeting Rooms II (LC 253)

## Problem
Find minimum number of conference rooms required.

## Input
[[0,30],[5,10],[15,20]]
## Output
2

## Approach
Sort by start. Use min-heap of end times. If room is free (heap top ≤ start), reuse it.
**Time: O(n log n)  Space: O(n)**