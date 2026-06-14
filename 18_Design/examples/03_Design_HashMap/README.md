# Example 03: Design HashMap (LC 706)

## Problem
Design HashMap without built-in hash table libraries.

## Operations: put(key,val), get(key), remove(key)

## Approach
Chaining: array of buckets (lists of key-value pairs). Hash = key % BUCKETS.
**Time: O(1) avg  Space: O(n)**