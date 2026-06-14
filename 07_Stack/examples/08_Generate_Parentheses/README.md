# Example 08: Generate Parentheses (LC 22)

## Problem
Generate all combinations of n pairs of well-formed parentheses.

## Input
n = 3
## Output
["((()))","(()())","(())()","()(())","()()()"]

## Approach
Backtracking: add '(' if open_count < n; add ')' if close_count < open_count.
**Time: O(4^n/√n)  Space: O(n)**