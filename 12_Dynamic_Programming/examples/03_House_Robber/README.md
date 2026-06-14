# Example 03: House Robber (LC 198)

## Problem
Rob houses; can't rob two adjacent. Maximize total.

## Input
nums = [2,7,9,3,1]
## Output
12 (rob houses 0,2,4: 2+9+1=12)

## Approach
dp[i] = max(dp[i-1], dp[i-2]+nums[i])

Optimized: track only prev2, prev1.
**Time: O(n)  Space: O(1)**