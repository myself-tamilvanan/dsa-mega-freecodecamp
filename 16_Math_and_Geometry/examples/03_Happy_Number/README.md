# Example 03: Happy Number (LC 202)

## Problem
A happy number eventually reaches 1 when replaced by sum of squares of digits.

## Input
n = 19
## Output
True (19 → 82 → 68 → 100 → 1)

## Approach
Floyd's cycle detection. If it cycles to 1 → happy. If cycle doesn't include 1 → not happy.
**Time: O(log n)  Space: O(1)**