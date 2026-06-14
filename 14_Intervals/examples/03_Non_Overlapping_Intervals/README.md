# Example 03: Non-Overlapping Intervals (LC 435)

## Problem
Minimum number of intervals to remove so none overlap.

## Input
[[1,2],[2,3],[3,4],[1,3]]
## Output
1 (remove [1,3])

## Approach
Sort by end time. Greedily keep intervals with earliest end time.
**Time: O(n log n)  Space: O(1)**