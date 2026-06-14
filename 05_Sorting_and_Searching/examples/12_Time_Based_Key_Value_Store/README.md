# Example 12: Time Based Key-Value Store (LC 981)

## Problem
Design a key-value store that stores multiple values at different timestamps. get() returns value at latest timestamp <= given timestamp.

## Operations
- set(key, value, timestamp)
- get(key, timestamp) → latest value at timestamp ≤ given

## Approach
Dict of key → list of (timestamp, value). Binary search on timestamps.
**Time: O(log n) get, O(1) set  Space: O(n)**