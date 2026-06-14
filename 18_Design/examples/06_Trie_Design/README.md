# Example 06: Implement Trie (Prefix Tree) (LC 208)
## Problem
Implement a Trie with insert, search, and startsWith operations.
## Example
insert("apple"), search("apple")=True, search("app")=False, startsWith("app")=True
## Approach
Each TrieNode: children dict + is_end flag.
**Time: O(m) per op  Space: O(n×m)**