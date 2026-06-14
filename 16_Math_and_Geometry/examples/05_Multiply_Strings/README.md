# Example 05: Multiply Strings (LC 43)
## Problem
Given two non-negative integers as strings, return product as string. No big integer library.
## Input
num1="123", num2="456" → "56088"
## Approach
Grade-school multiplication: result[i+j+1] += d1*d2. Handle carries.
**Time: O(m×n)  Space: O(m+n)**