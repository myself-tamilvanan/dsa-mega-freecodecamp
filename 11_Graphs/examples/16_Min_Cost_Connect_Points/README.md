# Example 16: Minimum Cost to Connect All Points (LC 1584)
## Problem
Find minimum cost to connect all points where cost=Manhattan distance. (MST)
## Input
points=[[0,0],[2,2],[3,10],[5,2],[7,0]] → 20
## Approach
Prim's algorithm: greedily add closest unvisited point.
**Time: O(n² log n)  Space: O(n)**