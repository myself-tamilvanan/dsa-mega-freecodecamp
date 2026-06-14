# Minimum Interval to Include Each Query (LeetCode #1851)

## Problem
Given intervals and queries, for each query find the smallest interval [l,r] that contains query (l<=query<=r). Return array of answers (-1 if no interval).

## Examples
Input: intervals=[[1,4],[2,4],[3,6],[4,4]], queries=[2,3,4,5] → Output: [3,3,1,4]
Input: intervals=[[2,3],[2,5],[1,8],[20,25]], queries=[2,19,5,22] → Output: [2,-1,4,6]

## Approach
Sort both queries and intervals. Use min-heap sorted by interval size. Process queries in order, add intervals that start ≤ query, pop intervals that end < query.

## Complexity
- Time: O((n+q) log n), Space: O(n+q)
