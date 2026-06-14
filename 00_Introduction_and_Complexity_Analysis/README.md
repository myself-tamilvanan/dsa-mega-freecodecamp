# Chapter 00: Introduction & Complexity Analysis

## What is an Algorithm?
A step-by-step procedure to solve a problem. Judged on correctness, efficiency, and readability.

## What is a Data Structure?
A way of organizing data to enable efficient access and modification.

---

## ⏱️ Time Complexity – Big O

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array index access |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | Single loop |
| O(n log n) | Linearithmic | Merge Sort |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Naive recursion |
| O(n!) | Factorial | All permutations |

### Big O Rules
- Drop constants: O(2n) → O(n)
- Drop non-dominants: O(n² + n) → O(n²)
- Sequential steps add: O(n) + O(m) → O(n + m)
- Nested steps multiply: O(n) × O(m) → O(n × m)

---

## 💾 Space Complexity
- Only count **extra** memory used (not input)
- Recursive calls use O(depth) stack space
- Creating new arrays: O(n) space

---

## 🧠 Problem-Solving Framework
1. **Understand** – restate the problem, clarify edge cases
2. **Examples** – walk through 2-3 examples by hand
3. **Brute Force** – find any working solution first
4. **Optimize** – identify bottlenecks, apply patterns
5. **Code** – write clean, modular code
6. **Test** – edge cases: empty, single, duplicates, negatives
