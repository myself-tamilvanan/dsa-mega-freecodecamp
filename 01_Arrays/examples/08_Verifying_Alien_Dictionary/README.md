# Example 08: Verifying an Alien Dictionary (LC 953)

## Problem
Given a list of words in alien language order, verify if words are lexicographically sorted according to the alien alphabet.

## Input
words=["hello","leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"
## Output
True

## Approach
Build order map (char→rank). Compare adjacent word pairs character by character.
**Time: O(M) where M = total characters  Space: O(1)**