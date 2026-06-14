# Example 01: Best Time to Buy and Sell Stock (LC 121)

## Problem
Find maximum profit from one buy and one sell.

## Input
prices = [7,1,5,3,6,4]
## Output
5 (buy at 1, sell at 6)

## Approach
Sliding window: track min price so far. Profit = current - min.
**Time: O(n)  Space: O(1)**