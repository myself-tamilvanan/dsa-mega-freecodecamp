# Chapter 02: Sliding Window
Use a window that slides over data to avoid O(n²) brute force.

## Types
1. **Fixed window** — size k constant; slide by remove-left add-right
2. **Variable window** — expand right, shrink left when condition violated

## Template (Variable)
```
left = 0
for right in range(len(s)):
    # expand window with s[right]
    while WINDOW_INVALID:
        # shrink: remove s[left]; left++
    result = max(result, right-left+1)
```

## LeetCode Problems
LC 121 Best Time to Buy/Sell Stock, LC 567 Permutation in String,
LC 424 Longest Repeating Char Replacement, LC 3 Longest Substring Without Repeat,
LC 239 Sliding Window Maximum, LC 76 Minimum Window Substring
