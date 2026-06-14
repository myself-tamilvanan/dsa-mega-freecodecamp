"""LC 621 - Task Scheduler"""
import heapq
from collections import Counter, deque

def least_interval(tasks, n):
    count = Counter(tasks)
    heap = [-c for c in count.values()]
    heapq.heapify(heap)
    queue = deque()  # (count, available_at_time)
    time = 0
    while heap or queue:
        time += 1
        if heap:
            cnt = 1 + heapq.heappop(heap)  # decrement (was negated)
            if cnt != 0:
                queue.append((cnt, time + n))
        if queue and queue[0][1] == time:
            heapq.heappush(heap, queue.popleft()[0])
    return time

if __name__ == "__main__":
    cases = [(["A","A","A","B","B","B"], 2), (["A","A","A","B","B","B"], 0), (["A","A","A","A","A","A","B","C","D","E","F","G"], 2)]
    for tasks, n in cases:
        print(f"tasks={tasks}, n={n} -> {least_interval(tasks, n)}")
