"""LC 703 - Kth Largest Element in a Stream"""
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for n in nums:
            self.add(n)

    def add(self, val):
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

if __name__ == "__main__":
    kl = KthLargest(3, [4,5,8,2])
    adds = [3,5,10,9,4]
    for val in adds:
        print(f"add({val}) -> {kl.add(val)}")
