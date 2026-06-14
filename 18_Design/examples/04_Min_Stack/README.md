# Example 04: Min Stack (LC 155)

## Problem
Stack with O(1) push, pop, top, and getMin.

## Approach
Parallel min-stack: push min(new_val, current_min). Pop both in sync.

## Alternative
Single stack storing (val, current_min) pairs.
**Time: O(1) all ops  Space: O(n)**