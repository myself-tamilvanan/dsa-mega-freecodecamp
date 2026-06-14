# Hand of Straights (LeetCode #846)

## Problem
You have a hand of cards given as array hand. Return true if you can arrange the cards into groups of size groupSize where each group is consecutive.

## Examples
Input: hand=[1,2,3,6,2,3,4,7,8], groupSize=3 → Output: true (groups: [1,2,3],[2,3,4],[6,7,8])
Input: hand=[1,2,3,4,5], groupSize=4 → Output: false

## Approach
Sort + greedy / Counter: sort unique values, for smallest card start a new group, check groupSize consecutive values exist.

## Complexity
- Time: O(n log n), Space: O(n)
