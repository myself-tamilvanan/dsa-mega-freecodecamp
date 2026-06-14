# Chapter 00: Introduction & Complexity Analysis

## Course Overview
This chapter covers the foundational theory from the course's introduction section, spanning 10 key sub-topics before the DSA deep-dives begin.

---

## 1. Introduction
Data Structures and Algorithms (DSA) are the backbone of software engineering and technical interviews. This course covers every major topic end-to-end in 49 hours.

---

## 2. Technical Interviews 101
- Clarify the problem before coding
- Think out loud — explain your approach
- Start with brute force, then optimize
- Consider edge cases: empty input, nulls, duplicates, large inputs
- Discuss time/space trade-offs
- Test your solution with examples

---

## 3. How to Judge an Algorithm
An algorithm is judged on:
- **Correctness** — does it produce the right output?
- **Efficiency** — time and space complexity
- **Readability** — clean, maintainable code
- **Scalability** — how does it behave as input grows?

---

## 4. What is Time Complexity?
Time complexity measures how the **number of operations** grows relative to input size `n`.
- It is NOT about actual clock time — it is about growth rate
- We drop constants and lower-order terms
- Common complexities (best → worst): O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ), O(n!)

---

## 5. What is Big O Notation?
Big O describes the **worst-case** upper bound of an algorithm's growth rate.

| Notation   | Name         | Example                  |
|------------|--------------|--------------------------|
| O(1)       | Constant     | Array index access       |
| O(log n)   | Logarithmic  | Binary search            |
| O(n)       | Linear       | Single loop              |
| O(n log n) | Linearithmic | Merge sort               |
| O(n²)      | Quadratic    | Nested loops             |
| O(2ⁿ)      | Exponential  | Recursive Fibonacci      |
| O(n!)      | Factorial    | Permutation generation   |

---

## 6. Big O for Code Blocks
Rules for analyzing code:
- **Sequential statements** → add complexities: O(n) + O(n) = O(n)
- **Nested loops** → multiply: O(n) × O(n) = O(n²)
- **Drop constants**: O(2n) → O(n)
- **Drop non-dominant terms**: O(n² + n) → O(n²)
- **Logarithmic**: any algorithm that halves the input each step = O(log n)

```python
# O(n) - single loop
for i in range(n): pass

# O(n²) - nested loops
for i in range(n):
    for j in range(n): pass

# O(log n) - halving
i = n
while i > 1:
    i //= 2
```

---

## 7. Space Complexity Example
Space complexity measures **extra memory** used (not counting input).

```python
# O(1) space - only a few variables
def sum_array(arr):
    total = 0          # O(1)
    for x in arr:
        total += x
    return total

# O(n) space - new array proportional to input
def double_array(arr):
    return [x * 2 for x in arr]  # O(n) extra space

# O(n) space - recursion stack depth
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)  # n stack frames
```

---

## 8. How to Get Good at Solving DSA Problems
1. **Learn the patterns** — not just individual problems
2. **Practice consistently** — 30–60 minutes daily beats marathon sessions
3. **Understand before memorizing** — know WHY a solution works
4. **Categorize problems** — sliding window, two pointers, DFS/BFS, etc.
5. **Review mistakes** — failed attempts are the best learning
6. **Use spaced repetition** — revisit problems after 1 day, 1 week, 1 month

---

## 9. Types of Data Structures
| Type | Examples | Use Cases |
|------|----------|-----------|
| Linear | Array, Linked List, Stack, Queue | Sequential data |
| Non-Linear | Tree, Graph | Hierarchical/networked data |
| Hash-based | HashMap, HashSet | O(1) lookup |
| Heap | Min/Max Heap | Priority access |
| Trie | Prefix Tree | String search |

---

## 10. Quick Recap
Before diving into DSA chapters:
- Big O is about growth rate, not exact speed
- Time and space are often trade-offs
- Choose data structures based on operations needed
- Master each pattern: it applies to many problems

---

## Examples in This Chapter
1. **Big_O_Comparison** — compare O(1), O(log n), O(n), O(n²) visually
2. **Space_Complexity** — demonstrate O(1) vs O(n) space usage
3. **Fibonacci_Approaches** — O(2ⁿ) naive vs O(n) memoized vs O(1) iterative
4. **Count_Steps** — analyze loop-based algorithms step by step
