# Example 04: Longest Substring Without Repeating Characters (LC 3)

## Problem
Find length of longest substring without repeated characters.

## Input
s = "abcabcbb"
## Output
3 ("abc")

## Approach
Variable sliding window. When duplicate found, move left past its last occurrence.
**Time: O(n)  Space: O(min(m,n))**