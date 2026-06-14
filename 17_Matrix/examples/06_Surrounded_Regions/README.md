# Example 06: Surrounded Regions (LC 130)
## Problem
Flip all 'O' regions fully enclosed by 'X'. Border-connected 'O' cells remain.
## Approach
Mark border-connected 'O' as safe ('S'). Then: 'O'→'X', 'S'→'O'.
**Time: O(m×n)  Space: O(m×n)**