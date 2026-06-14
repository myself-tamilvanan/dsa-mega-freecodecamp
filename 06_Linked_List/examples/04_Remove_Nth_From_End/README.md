# Example 04: Remove Nth Node From End (LC 19)
## Problem: Remove nth node from end of list in one pass.
## Input: head=1->2->3->4->5, n=2
## Output: 1->2->3->5
## Approach: Two pointers, advance fast n+1 steps then move both until fast is null.
**Time: O(L)  Space: O(1)**