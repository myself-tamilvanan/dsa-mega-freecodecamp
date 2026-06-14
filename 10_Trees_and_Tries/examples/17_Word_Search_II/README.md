# Example 17: Word Search II (LC 212)
## Problem
Find all words from a list that exist in the board.
## Input
board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words=["oath","pea","eat","rain"]
## Output
["eat","oath"]
## Approach
Build Trie from words. DFS on board matching Trie paths.
**Time: O(M*N*4^L)  Space: O(W*L)**