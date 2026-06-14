# Example 05: Implement Trie (Prefix Tree) (LC 208)

## Problem
Implement Trie with insert, search, startsWith.

## Example
- insert("apple")
- search("apple") → True
- search("app") → False
- startsWith("app") → True

## Approach
Each TrieNode has children dict and is_end flag.
**Time: O(m) per op  Space: O(n*m)**