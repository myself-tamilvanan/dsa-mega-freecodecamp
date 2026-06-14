# Example 06: Reorder List (LC 143)
## Problem: Reorder L0->Ln->L1->Ln-1->L2->Ln-2...
## Input: 1->2->3->4->5
## Output: 1->5->2->4->3
## Approach: Find middle, reverse second half, merge two halves.
**Time: O(n)  Space: O(1)**