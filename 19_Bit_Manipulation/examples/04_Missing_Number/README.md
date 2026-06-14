# Example 04: Missing Number (LC 268)

## Problem
Given array containing n distinct numbers in range [0,n], find the missing one.

## Input
nums = [3,0,1]
## Output
2

## Three Approaches
1. XOR: XOR 0..n with all nums; missing remains
2. Math: n*(n+1)/2 - sum(nums)
3. Sorting
**Time: O(n)  Space: O(1)**