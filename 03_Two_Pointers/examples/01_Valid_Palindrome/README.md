# Example 01: Valid Palindrome (LC 125)

## Problem
A phrase is a palindrome if, after lowercasing and removing non-alphanumeric characters, it reads the same forwards and backwards.

## Input
s = "A man, a plan, a canal: Panama"
## Output
True

## Approach
Two pointers from both ends, skipping non-alphanumeric.
**Time: O(n)  Space: O(1)**