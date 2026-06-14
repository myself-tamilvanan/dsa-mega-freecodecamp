# Chapter 14: Intervals
Sort by start time. Two intervals [a,b],[c,d] overlap if a<=d AND c<=b.

## Patterns
- **Merge**: sort by start, greedily extend end
- **Insert**: find overlap range, merge all touched
- **Min rooms / conflicts**: sort + min-heap of end times
- **Min removals**: sort by end, keep greedy non-overlapping

## LeetCode Problems
LC 56 Merge Intervals, LC 57 Insert Interval, LC 435 Non-overlapping,
LC 252 Meeting Rooms, LC 253 Meeting Rooms II
