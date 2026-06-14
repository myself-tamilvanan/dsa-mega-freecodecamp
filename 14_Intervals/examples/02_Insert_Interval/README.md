# Example 02: Insert Interval (LC 57)

## Problem
Insert newInterval into sorted non-overlapping intervals, merge if needed.

## Input
intervals=[[1,3],[6,9]], newInterval=[2,5]
## Output
[[1,5],[6,9]]

## Approach
Three phases: add before, merge overlapping, add after.
**Time: O(n)  Space: O(n)**