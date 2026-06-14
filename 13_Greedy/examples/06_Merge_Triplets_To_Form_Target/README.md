# Merge Triplets to Form Target Triplet (LeetCode #1899)

## Problem
Given 2D array of triplets and a target triplet, merge valid triplets (element-wise max) to form the target.
A triplet is valid if no element exceeds the corresponding target element.

## Examples
Input: triplets=[[2,5,3],[1,8,4],[1,7,5]], target=[2,7,5] → Output: true
Input: triplets=[[3,4,5],[4,5,6]], target=[3,2,5] → Output: false

## Approach
Greedy: filter triplets that don't exceed target. Check if merge of valid ones equals target.

## Complexity
- Time: O(n), Space: O(1)
