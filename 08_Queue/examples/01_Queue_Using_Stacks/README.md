# Example 01: Implement Queue Using Stacks (LC 232)
## Problem: Implement FIFO queue using only two stacks.
## Operations: push, pop, peek, empty — all amortized O(1).
## Approach: in_stack for push; on pop/peek transfer all to out_stack.