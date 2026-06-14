# Example 06: Text Justification (LC 68)

## Problem
Format text: each line has exactly maxWidth characters, fully justified (except last line which is left-justified).

## Input
words=["This","is","an","example","of","text","justification."], maxWidth=16
## Output
["This    is    an","example  of text","justification.  "]

## Approach
Greedy word packing. Distribute spaces evenly; extra spaces go left-to-right.
**Time: O(n)  Space: O(n)**