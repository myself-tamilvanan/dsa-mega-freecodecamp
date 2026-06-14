# Example 19: Swim in Rising Water (LC 778)
## Problem
At time t, every cell ≤ t is passable. Find minimum t to swim from top-left to bottom-right.
## Input
grid=[[0,2],[1,3]] → 3
## Approach
Dijkstra/Binary search + BFS. Min-heap: (max_elevation_so_far, r, c).
**Time: O(n² log n)  Space: O(n²)**