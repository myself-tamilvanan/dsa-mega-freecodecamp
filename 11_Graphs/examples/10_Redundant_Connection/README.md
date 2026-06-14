# Example 10: Redundant Connection (LC 684)
## Problem
Find the last edge that created a cycle in an undirected graph.
## Input
edges=[[1,2],[1,3],[2,3]] → [2,3]
## Approach
Union-Find: process edges in order. First edge where both nodes already connected = redundant.
**Time: O(n*α(n))  Space: O(n)**