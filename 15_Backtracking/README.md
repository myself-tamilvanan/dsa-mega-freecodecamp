# Chapter 15: Backtracking
Build candidates incrementally, abandon (backtrack) when invalid.

## Template
```
def backtrack(state, choices):
    if is_solution(state):
        result.append(state[:]); return
    for choice in choices:
        if is_valid(choice):
            state.append(choice)
            backtrack(state, choices)
            state.pop()  # UNDO
```

## LeetCode Problems
LC 78 Subsets, LC 90 Subsets II, LC 46 Permutations,
LC 39 Combination Sum, LC 40 Combination Sum II,
LC 79 Word Search, LC 51 N-Queens, LC 131 Palindrome Partitioning
