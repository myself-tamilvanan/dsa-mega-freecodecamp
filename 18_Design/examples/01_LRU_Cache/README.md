# Example 01: LRU Cache (LC 146)

## Problem
Design LRU Cache with O(1) get and put.
- get(key): return value or -1
- put(key, value): insert/update, evict LRU if over capacity

## Approach
OrderedDict: maintains order, supports O(1) move_to_end and popitem.
**Time: O(1) all ops  Space: O(capacity)**