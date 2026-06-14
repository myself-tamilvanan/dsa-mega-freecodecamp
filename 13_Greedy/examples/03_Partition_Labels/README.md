# Example 03: Partition Labels (LC 763)

## Problem
Partition string so each letter appears in at most one part. Return partition sizes.

## Input
s = "ababcbacadefegdehijhklij"
## Output
[9,7,8]

## Approach
1. Record last occurrence of each character.
2. Expand current partition until all chars in it have ended.
**Time: O(n)  Space: O(1)**