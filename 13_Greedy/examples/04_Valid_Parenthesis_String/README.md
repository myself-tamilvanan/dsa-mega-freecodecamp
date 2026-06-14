# Example 04: Valid Parenthesis String (LC 678)

## Problem
'*' can be '(' or ')' or ''. Check if string is valid.

## Input
s = "(*)"
## Output
True

## Approach
Track range [min_open, max_open]. If max_open < 0 → impossible.
**Time: O(n)  Space: O(1)**