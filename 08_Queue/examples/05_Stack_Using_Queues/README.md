# Example 05: Implement Stack Using Queues (LC 225)

## Problem
Implement a LIFO stack using only two queues.

## Approach
On each push, add to q2 then move all of q1 into q2, then swap q1 and q2. This keeps newest element at front.
**push: O(n)  pop/top/empty: O(1)**