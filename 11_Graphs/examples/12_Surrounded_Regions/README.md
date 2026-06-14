# Example 12: Surrounded Regions (LC 130)
## Problem
Capture all 'O' regions fully surrounded by 'X'. Border-connected 'O' regions are NOT captured.
## Approach
DFS from border 'O' cells marking them safe ('S'). Then flip: 'O'→'X', 'S'→'O'.
**Time: O(m×n)  Space: O(m×n)**