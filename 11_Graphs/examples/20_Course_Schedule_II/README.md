# Course Schedule II (LeetCode #210)

## Problem
There are numCourses courses (0 to numCourses-1). Given prerequisites[i] = [ai, bi] meaning you must take course bi first to take ai. Return the ordering of courses to finish all. If impossible, return [].

## Examples
Input: numCourses=2, prerequisites=[[1,0]] → Output: [0,1]
Input: numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]] → Output: [0,2,1,3] or [0,1,2,3]
Input: numCourses=1, prerequisites=[] → Output: [0]

## Constraints
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= numCourses*(numCourses-1)

## Approach
Topological sort (Kahn's BFS): build in-degree map, process nodes with in-degree 0, reduce neighbors' in-degrees. If order contains all courses, return it.

## Complexity
- Time: O(V + E)
- Space: O(V + E)
