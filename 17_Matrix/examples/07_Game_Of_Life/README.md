# Game of Life (LeetCode #289)

## Problem
Given m x n grid board where each cell is 0 (dead) or 1 (live), apply Conway's Game of Life rules simultaneously:
- Live cell with 2-3 live neighbors → stays alive
- Dead cell with exactly 3 live neighbors → becomes alive
- Otherwise → dead

## Examples
Input: [[0,1,0],[0,0,1],[1,1,1],[0,0,0]] → Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

## Approach
In-place with encoded states: use 2 (was dead→live) and -1 (was live→dead) to encode transitions.

## Complexity
- Time: O(m*n), Space: O(1)
