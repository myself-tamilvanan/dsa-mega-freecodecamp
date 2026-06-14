# Example 07: Number of Provinces (LC 547)
## Problem
Given adjacency matrix isConnected[i][j], find number of provinces (connected components).
## Input
isConnected=[[1,1,0],[1,1,0],[0,0,1]] → 2
## Approach
DFS/Union-Find. Mark visited nodes, count DFS starts.
**Time: O(n²)  Space: O(n)**