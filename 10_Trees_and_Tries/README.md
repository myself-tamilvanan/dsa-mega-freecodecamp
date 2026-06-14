# Chapter 10: Trees & Tries
Binary tree: each node ≤ 2 children. BST: left<root<right.

## Traversals
| Order | Pattern | Use Case |
|-------|---------|---------|
| Inorder | L→Root→R | BST sorted output |
| Preorder | Root→L→R | Copy/serialize |
| Postorder | L→R→Root | Delete/evaluate |
| Level-order | BFS | Level queries |

## Trie
Prefix tree for word search. O(m) insert/search where m=word length.

## LeetCode Problems
LC 104 Max Depth, LC 100 Same Tree, LC 226 Invert, LC 102 Level Order,
LC 199 Right Side View, LC 543 Diameter, LC 98 Validate BST,
LC 235 LCA of BST, LC 297 Serialize/Deserialize, LC 124 Max Path Sum,
LC 208 Implement Trie, LC 212 Word Search II
