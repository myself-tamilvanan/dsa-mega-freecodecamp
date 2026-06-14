from typing import List
from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == numCourses else []

if __name__ == "__main__":
    sol = Solution()
    print(sol.findOrder(2, [[1,0]]))              # [0,1]
    print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))  # [0,1,2,3] or similar
    print(sol.findOrder(2, [[1,0],[0,1]]))         # [] (cycle)
