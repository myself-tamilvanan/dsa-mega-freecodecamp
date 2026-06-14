"""LC 56 - Merge Intervals"""
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result

if __name__ == "__main__":
    cases = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,4],[4,5]],
        [[1,4],[2,3]],
        [[1,2],[3,4],[5,6]],
    ]
    for intervals in cases:
        print(f"{intervals} -> {merge(intervals)}")
