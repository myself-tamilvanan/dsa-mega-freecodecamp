# Example 18: Alien Dictionary (LC 269)
## Problem
Given sorted alien language word list, derive character ordering.
## Input
words=["wrt","wrf","er","ett","rftt"] → "wertf"
## Approach
Build directed graph from adjacent word comparisons. Topological sort (BFS/Kahn's).
**Time: O(N+V+E)  Space: O(V+E)**