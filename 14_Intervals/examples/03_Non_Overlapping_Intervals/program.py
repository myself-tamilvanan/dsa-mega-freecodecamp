"""LC 435 - Non-Overlapping Intervals"""
def erase_overlap_intervals(intervals):
    if not intervals: return 0
    intervals.sort(key=lambda x: x[1])  # sort by end
    removals = 0
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:  # overlap
            removals += 1  # remove current (keep one with earlier end)
        else:
            end = intervals[i][1]
    return removals

if __name__ == "__main__":
    cases = [
        [[1,2],[2,3],[3,4],[1,3]],
        [[1,2],[1,2],[1,2]],
        [[1,2],[2,3]],
    ]
    for intervals in cases:
        print(f"{intervals} -> remove {erase_overlap_intervals(intervals)} interval(s)")
