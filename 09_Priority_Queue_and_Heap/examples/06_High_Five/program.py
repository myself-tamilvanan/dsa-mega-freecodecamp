"""LC 1086 - High Five"""
import heapq
from collections import defaultdict

def high_five(items):
    scores = defaultdict(list)
    for student_id, score in items:
        heapq.heappush(scores[student_id], score)
        if len(scores[student_id]) > 5:
            heapq.heappop(scores[student_id])  # remove smallest
    result = []
    for sid in sorted(scores):
        avg = sum(scores[sid]) // 5
        result.append([sid, avg])
    return result

if __name__ == "__main__":
    items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[2,100],[1,87],[1,100]]
    print("High Five:", high_five(items))
    items2 = [[1,100],[1,99],[1,98],[1,97],[1,96],[1,50]]
    print("Single student:", high_five(items2))
