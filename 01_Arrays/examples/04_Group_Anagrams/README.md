# Example 04: Group Anagrams (LC 49)

## Problem
Given array of strings, group anagrams together.

## Input
strs = ["eat","tea","tan","ate","nat","bat"]
## Output
[["bat"],["nat","tan"],["ate","eat","tea"]]

## Approach
Sort each word as canonical key, group by key.
**Time: O(n·k log k)  Space: O(n·k)**