# Chapter 18: Design
Combine data structures for O(1) complex operations.

## Key Designs
- **LRU Cache**: OrderedDict or DLL + HashMap
- **LFU Cache**: key→val, key→freq, freq→OrderedDict
- **Design Twitter**: heap + deque per user
- **Trie**: TrieNode with children dict + is_end flag

## LeetCode Problems
LC 146 LRU Cache, LC 460 LFU Cache, LC 355 Design Twitter,
LC 208 Implement Trie, LC 155 Min Stack, LC 622 Circular Queue
