# Candy (LeetCode #135)

## Problem
n children in a line with ratings. Each child must have at least 1 candy. Children with higher rating than neighbors get more. Return minimum candies needed.

## Examples
Input: ratings=[1,0,2] → Output: 5 (candies: [2,1,2])
Input: ratings=[1,2,2] → Output: 4 (candies: [1,2,1])

## Approach
Two-pass greedy: left-to-right (give more if rating > left neighbor), right-to-left (give more if rating > right neighbor), take max.

## Complexity
- Time: O(n), Space: O(n)
