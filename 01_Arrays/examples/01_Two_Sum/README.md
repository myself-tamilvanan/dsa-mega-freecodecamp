# Example 01: Two Sum (LC 1)

## Problem
Given array nums and integer target, return indices of two numbers that add to target. Exactly one solution exists.

## Input
nums = [2,7,11,15], target = 9
## Output
[0, 1] (nums[0]+nums[1] = 2+7 = 9)

## Constraints
- 2 ≤ nums.length ≤ 10⁴
- Only one valid answer

## Approach
Hash map: store value→index. For each number, check if complement exists.
**Time: O(n)  Space: O(n)**