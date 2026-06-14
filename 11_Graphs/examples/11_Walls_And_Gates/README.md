# Example 11: Walls & Gates (LC 286)
## Problem
Fill each empty room with distance to nearest gate. -1=wall, 0=gate, INF=empty.
## Approach
Multi-source BFS from all gates simultaneously.
**Time: O(m×n)  Space: O(m×n)**