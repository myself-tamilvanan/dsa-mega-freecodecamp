# Example 06: High Five (LC 1086)

## Problem
Given list of [student_id, score], return each student's top 5 average score.

## Input
items=[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[2,100],[1,87],[1,100]]
## Output
[[1,87],[2,93]] (averages of top 5)

## Approach
Min-heap of size 5 per student. Sum top 5 and divide.
**Time: O(n log 5) = O(n)  Space: O(n)**