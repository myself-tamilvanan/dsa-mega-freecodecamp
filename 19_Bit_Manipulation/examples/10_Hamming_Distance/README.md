# Hamming Distance (LeetCode #461)

## Problem
Given two integers x and y, return the Hamming distance (number of positions where bits differ).

## Examples
Input: x=1, y=4 → Output: 2 (1=0001, 4=0100 → differ at bits 0,2)
Input: x=3, y=1 → Output: 1

## Approach
XOR gives 1 at positions where bits differ. Count set bits in XOR result.

## Complexity
- Time: O(1), Space: O(1)
