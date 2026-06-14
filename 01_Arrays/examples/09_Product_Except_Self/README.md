# Product of Array Except Self (LeetCode #238)

## Problem
Given integer array nums, return array answer such that answer[i] equals the product of all elements except nums[i]. Must run in O(n), no division.

## Examples
Input: nums=[1,2,3,4] → Output: [24,12,8,6]
Input: nums=[-1,1,0,-3,3] → Output: [0,0,9,0,0]

## Constraints
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30

## Approach
Two passes: left pass (prefix products) and right pass (suffix products). Multiply prefix and suffix for each index.

## Complexity
- Time: O(n), Space: O(1) (output array not counted)
