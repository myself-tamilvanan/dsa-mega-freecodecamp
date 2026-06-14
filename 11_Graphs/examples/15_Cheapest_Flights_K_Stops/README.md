# Example 15: Cheapest Flights Within K Stops (LC 787)
## Problem
Find cheapest price from src to dst with at most k stops.
## Input
n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src=0, dst=3, k=1 → 700
## Approach
Bellman-Ford for k+1 iterations, or Dijkstra with (cost,stops) state.
**Time: O(k×E)  Space: O(n)**