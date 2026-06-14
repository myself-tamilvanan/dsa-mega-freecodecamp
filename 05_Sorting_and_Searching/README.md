# Chapter 05: Sorting & Searching

## Sorting Algorithms
| Algorithm | Time | Space | Stable |
|-----------|------|-------|--------|
| Bubble | O(n²) | O(1) | Yes |
| Merge | O(n log n) | O(n) | Yes |
| Quick | O(n log n) avg | O(log n) | No |
| Heap | O(n log n) | O(1) | No |
| Counting | O(n+k) | O(k) | Yes |

## Binary Search Variants
- **Standard**: find exact target in sorted array
- **Lower/Upper bound**: first/last occurrence
- **On answer space**: minimize/maximize value satisfying a condition

## Template
```
l, r = 0, len(arr)-1
while l <= r:
    m = (l+r)//2
    if check(m): r = m-1
    else: l = m+1
```
