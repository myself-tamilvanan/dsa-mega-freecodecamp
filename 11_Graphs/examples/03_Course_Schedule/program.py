"""LC 207 - Course Schedule"""
from collections import defaultdict, deque

def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a); indegree[a] += 1
    q = deque(i for i in range(numCourses) if indegree[i] == 0)
    completed = 0
    while q:
        course = q.popleft(); completed += 1
        for next_c in graph[course]:
            indegree[next_c] -= 1
            if indegree[next_c] == 0: q.append(next_c)
    return completed == numCourses

def course_order(numCourses, prerequisites):
    """LC 210 - Return actual order"""
    graph = defaultdict(list)
    indegree = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a); indegree[a] += 1
    q = deque(i for i in range(numCourses) if indegree[i] == 0)
    order = []
    while q:
        c = q.popleft(); order.append(c)
        for nc in graph[c]:
            indegree[nc] -= 1
            if indegree[nc] == 0: q.append(nc)
    return order if len(order) == numCourses else []

if __name__ == "__main__":
    cases = [(2,[[1,0]]),(2,[[1,0],[0,1]]),(4,[[1,0],[2,0],[3,1],[3,2]])]
    for n, prereqs in cases:
        print(f"n={n}, prereqs={prereqs}")
        print(f"  Can finish: {can_finish(n, prereqs)}")
        print(f"  Order: {course_order(n, prereqs)}")
