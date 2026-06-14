# Example 06: Minimum Window Substring (LC 76)

## Problem
Find the minimum window substring of s that contains all characters of t.

## Input
s = "ADOBECODEBANC", t = "ABC"
## Output
"BANC"

## Approach
Variable sliding window. Track 'have' vs 'need' counts. Shrink when valid.
**Time: O(|s| + |t|)  Space: O(|s| + |t|)**