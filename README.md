# DSA Mega Course – Complete Notes Guide

## Data Structures and Algorithms (Python)

> Based on the FreeCodeCamp DSA Mega Course (49 Hours) by Destination FAANG

---

## 📚 Course Overview

This notes guide covers every major Data Structure and Algorithm topic needed to master technical interviews. Each chapter contains:

- **README.md** – Theory, concepts, time/space complexity, patterns, tips
- **program.py** – Core implementations in Python
- **examples/** – Multiple LeetCode-style problems, each in its own subfolder with README.md (problem) and program.py (solution)

---

## 🗂️ Chapters

| #   | Chapter                            | Examples Included |
| --- | ---------------------------------- | ----------------- |
| 00  | Introduction & Complexity Analysis | 4 examples        |
| 01  | Arrays                             | 10 examples       |
| 02  | Sliding Window                     | 6 examples        |
| 03  | Two Pointers                       | 7 examples        |
| 04  | Strings                            | 6 examples        |
| 05  | Sorting & Searching                | 13 examples       |
| 06  | Linked List                        | 12 examples       |
| 07  | Stack                              | 9 examples        |
| 08  | Queue                              | 5 examples        |
| 09  | Priority Queue & Heap              | 9 examples        |
| 10  | Trees & Tries                      | 22 examples       |
| 11  | Graphs                             | 22 examples       |
| 12  | Dynamic Programming                | 20 examples       |
| 13  | Greedy                             | 7 examples        |
| 14  | Intervals                          | 6 examples        |
| 15  | Backtracking                       | 10 examples       |
| 16  | Math & Geometry                    | 6 examples        |
| 17  | Matrix                             | 8 examples        |
| 18  | Design                             | 8 examples        |
| 19  | Bit Manipulation                   | 10 examples       |

---

## 🚀 How to Use

1. Read each chapter's `README.md` for theory
2. Study `program.py` for clean implementations
3. Go to `examples/XX_ProblemName/` and read the problem in `README.md`
4. Try to solve it yourself first, then check `program.py`
5. Run: `python examples/XX_ProblemName/program.py`

---

## ⏱️ Big O Cheat Sheet

| Notation   | Name         | Example                   |
| ---------- | ------------ | ------------------------- |
| O(1)       | Constant     | Array access, hash lookup |
| O(log n)   | Logarithmic  | Binary search             |
| O(n)       | Linear       | Array scan                |
| O(n log n) | Linearithmic | Merge sort                |
| O(n²)      | Quadratic    | Bubble sort, nested loops |
| O(2ⁿ)      | Exponential  | Subset generation         |
| O(n!)      | Factorial    | Permutations              |

---

# 📚 Data Structures — Big O Cheat Sheet

> **Reference:** _Data Structures Explained for Beginners - How I Wish I was Taught_ by [Sajjaad Khader](https://www.youtube.com/@SajjaadKhader)
> — [Watch on YouTube](https://www.youtube.com/watch?v=O9v10jQkm5c)

---

## 🔢 Big O Notation Quick Reference

Before diving into data structures, it's important to understand how we measure efficiency. Big O describes how an operation scales as input size (`n`) grows.

| Notation | Name        | Description                                                                                                       |
| -------- | ----------- | ----------------------------------------------------------------------------------------------------------------- |
| O(1)     | Constant    | Speed of light — doesn't matter how big the input is, it always takes the same time                               |
| O(log n) | Logarithmic | Cuts the search space in half every step (e.g., binary search in a dictionary)                                    |
| O(n)     | Linear      | Goes through every element once (e.g., looking at every student to find one)                                      |
| O(n²)    | Quadratic   | Every element is compared against every other element (e.g., a class full of students shaking each other's hands) |

---

## 📦 Data Structures

---

### 1. Array

**Summary:** An array stores data in a contiguous block of memory where each element sits side by side. Because each element has a fixed index, you can jump directly to any position instantly — no searching required. The downside is that arrays have a fixed size; adding beyond capacity requires creating a brand new array and copying everything over.

**Real-World Example:** A row of middle school lockers — each locker has a fixed number and you can go directly to it without checking the others. But you can't add a new locker without breaking down a wall (i.e., rebuilding the whole row).

| Operation           | Average Case | Worst Case | Notes                                   |
| ------------------- | ------------ | ---------- | --------------------------------------- |
| Access              | O(1)         | O(1)       | Direct index lookup                     |
| Search              | O(n)         | O(n)       | Must scan each element                  |
| Insert (replace)    | O(1)         | O(1)       | Replacing an existing index             |
| Insert (new/expand) | O(n)         | O(n)       | Must copy entire array to a new one     |
| Delete (end)        | O(1)         | O(1)       | Remove last element, no shifting        |
| Delete (middle)     | O(n)         | O(n)       | All subsequent elements must shift down |
| **Space**           | **O(n)**     | **O(n)**   |                                         |

---

### 2. Linked List

**Summary:** A linked list is made up of nodes, where each node holds a value and a pointer to the next node. Unlike arrays there is no contiguous memory — nodes can live anywhere and are stitched together by pointers. This makes insertion and deletion very efficient (just redirect a pointer), but searching requires traversing node by node from the beginning. There is also no fixed-size constraint, so resizing is never an issue.

**Real-World Example:** A scavenger hunt — each clue tells you where the next one is. You can't jump to clue #5 directly; you have to follow the chain from the start.

| Operation               | Average Case | Worst Case | Notes                               |
| ----------------------- | ------------ | ---------- | ----------------------------------- |
| Access                  | O(n)         | O(n)       | Must traverse from head             |
| Search                  | O(n)         | O(n)       | No indexing, must walk the list     |
| Insert (with reference) | O(1)         | O(1)       | Just redirect pointers              |
| Insert (no reference)   | O(n)         | O(n)       | Must search for position first      |
| Delete (with reference) | O(1)         | O(1)       | Just redirect pointers, no shifting |
| Delete (no reference)   | O(n)         | O(n)       | Must search for node first          |
| **Space**               | **O(n)**     | **O(n)**   |                                     |

---

### 3. Stack

**Summary:** A stack follows the **Last In, First Out (LIFO)** principle — the last element added is the first one removed. Think of a stack of plates: you always take from the top. The only operations you ever do are `push` (add to top) and `pop` (remove from top), both of which are O(1). Stacks are commonly used in depth-first search (DFS) and function call management.

**Real-World Example:** A stack of Pringles chips — you can only eat the one on top. You can't reach down and grab one from the middle.

| Operation          | Average Case | Worst Case | Notes                        |
| ------------------ | ------------ | ---------- | ---------------------------- |
| Access (top)       | O(1)         | O(1)       | Peek at the top element      |
| Access (arbitrary) | O(n)         | O(n)       | Must pop through to reach it |
| Search             | O(n)         | O(n)       | No indexing, must traverse   |
| Insert (push)      | O(1)         | O(1)       | Add to the top               |
| Delete (pop)       | O(1)         | O(1)       | Remove from the top          |
| **Space**          | **O(n)**     | **O(n)**   |                              |

---

### 4. Queue

**Summary:** A queue follows the **First In, First Out (FIFO)** principle — the first element added is the first one removed. Elements are added at the back (`enqueue`) and removed from the front (`dequeue`). Think of it as the reverse of a stack. Queues are widely used in breadth-first search (BFS) and streaming applications like Spotify's music queue.

**Real-World Example:** A line at the grocery store — the first person in line is the first person served. New people join the back of the line.

| Operation          | Average Case | Worst Case | Notes                      |
| ------------------ | ------------ | ---------- | -------------------------- |
| Access (front)     | O(1)         | O(1)       | Peek at the front element  |
| Access (arbitrary) | O(n)         | O(n)       | Must traverse the queue    |
| Search             | O(n)         | O(n)       | No indexing, must traverse |
| Insert (enqueue)   | O(1)         | O(1)       | Add to the back            |
| Delete (dequeue)   | O(1)         | O(1)       | Remove from the front      |
| **Space**          | **O(n)**     | **O(n)**   |                            |

---

### 5. Heap (Priority Queue)

**Summary:** A heap is a **complete binary tree** that satisfies the heap property. In a **Min Heap**, every parent is smaller than its children — the top (root) is always the smallest element. In a **Max Heap**, every parent is larger — the root is always the largest. When an element is added, it "bubbles up" to its correct position; when removed, the structure "bubbles down" to restore balance. Because heaps are balanced binary trees, insert and delete are O(log n) — far more efficient than linear structures for priority-based access.

**Real-World Example:** A pyramid of stacked boxes where the smallest box is always at the very top. If you remove any box, the pyramid instantly rearranges so a new smallest box is back at the top.

| Operation          | Average Case | Worst Case | Notes                                  |
| ------------------ | ------------ | ---------- | -------------------------------------- |
| Access (root/top)  | O(1)         | O(1)       | Min or max element always at root      |
| Access (arbitrary) | O(n)         | O(n)       | No direct indexing for other elements  |
| Search             | O(n)         | O(n)       | Must scan the tree                     |
| Insert             | O(log n)     | O(log n)   | Element bubbles up to correct position |
| Delete (root)      | O(log n)     | O(log n)   | Remove root, then bubble down          |
| **Space**          | **O(n)**     | **O(n)**   |                                        |

---

### 6. Hashmap (Hash Table / Dictionary)

**Summary:** A hashmap stores **key-value pairs** and uses a **hash function** to map each key to a specific index in an underlying array. This allows O(1) average-time access, insertion, and deletion — you go directly to the right "mailbox" without scanning anything. The main challenge is **hash collisions**, where two keys hash to the same index. These are resolved via chaining (a linked list at that index) or linear probing (finding the next open slot). Worst case (everything collides into one bucket) degrades to O(n). In Python, hashmaps are called **dictionaries**.

**Real-World Example:** A mail room in an office where each employee has a dedicated numbered mailbox. Instead of sorting through every piece of mail, you look up the employee's box number and put it there directly.

| Operation | Average Case | Worst Case | Notes                                        |
| --------- | ------------ | ---------- | -------------------------------------------- |
| Access    | O(1)         | O(n)       | Worst case: all keys collide into one bucket |
| Search    | O(1)         | O(n)       | Same as access                               |
| Insert    | O(1)         | O(n)       | May require collision resolution             |
| Delete    | O(1)         | O(n)       | May require traversing a collision chain     |
| **Space** | **O(n)**     | **O(n)**   |                                              |

---

### 7. Binary Search Tree (BST)

**Summary:** A BST is a tree structure where each node follows a strict ordering rule: the **left child holds values smaller** than the parent, and the **right child holds values greater**. This makes searching very efficient — at each node, you eliminate half the remaining tree. Like a binary search on a sorted dictionary: you open to the middle, decide left or right, and repeat. However, if the tree becomes **unbalanced** (e.g., all insertions go to one side and it looks like a linked list), all operations degrade to O(n).

**Real-World Example:** Searching for a word in a dictionary — you open to the middle, decide if your word comes before or after, then jump to that half and repeat until found.

| Operation | Average Case | Worst Case | Notes                                            |
| --------- | ------------ | ---------- | ------------------------------------------------ |
| Access    | O(log n)     | O(n)       | Worst case: unbalanced tree (like a linked list) |
| Search    | O(log n)     | O(n)       | Half the tree eliminated at each step            |
| Insert    | O(log n)     | O(n)       | Traverse to correct position, then insert        |
| Delete    | O(log n)     | O(n)       | Find node, then restructure                      |
| **Space** | **O(n)**     | **O(n)**   |                                                  |

---

### 8. Set (Hash Set)

**Summary:** A set is a collection that stores **unique elements only** — no duplicates allowed. Under the hood it typically uses a hash table, giving it O(1) average time for insertion, deletion, and membership checks. Sets do **not maintain order** and do **not allow duplicates**. They're extremely useful in coding interviews for tasks like removing duplicates from a list, checking for membership, or performing mathematical set operations (union, intersection, difference).

**Real-World Example:** Thanos's Infinity Gauntlet — it can hold powerful Infinity Stones, but each stone is unique. Try adding the same stone twice and it simply won't work.

| Operation         | Average Case | Worst Case | Notes                                           |
| ----------------- | ------------ | ---------- | ----------------------------------------------- |
| Access / Contains | O(1)         | O(n)       | Hash-based lookup; worst case = many collisions |
| Search            | O(1)         | O(n)       | Same as contains check                          |
| Insert            | O(1)         | O(n)       | Ignored if element already exists               |
| Delete            | O(1)         | O(n)       | Hash-based removal                              |
| **Space**         | **O(n)**     | **O(n)**   |                                                 |

---

## 📊 Master Cheat Sheet

| Data Structure  | Access       | Search       | Insert       | Delete       | Space |
| --------------- | ------------ | ------------ | ------------ | ------------ | ----- |
| **Array**       | O(1)         | O(n)         | O(n)\*       | O(n)\*       | O(n)  |
| **Linked List** | O(n)         | O(n)         | O(1)\*\*     | O(1)\*\*     | O(n)  |
| **Stack**       | O(n)         | O(n)         | O(1)         | O(1)         | O(n)  |
| **Queue**       | O(n)         | O(n)         | O(1)         | O(1)         | O(n)  |
| **Heap**        | O(1)\*\*\*   | O(n)         | O(log n)     | O(log n)     | O(n)  |
| **Hashmap**     | O(1) avg     | O(1) avg     | O(1) avg     | O(1) avg     | O(n)  |
| **BST**         | O(log n) avg | O(log n) avg | O(log n) avg | O(log n) avg | O(n)  |
| **Set**         | O(1) avg     | O(1) avg     | O(1) avg     | O(1) avg     | O(n)  |

> \* O(1) if inserting/deleting at the end of the array
> \*\* O(1) only if you already hold a reference to the node; O(n) if you must search first
> \*\*\* O(1) only for the root (min or max); O(n) for arbitrary elements

---

## 🏆 When to Use What

| Use Case                                    | Best Choice     |
| ------------------------------------------- | --------------- |
| Fast index-based access                     | **Array**       |
| Frequent insertions/deletions in the middle | **Linked List** |
| Undo/redo, function call tracking, DFS      | **Stack**       |
| Task scheduling, BFS, streaming queues      | **Queue**       |
| Always need min or max quickly              | **Heap**        |
| Fast key-value lookup                       | **Hashmap**     |
| Sorted data, range queries                  | **BST**         |
| Deduplication, membership testing           | **Set**         |

---

_Based on the video: ["Data Structures Explained for Beginners - How I Wish I was Taught"](https://www.youtube.com/watch?v=O9v10jQkm5c) by Sajjaad Khader_
