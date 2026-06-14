# Example 07: Same Tree (LC 100)
## Problem
Determine if two binary trees are identical (same structure and values).
## Input
p=[1,2,3], q=[1,2,3] → True
p=[1,2], q=[1,null,2] → False
## Approach
Recursive DFS: both null→True, one null→False, values differ→False.
**Time: O(n)  Space: O(h)**