# Example 02: Clone Graph (LC 133)

## Problem
Deep copy a connected undirected graph.

## Input
Node with val=1, neighbors=[2,4]; Node 2 neighbors=[1,3]; etc.
## Output
A new graph with the same structure.

## Approach
BFS/DFS with HashMap {original → clone}.
**Time: O(V+E)  Space: O(V)**