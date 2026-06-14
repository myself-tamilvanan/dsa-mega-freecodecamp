# Example 02: Permutation in String (LC 567)

## Problem
Return true if any permutation of s1 is a substring of s2.

## Input
s1="ab", s2="eidbaooo"
## Output
True ("ba" is in s2)

## Approach
Fixed sliding window of size len(s1). Compare character frequency maps.
**Time: O(n)  Space: O(1)**