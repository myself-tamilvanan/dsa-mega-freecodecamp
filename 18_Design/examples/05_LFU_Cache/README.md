# Example 05: LFU Cache (LC 460)
## Problem
Least Frequently Used Cache — evict least frequently used item (tie: evict least recently used).
## Approach
Three maps: key→val, key→freq, freq→OrderedDict. Track min_freq.
**All ops O(1)  Space: O(capacity)**