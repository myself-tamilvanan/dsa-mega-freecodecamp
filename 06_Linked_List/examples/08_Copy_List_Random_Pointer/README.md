# Example 08: Copy List with Random Pointer (LC 138)

## Problem
Deep copy a linked list where each node has next AND random pointer.

## Approach
1. Interleave clones: original→clone→original.next→...
2. Set random pointers
3. Separate the two lists
**Time: O(n)  Space: O(1)**