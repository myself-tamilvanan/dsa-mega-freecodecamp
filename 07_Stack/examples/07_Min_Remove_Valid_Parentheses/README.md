# Example 07: Minimum Remove to Make Valid Parentheses (LC 1249)

## Problem
Remove minimum parentheses to make the string valid. Return the result.

## Input
s = "lee(t(c)o)de)"
## Output
"lee(t(c)o)de"

## Approach
Use stack to track unmatched '(' indices. Mark invalid chars, rebuild string.
**Time: O(n)  Space: O(n)**