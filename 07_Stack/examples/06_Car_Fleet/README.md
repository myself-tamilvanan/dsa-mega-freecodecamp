# Example 06: Car Fleet (LC 853)

## Problem
Cars drive to target. Faster car catching slower forms a fleet. Count fleets.

## Input
target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3]
## Output
3

## Approach
Sort by position descending. Stack: if arrival time <= top of stack, they merge.
**Time: O(n log n)  Space: O(n)**