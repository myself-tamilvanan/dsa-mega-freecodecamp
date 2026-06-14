# Example 05: Reverse Bits (LC 190)
## Problem
Reverse bits of a 32-bit unsigned integer.
## Input
n=43261596 (binary 00000010100101000001111010011100) → 964176192
## Approach
Shift result left and take LSB of n, repeat 32 times.
**Time: O(32)=O(1)  Space: O(1)**