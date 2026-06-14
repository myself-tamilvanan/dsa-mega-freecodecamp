# Example 06: Palindrome Partitioning (LC 131)
## Problem
Partition string s such that every substring is a palindrome. Return all partitions.
## Input
s="aab" → [["a","a","b"],["aa","b"]]
## Approach
Backtracking: try every prefix, recurse if it's a palindrome.
**Time: O(n×2^n)  Space: O(n)**