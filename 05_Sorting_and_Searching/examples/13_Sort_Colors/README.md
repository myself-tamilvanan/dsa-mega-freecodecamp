# Sort Colors / Dutch National Flag (LeetCode #75)

## Problem
Given array nums with values 0, 1, 2 (representing red, white, blue), sort them in-place so all 0s first, then 1s, then 2s.

## Examples
Input: nums=[2,0,2,1,1,0] → Output: [0,0,1,1,2,2]
Input: nums=[2,0,1] → Output: [0,1,2]

## Constraints
- 1 <= nums.length <= 300, nums[i] is 0, 1, or 2

## Approach
Dutch National Flag (3-way partition): use three pointers low, mid, high.
- nums[mid]==0: swap with low, advance both
- nums[mid]==1: advance mid
- nums[mid]==2: swap with high, retreat high

## Complexity
- Time: O(n), Space: O(1)
