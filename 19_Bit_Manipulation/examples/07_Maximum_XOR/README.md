# Example 07: Maximum XOR of Two Numbers in an Array (LC 421)
## Problem
Find maximum XOR of any two elements in the array.
## Input
nums=[3,10,5,25,2,8] → 28 (5 XOR 25)
## Approach
Bit by bit from MSB: greedily try to set each bit. Use prefix set to check feasibility.
**Time: O(32n)=O(n)  Space: O(n)**