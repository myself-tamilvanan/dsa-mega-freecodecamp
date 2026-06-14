# Sudoku Solver (LeetCode #37)

## Problem
Write program to solve a Sudoku puzzle by filling empty cells ('.').

## Rules
- Each row, column, and 3x3 box must contain digits 1-9 with no repetition.

## Approach
Backtracking: try digits 1-9 for each empty cell, checking row/col/box validity. Backtrack on failure.

## Complexity
- Time: O(9^m) where m = empty cells, Space: O(81)
