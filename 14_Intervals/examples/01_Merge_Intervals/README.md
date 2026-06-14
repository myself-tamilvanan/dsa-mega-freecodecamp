# Example 01: Merge Intervals (LC 56)

## Problem
Merge all overlapping intervals.

## Input
[[1,3],[2,6],[8,10],[15,18]]
## Output
[[1,6],[8,10],[15,18]]

## Approach
Sort by start. If current start <= last merged end → extend end.
**Time: O(n log n)  Space: O(n)**