# Chapter 07: Stack
LIFO — push/pop/peek all O(1). Use Python list.

## Key Patterns
- **Matching brackets**: push open, pop on close
- **Monotonic stack**: maintain increasing/decreasing order for "next greater/smaller"
- **Expression evaluation**: RPN

## Monotonic Stack
Push index; while top violates order, pop and process.
Used for: Daily Temperatures, Largest Rectangle in Histogram, Car Fleet.

## LeetCode Problems
LC 20 Valid Parentheses, LC 155 Min Stack, LC 739 Daily Temperatures,
LC 853 Car Fleet, LC 150 Evaluate RPN, LC 22 Generate Parentheses,
LC 84 Largest Rectangle in Histogram
