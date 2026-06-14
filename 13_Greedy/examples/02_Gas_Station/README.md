# Example 02: Gas Station (LC 134)

## Problem
Find starting gas station to complete circular route, or return -1.

## Input
gas=[1,2,3,4,5], cost=[3,4,5,1,2]
## Output
3

## Key Insight
If total gas >= total cost, a solution exists. Start from where running sum went negative.
**Time: O(n)  Space: O(1)**