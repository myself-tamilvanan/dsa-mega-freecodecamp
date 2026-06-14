# Burst Balloons (LeetCode #312)

## Problem
Given n balloons, indexed 0 to n-1. nums[i] is the number on balloon i. Bursting balloon i gives nums[i-1]*nums[i]*nums[i+1] coins. Return max coins.

## Examples
Input: nums=[3,1,5,8] → Output: 167 ([3,1,5,8]→[3,5,8]→[3,8]→[8]→[] with 3*1*5+3*5*8+1*3*8+1*8*1=167)
Input: nums=[1,5] → Output: 10

## Approach
Interval DP: dp[left][right] = max coins for balloons in range (left, right) exclusive. Choose last balloon to burst.

## Complexity
- Time: O(n^3), Space: O(n^2)
