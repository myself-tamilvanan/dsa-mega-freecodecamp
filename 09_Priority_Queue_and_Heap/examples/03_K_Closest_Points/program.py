"""LC 973 - K Closest Points to Origin"""
import heapq

def k_closest(points, k):
    # Max-heap of size k (negate distance)
    heap = []
    for x, y in points:
        dist = -(x*x + y*y)
        heapq.heappush(heap, (dist, x, y))
        if len(heap) > k:
            heapq.heappop(heap)
    return [[x, y] for _, x, y in heap]

def k_closest_sort(points, k):
    """Simple sort approach O(n log n)"""
    return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]

if __name__ == "__main__":
    cases = [([[1,3],[-2,2]], 1), ([[3,3],[5,-1],[-2,4]], 2)]
    for pts, k in cases:
        print(f"points={pts}, k={k} -> {k_closest(pts, k)}")
