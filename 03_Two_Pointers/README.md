# Chapter 03: Two Pointers
Use two index variables to eliminate nested loops.

## Patterns
1. **Opposite ends**: l=0, r=n-1 → meet in middle (sorted array pairs)
2. **Same direction**: fast moves ahead, slow follows (in-place editing)
3. **Two arrays**: one pointer per array

## Template (Opposite)
```
l, r = 0, len(arr)-1
while l < r:
    if CONDITION: l += 1
    else: r -= 1
```

## LeetCode Problems
LC 125 Valid Palindrome, LC 167 Two Sum II, LC 15 3Sum,
LC 11 Container With Most Water, LC 42 Trapping Rain Water,
LC 26 Remove Duplicates, LC 31 Next Permutation
