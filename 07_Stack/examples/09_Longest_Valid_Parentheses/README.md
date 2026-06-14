# Example 09: Longest Valid Parentheses (LC 32)

## Problem
Find the length of the longest valid (well-formed) parentheses substring.

## Input
s = ")()())"
## Output
4

## Approach
Stack storing indices. Push index of '('; on ')' pop and compute length.
**Time: O(n)  Space: O(n)**