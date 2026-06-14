"""LC 743 - Network Delay Time (Dijkstra)"""
import heapq
from collections import defaultdict

def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for u,v,w in times: graph[u].append((w,v))
    dist = {k: 0}
    heap = [(0, k)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float('inf')): continue
        for w, nb in graph[node]:
            new_d = d + w
            if new_d < dist.get(nb, float('inf')):
                dist[nb] = new_d; heapq.heappush(heap, (new_d, nb))
    if len(dist) != n: return -1
    return max(dist.values())

if __name__ == "__main__":
    cases = [([[2,1,1],[2,3,1],[3,4,1]],4,2), ([[1,2,1]],2,1), ([[1,2,1]],2,2)]
    for times,n,k in cases:
        print(f"times={times}, n={n}, k={k} -> {network_delay_time(times,n,k)}")
