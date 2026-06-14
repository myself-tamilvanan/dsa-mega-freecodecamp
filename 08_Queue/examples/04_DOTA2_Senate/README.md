# Example 04: DOTA2 Senate (LC 649)
## Problem: Each senator can ban the nearest opponent. Who wins?
## Input: senate = "RDD"
## Output: "Dire"
## Approach: Two queues of indices. Smaller index wins each round, then re-queues with +n.
**Time: O(n)  Space: O(n)**