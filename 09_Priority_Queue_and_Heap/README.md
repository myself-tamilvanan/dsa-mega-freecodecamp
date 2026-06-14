# Chapter 09: Priority Queue & Heap
Complete binary tree. Python heapq = min-heap. Negate for max-heap.

## Operations
| Op | Time |
|----|------|
| Insert | O(log n) |
| Extract min | O(log n) |
| Peek min | O(1) |
| Heapify | O(n) |

## When to Use
- Top K elements → min-heap size k
- Median maintenance → two heaps
- K-way merge → heap of (val, list_idx)
- Dijkstra / Prim → min-heap of (dist, node)

## LeetCode Problems
LC 1046 Last Stone Weight, LC 215 Kth Largest, LC 973 K Closest,
LC 703 Kth Largest Stream, LC 621 Task Scheduler,
LC 295 Median from Data Stream, LC 355 Design Twitter
