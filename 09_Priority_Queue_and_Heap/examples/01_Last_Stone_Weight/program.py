"""LC 1046 - Last Stone Weight"""
import heapq

def last_stone_weight(stones):
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        y = -heapq.heappop(heap)
        x = -heapq.heappop(heap)
        if x != y:
            heapq.heappush(heap, -(y - x))
    return -heap[0] if heap else 0

if __name__ == "__main__":
    cases = [[2,7,4,1,8,1], [1], [1,1], [3,3,3]]
    for stones in cases:
        print(f"{stones} -> {last_stone_weight(stones)}")
