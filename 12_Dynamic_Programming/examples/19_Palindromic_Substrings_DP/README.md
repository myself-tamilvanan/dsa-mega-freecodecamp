# Palindromic Substrings (LeetCode #647)

## Problem
Given a string s, return the number of palindromic substrings in it.

## Examples
Input: s="abc" → Output: 3 ("a","b","c")
Input: s="aaa" → Output: 6 ("a","a","a","aa","aa","aaa")

## Approach
Expand around center: for each center (single char or between two chars), expand outward counting palindromes.

## Complexity
- Time: O(n^2), Space: O(1)
