# Example 18: Design Add and Search Words Data Structure (LC 211)
## Problem
Design structure supporting addWord and search where search can contain '.' (any character).
## Approach
Trie where '.' triggers DFS on all children.
**Time: O(M) add, O(26^M) search worst case  Space: O(M*N)**