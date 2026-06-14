# Example 04: Evaluate Reverse Polish Notation (LC 150)
## Problem: Evaluate RPN expression.
## Input: ["2","1","+","3","*"]
## Output: 9  ((2+1)*3)
## Approach: Stack. On operand push; on operator pop two and compute.
**Time: O(n)  Space: O(n)**