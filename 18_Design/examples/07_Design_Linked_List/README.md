# Design Linked List (LeetCode #707)

## Problem
Design and implement a linked list class that supports:
get(index), addAtHead(val), addAtTail(val), addAtIndex(index, val), deleteAtIndex(index)

## Approach
Doubly linked list with dummy head and tail for clean boundary handling.

## Complexity
- get/add/delete: O(n), Space: O(n)
