# Example 06: Longest Consecutive Sequence (LC 128)

## Problem
Find the length of the longest consecutive elements sequence in O(n).

## Input
nums = [100,4,200,1,3,2]
## Output
4 (sequence: 1,2,3,4)

## Approach
Add all to a set. Only start counting from n where n-1 is NOT in set.
**Time: O(n)  Space: O(n)**