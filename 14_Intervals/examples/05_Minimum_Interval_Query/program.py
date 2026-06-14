from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        result = [-1] * len(queries)
        heap = []  # (size, end)
        i = 0
        for idx, q in sorted_queries:
            # Add all intervals starting <= q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1
            # Remove intervals ending < q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                result[idx] = heap[0][0]
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.minInterval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]))      # [3,3,1,4]
    print(sol.minInterval([[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]))   # [2,-1,4,6]
