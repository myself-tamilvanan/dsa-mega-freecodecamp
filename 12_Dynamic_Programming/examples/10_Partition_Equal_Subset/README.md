# Partition Equal Subset Sum (LeetCode #416)

## Problem
Given integer array nums, return true if you can partition it into two subsets with equal sum.

## Examples
Input: nums=[1,5,11,5] → Output: true (subsets: [1,5,5] and [11])
Input: nums=[1,2,3,5] → Output: false

## Approach
DP 0/1 knapsack: if total sum is odd, return false. Otherwise find if subset with sum=total/2 exists.

## Complexity
- Time: O(n * sum/2), Space: O(sum/2)
