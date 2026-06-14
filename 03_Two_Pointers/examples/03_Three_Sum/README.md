# Example 03: 3Sum (LC 15)

## Problem
Find all unique triplets that sum to zero.

## Input
nums = [-1,0,1,2,-1,-4]
## Output
[[-1,-1,2],[-1,0,1]]

## Approach
Sort, then for each element use two-pointer on the rest. Skip duplicates.
**Time: O(n²)  Space: O(1)**