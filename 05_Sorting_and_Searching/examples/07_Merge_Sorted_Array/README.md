# Example 07: Merge Sorted Array (LC 88)

## Problem
Merge nums2 into nums1 in-place. nums1 has m+n slots (last n are zeros).

## Input
nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3
## Output
nums1=[1,2,2,3,5,6]

## Approach
Three pointers from the back. Place largest first.
**Time: O(m+n)  Space: O(1)**