# Chapter 08: Queue
FIFO — enqueue at rear, dequeue at front. Use collections.deque.

## Key Usage
- **BFS**: level-order tree, shortest path in graph
- **Circular buffer**: streaming / rate limiting
- **Scheduling**: task processing in order

## BFS Template
```
from collections import deque
q = deque([start]); visited = {start}
while q:
    node = q.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor); q.append(neighbor)
```

## LeetCode Problems
LC 232 Queue Using Stacks, LC 225 Stack Using Queues,
LC 622 Circular Queue, LC 752 Open the Lock, LC 649 DOTA2 Senate
