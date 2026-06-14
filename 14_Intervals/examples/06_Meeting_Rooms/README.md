# Meeting Rooms (LeetCode #252)

## Problem
Given array of meeting time intervals [start, end], determine if a person could attend all meetings (no overlaps).

## Examples
Input: intervals=[[0,30],[5,10],[15,20]] → Output: false
Input: intervals=[[7,10],[2,4]] → Output: true

## Approach
Sort by start time. Check if any meeting starts before previous one ends.

## Complexity
- Time: O(n log n), Space: O(1)
