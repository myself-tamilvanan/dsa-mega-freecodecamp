# Example 03: Longest Repeating Character Replacement (LC 424)

## Problem
Replace at most k characters. Find longest substring of one repeated letter.

## Input
s = "AABABBA", k = 1
## Output
4

## Key Insight
Window is valid if (window_size - max_frequency) <= k
**Time: O(n)  Space: O(1)**