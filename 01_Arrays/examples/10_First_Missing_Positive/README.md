# First Missing Positive (LeetCode #41)

## Problem
Given unsorted integer array nums, return the smallest missing positive integer. Must run in O(n) time and O(1) space.

## Examples
Input: nums=[1,2,0] → Output: 3
Input: nums=[3,4,-1,1] → Output: 2
Input: nums=[7,8,9,11,12] → Output: 1

## Constraints
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1

## Approach
Index as hash: place each number n in position n-1 if 1<=n<=len. Then scan for first index where nums[i] != i+1.

## Complexity
- Time: O(n), Space: O(1)
