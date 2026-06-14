# Example 03: Open the Lock (LC 752)
## Problem: BFS from "0000" to target, avoiding deadends.
## Input: deadends=["0201","0101","0102","1212","2002"], target="0202"
## Output: 6
## Approach: Multi-directional BFS. Each state = 4-digit string.
**Time: O(10^4 * 4 * 2)**