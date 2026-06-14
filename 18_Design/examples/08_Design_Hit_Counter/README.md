# Design Hit Counter (LeetCode #362)

## Problem
Design a hit counter which counts hits in the past 5 minutes (300 seconds).
- hit(timestamp): record a hit at given timestamp (in seconds)
- getHits(timestamp): return number of hits in past 5 minutes

## Approach
Use a deque. Remove old timestamps (> 300 seconds old) on each call.

## Complexity
- hit: O(1), getHits: O(n) amortized, Space: O(n)
