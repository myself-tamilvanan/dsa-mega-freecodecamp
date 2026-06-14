# Best Time to Buy and Sell Stock with Cooldown (LeetCode #309)

## Problem
Given prices array, find max profit with cooldown: after selling, you must wait 1 day (cooldown) before buying.

## Examples
Input: prices=[1,2,3,0,2] → Output: 3 (buy 1, sell 3, cooldown, buy 0, sell 2)
Input: prices=[1] → Output: 0

## Approach
State machine DP with 3 states: holding, sold (cooldown), idle.

## Complexity
- Time: O(n), Space: O(1)
