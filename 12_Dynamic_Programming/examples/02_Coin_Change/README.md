# Example 02: Coin Change (LC 322)

## Problem
Find minimum number of coins to make amount.

## Input
coins = [1,5,11], amount = 15
## Output
3 (5+5+5)

## Approach
Bottom-up DP. dp[i] = min coins for amount i.

## Key: order of loops matters!
- Outer: amounts, Inner: coins → correct
**Time: O(amount × coins)  Space: O(amount)**