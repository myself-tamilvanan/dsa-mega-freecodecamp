# Example 04: Palindromic Substrings (LC 647)

## Problem
Count the number of palindromic substrings.
## Input: s = "aaa"
## Output: 6 ("a","a","a","aa","aa","aaa")
## Approach: Expand around center for each character (odd+even length).
**Time: O(n²)  Space: O(1)**