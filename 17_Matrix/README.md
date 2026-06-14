# Chapter 17: Matrix
2D grid problems. Most use DFS or BFS with 4-directional movement.

## Traversal Patterns
- **DFS**: connected components, flood fill (recursive or stack)
- **BFS**: shortest path, level-by-level spread (multi-source BFS)
- **In-place marking**: avoid extra visited array

## Common Directions
```python
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
```

## LeetCode Problems
LC 73 Set Zeroes, LC 994 Rotting Oranges, LC 286 Walls & Gates,
LC 130 Surrounded Regions, LC 62 Unique Paths
