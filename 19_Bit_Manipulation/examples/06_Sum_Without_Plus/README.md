# Example 06: Sum of Two Integers (LC 371)
## Problem
Calculate sum of a and b without using + or - operators.
## Approach
XOR gives sum bits (no carry). AND+left_shift gives carry. Repeat until no carry.
**Time: O(1)  Space: O(1)**