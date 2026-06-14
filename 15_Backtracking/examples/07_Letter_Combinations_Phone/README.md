# Example 07: Letter Combinations of a Phone Number (LC 17)
## Problem
Given digits string, return all letter combinations.
## Input
digits="23" → ["ad","ae","af","bd","be","bf","cd","ce","cf"]
## Approach
Backtracking: for each digit, try each mapped letter.
**Time: O(4^n × n)  Space: O(n)**