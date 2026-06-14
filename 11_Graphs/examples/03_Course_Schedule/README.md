# Example 03: Course Schedule (LC 207)

## Problem
Can you finish all courses given prerequisites? (Detect cycle in directed graph)

## Input
numCourses=2, prerequisites=[[1,0]]
## Output
True

## Approach
Topological sort (Kahn's BFS). If all nodes processed → no cycle.
**Time: O(V+E)  Space: O(V+E)**