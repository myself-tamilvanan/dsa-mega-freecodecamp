# Example 07: Next Permutation (LC 31)

## Problem
Rearrange numbers to form lexicographically next greater permutation in-place. If not possible, return the lowest order (ascending).

## Input
nums = [1,2,3] → [1,3,2]
nums = [3,2,1] → [1,2,3]
nums = [1,1,5] → [1,5,1]

## Algorithm
1. Find largest i such that nums[i] < nums[i+1]
2. Find largest j such that nums[i] < nums[j]
3. Swap i and j
4. Reverse from i+1 to end
**Time: O(n)  Space: O(1)**