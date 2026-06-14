# Example 11: Largest Number (LC 179)

## Problem
Arrange non-negative integers to form the largest number.

## Input
nums = [3,30,34,5,9]
## Output
"9534330"

## Approach
Custom sort: compare ab vs ba as strings. Use functools.cmp_to_key.
**Time: O(n log n)  Space: O(n)**