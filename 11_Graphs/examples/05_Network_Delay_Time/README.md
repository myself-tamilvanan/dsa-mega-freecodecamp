# Example 05: Network Delay Time (LC 743)

## Problem
Find the minimum time for all nodes to receive a signal sent from node k.

## Input
times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2
## Output
2

## Approach
Dijkstra's algorithm from source k.
**Time: O(E log V)  Space: O(V+E)**