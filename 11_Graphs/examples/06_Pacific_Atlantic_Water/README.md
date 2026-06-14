# Example 06: Pacific Atlantic Water Flow (LC 417)

## Problem
Find cells from which water can flow to BOTH Pacific and Atlantic oceans.

## Approach
Reverse thinking: BFS/DFS from ocean borders inward (water flows uphill in reverse).
**Time: O(m×n)  Space: O(m×n)**