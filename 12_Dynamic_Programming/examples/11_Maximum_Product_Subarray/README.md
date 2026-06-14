# Maximum Product Subarray (LeetCode #152)

## Problem
Given integer array nums, find a contiguous non-empty subarray with the largest product and return it.

## Examples
Input: nums=[2,3,-2,4] → Output: 6 (subarray [2,3])
Input: nums=[-2,0,-1] → Output: 0

## Approach
Track both max and min products at each position (min can become max when multiplied by negative).

## Complexity
- Time: O(n), Space: O(1)
