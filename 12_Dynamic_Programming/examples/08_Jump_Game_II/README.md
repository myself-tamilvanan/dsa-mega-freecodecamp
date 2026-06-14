# Jump Game II (LeetCode #45)

## Problem
Given array nums where nums[i] is the max jump length at index i, return minimum number of jumps to reach the last index.

## Examples
Input: nums=[2,3,1,1,4] → Output: 2 (jump 1→3 steps, then 3→last)
Input: nums=[2,3,0,1,4] → Output: 2

## Constraints
- 1 <= nums.length <= 10^4, 0 <= nums[i] <= 1000, guaranteed reachable

## Approach
Greedy: track current range end and farthest reachable. When we reach end, increment jumps and extend to farthest.

## Complexity
- Time: O(n), Space: O(1)
