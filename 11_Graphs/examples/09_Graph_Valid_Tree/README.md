# Example 09: Graph Valid Tree (LC 261)
## Problem
Given n nodes and edges, determine if they form a valid tree (connected + no cycle).
## Input
n=5, edges=[[0,1],[0,2],[0,3],[1,4]] → True
## Approach
Valid tree: n-1 edges AND connected. Use Union-Find: cycle detected if union returns False.
**Time: O(n*α(n))  Space: O(n)**