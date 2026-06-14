# Example 08: Majority Element (LC 169)

## Problem
Find element that appears more than n/2 times. Always exists.

## Input
nums = [2,2,1,1,1,2,2]
## Output
2

## Approach (Boyer-Moore Voting)
Candidate with count: +1 for same, -1 for different. Surviving candidate wins.
**Time: O(n)  Space: O(1)**