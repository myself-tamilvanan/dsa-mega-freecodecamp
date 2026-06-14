# Power of Two (LeetCode #231)

## Problem
Given integer n, return true if n is a power of two.

## Examples
Input: n=1 → Output: true (2^0=1)
Input: n=16 → Output: true (2^4=16)
Input: n=3 → Output: false

## Approach
Bit trick: n & (n-1) == 0 for powers of two (only one bit set), and n > 0.

## Complexity
- Time: O(1), Space: O(1)
