# Chapter 12: Dynamic Programming
Break into overlapping subproblems, memoize results.

## Approaches
- **Top-down** (memo): recursive + cache dict
- **Bottom-up** (tabulation): fill table iteratively

## Patterns
| Pattern | Examples |
|---------|---------|
| 1D DP | Climbing Stairs, Fibonacci, House Robber |
| Knapsack | Coin Change, Partition Subset |
| 2D DP | Unique Paths, Edit Distance, LCS |
| String | Palindromic Subsequence, Word Break |
| Interval | Burst Balloons |

## Steps
1. Define dp[i] clearly
2. Find recurrence (how dp[i] depends on previous)
3. Set base cases
4. Fill order (bottom-up) or add memoization (top-down)
5. Optimize space if possible
