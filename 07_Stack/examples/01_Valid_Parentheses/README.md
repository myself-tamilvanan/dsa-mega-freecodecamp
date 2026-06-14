# Example 01: Valid Parentheses (LC 20)
## Problem: Check if brackets are properly closed and nested.
## Input: s = "()[]{}" → True,  s = "(]" → False
## Approach: Push open brackets; on close, check top matches.
**Time: O(n)  Space: O(n)**