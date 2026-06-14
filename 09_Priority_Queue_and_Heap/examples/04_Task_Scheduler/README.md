# Example 04: Task Scheduler (LC 621)

## Problem
Given tasks and cooldown n, find minimum time to finish all tasks.

## Input
tasks = ["A","A","A","B","B","B"], n = 2
## Output
8

## Key Insight
Always execute the most frequent remaining task. Use max-heap + cooldown queue.
**Time: O(m log m)  Space: O(m)** where m = unique tasks