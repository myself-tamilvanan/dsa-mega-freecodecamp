"""LC 295 - Find Median from Data Stream"""
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (negate)
        self.large = []  # min-heap

    def addNum(self, num):
        # Push to small
        heapq.heappush(self.small, -num)
        # Ensure small's max <= large's min
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

if __name__ == "__main__":
    mf = MedianFinder()
    stream = [1, 2, 3, 4, 5]
    for num in stream:
        mf.addNum(num)
        print(f"Added {num} -> median = {mf.findMedian()}")
