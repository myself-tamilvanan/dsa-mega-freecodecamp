# Example 08: Number of Connected Components (LC 323)
## Problem
Count connected components in undirected graph with n nodes and edges list.
## Input
n=5, edges=[[0,1],[1,2],[3,4]] → 2
## Approach
Union-Find. Each union reduces component count.
**Time: O(n+e*α(n))  Space: O(n)**