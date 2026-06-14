# Example 08: Employee Free Time (LC 759)

## Problem
Given schedules of employees (list of intervals), find free time common to ALL employees.

## Input
schedule=[[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
## Output
[[5,6],[7,9]]

## Approach
Flatten all intervals, sort, merge overlapping, find gaps between merged intervals.
**Time: O(n log n)  Space: O(n)**