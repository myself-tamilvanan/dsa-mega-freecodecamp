# Example 06: Plus One (LC 66)
## Problem
Increment large integer represented as digit array by 1.
## Input
digits=[1,2,3] → [1,2,4]
digits=[9,9,9] → [1,0,0,0]
## Approach
Traverse from right, add carry. Prepend 1 if all nines.
**Time: O(n)  Space: O(1)**