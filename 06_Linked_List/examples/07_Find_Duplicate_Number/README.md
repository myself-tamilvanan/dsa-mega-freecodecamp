# Example 07: Find the Duplicate Number (LC 287)

## Problem
Array of n+1 integers in [1,n]. Exactly one duplicate. Find it without modifying array, O(1) space.

## Input
nums = [1,3,4,2,2]
## Output
2

## Approach
Floyd's cycle detection: treat array as linked list where index→nums[index].
**Time: O(n)  Space: O(1)**