# Example 01: Single Number (LC 136)

## Problem
Every element appears twice except one. Find that one in O(n) time O(1) space.

## Input
nums = [4,1,2,1,2]
## Output
4

## Key Insight
XOR: a^a=0, a^0=a. XOR all numbers: pairs cancel, lone number remains.
**Time: O(n)  Space: O(1)**