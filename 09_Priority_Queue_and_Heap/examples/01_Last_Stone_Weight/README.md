# Example 01: Last Stone Weight (LC 1046)

## Problem
Smash the two heaviest stones. If unequal, remainder stays. Return last stone or 0.

## Input
stones = [2,7,4,1,8,1]
## Output
1

## Approach
Max-heap (negate for Python's min-heap). Keep popping two, push remainder.
**Time: O(n log n)  Space: O(n)**